import logging
from valve.rcon import RCON
import subprocess
import string
import asyncio
import sys
import os
import pytesseract
import dxcam
import random

from PIL import Image

from buttplug import *

x = 2560 // 2 - 70
y = 1440 // 2 + 350

xoff, yoff = 140, 55

UBER_ACTIVE_STRENGTH = 0.2
UBER_THRESHOLD_BUZZ = 0.3

rcon_port = 2541


def uber_percentage_grabber(dxc):
    frame = dxc.grab(region=(x, y, x + xoff, y + yoff))
    if frame is None:
        print("No new image!")
        return None

    img = Image.fromarray(frame)

    img.save("screencap.png")

    uber_str = pytesseract.image_to_string(img, config="--psm 8").strip()

    if uber_str:
        if uber_str[-1] == "%":
            try:
                uber_int = int(uber_str[:-1])
                if 0 <= uber_int <= 100:
                    return uber_int
                return None
            except:
                print("bad int")
                return None
        else:
            print("no %")
    return None


tf2_game_executable = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\hl2.exe"


async def main():
    client = Client("TF2 Healsluttery")

    connector = WebsocketConnector("ws://127.0.0.1:12345", logger=client.logger)

    try:
        await client.connect(connector)
    except:
        logging.error("Could not connect!")
        return

    await client.start_scanning()
    await asyncio.sleep(5)
    await client.stop_scanning()

    client.logger.info(f"Devices: {client.devices}")

    if len(client.devices) != 0:
        device = client.devices[0]

        if len(device.actuators) != 0:
            await device.actuators[0].command(0.5)

        else:
            logging.error("No actuators!")
            return

        await asyncio.sleep(1)
        await device.actuators[0].command(0)

        input("Ready!")
    else:
        logging.error("No devices!")
        return

    current_uber = 0
    last_uber = 0
    currently_ubered = False
    camera = dxcam.create()
    while True:
        logging.info(f"Screengrabbing")
        uber_grabbed = uber_percentage_grabber(camera)

        if uber_grabbed is not None:
            logging.info(f"Got new Uber: {uber_grabbed}")
            last_uber = current_uber
            current_uber = uber_grabbed

        if last_uber > current_uber != 0:
            currently_ubered = True
            logging.info("Activated Uber!")
            await device.actuators[0].command(UBER_ACTIVE_STRENGTH)

        if currently_ubered and (current_uber == 0 or current_uber > last_uber):
            currently_ubered = False
            logging.info("Deactivated Uber!")
            await device.actuators[0].command(0)

        await asyncio.sleep(0.5)


chars = string.digits + string.ascii_letters

address = ("127.0.0.1", rcon_port)

if os.path.isfile("rconpass.txt"):
    with open("rconpass.txt", "r") as f:
        rcon_password = f.read().strip()
else:
    rcon_password = ''.join([random.choice(chars) for i in range(32)])
    with open("rconpass.txt", "w") as f:
        f.write(rcon_password)

tf2_args = [tf2_game_executable]
added_args = (
        " -game tf -steam -secure -usercon +developer 1 +alias developer +ip 0.0.0.0 +alias ip +sv_rcon_whitelist_address 127.0.0.1 +alias sv_rcon_whitelist_address +rcon_password " + rcon_password + " +alias rcon_password +hostport " + str(
    rcon_port) + " +alias hostport +alias cl_reload_localization_files +net_start  +con_timestamp 1 +alias con_timestamp -condebug -conclearlog -windowed -noborder -novid").split()
tf2_args.extend(added_args)

subprocess.Popen(tf2_args)

input()

rcon = RCON(address, rcon_password)
rcon.connect()
rcon.authenticate()

input()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

if __name__ == "__main__":
    asyncio.run(main())
