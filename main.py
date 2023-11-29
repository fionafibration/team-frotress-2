import logging
from valve.rcon import RCON
import subprocess
import string
import asyncio
import sys
import os
import platform
import pytesseract
#import dxcam
import random

from PIL import ImageGrab, Image

# from buttplug import *

platform = platform.system()

# Checking resolution and setting screenshot regions for uber bar
if platform == 'Linux':
    resolution_raw = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0].split()[0].split(b'x')
    resolution = (int(resolution_raw[0].decode('UTF-8')),int(resolution_raw[1].decode('UTF-8')))
    if resolution == (1920,1080):           
        bar_center = (960,744)
        bar_width = 340
        bar_height = 16
        bar_left = bar_center[0]-bar_width/2
        bar_right = bar_center[0]+bar_width/2
        bar_top = bar_center[1]-bar_height/2
        bar_bottom = bar_center[1]+bar_height/2
        bar_tenth = bar_width/10
        full_bar_region = (bar_left, bar_top, bar_right, bar_bottom)
    elif resolution == (2560, 1440):
        # TODO
        pass
    else:
        logging.error("Detected incompatible resolution! \
                Currently supported resolutions are:\n1920x1080 and 2560x1440")
elif platform == 'Windows':
    # TODO
    resolution = (2560,1440)
else:
    logging.error("Detected incompatible operating system! \
            Currently supported operating systems are:\nLinux and Windows")


UBER_ACTIVE_STRENGTH = 0.2
UBER_THRESHOLD_BUZZ = 0.3

rcon_port = 2541

def uber_image_grabber(n=10, percentile=False):
    """
    INPUT: 
        n=9
            An integer, specifies which tenth is of interest. 
            Defaults to 10, the last tenth.
        percentile=False
            A Boolean, specifies whether tenth is stopping point or not.
            For example, (n=5, percintile=False) screenshots the first half
            but (n=5, percentile=True) screenshots only the 40-49 region
        
    """
    if percentile:
       return ImageGrab.grab(bar_left + tenth*(n-1), top, left + tenth*(n), bottom)
    else:
        return ImageGrab.grab(full_bar_region)

"""
Creating the pixel dictionary.
Keys are the percentiles, values are their pixel ranges.
"""
number_pixel_dict = {
    1:  [0, 0], 
    2:  [0, 0],
    3:  [0, 0],
    4:  [0, 0],
    5:  [0, 0],
    6:  [0, 0],
    7:  [0, 0],
    8:  [0, 0],
    9:  [0, 0],
    10: [0, 0],
}
for i in range(10):
    number_pixel_dict[i+1] = [bar_left+bar_tenth*(i), bar_left++bar_tenth*(i+1)]


def uber_percentage_grabber(dxc=None):
    if platform == 'Linux':
        img = uber_image_grabber()

    elif platform == 'Windows':
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

if platform == 'Linux':
    tf2_game_executable = "/home/dani/.local/share/Steam/steamapps/common/Team Fortress 2/hl2.sh"
elif platform == 'Windows':
    tf2_game_executable = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\hl2.exe"
else:
    logging.error("Detected incompatible operating system! \
            Currently supported operating systems are:\nLinux and Windows")

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
