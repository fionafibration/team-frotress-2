from config import *
import logging
import re
import subprocess
import string
import asyncio
import sys
import os
import platform
import random

from valve.rcon import RCON
from PIL import ImageGrab, Image
from buttplug import *

import log_tailer
import vibration_handler

platform = platform.system()

if platform == "Windows":
    import dxcam

if not os.path.isfile("config.py"):
    print("Copy config_default.py to config.py and change to set up!")
    exit()

# Checking resolution and setting screenshot regions for uber bar
if platform == 'Linux':
    resolution_raw = \
        subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[
            0].split()[
            0].split(b'x')
    resolution = (int(resolution_raw[0].decode('UTF-8')), int(resolution_raw[1].decode('UTF-8')))
    if resolution == (1920, 1080):
        bar_center = (960, 744)
        bar_width = 340
        bar_height = 16
        bar_left = bar_center[0] - bar_width // 2
        bar_right = bar_center[0] + bar_width // 2
        bar_top = bar_center[1] - bar_height // 2
        bar_bottom = bar_center[1] + bar_height // 2
        bar_tenth = bar_width // 10
        full_bar_region = (bar_left, bar_top, bar_right, bar_bottom)
    elif resolution == (2560, 1440):
        print("Detected incompatible resolution! \
                        Currently supported resolutions are:\n1920x1080")
        exit()
    else:
        print("Detected incompatible resolution! \
                Currently supported resolutions are:\n1920x1080")
        exit()
elif platform == 'Windows':
    bar_center = (960, 744)
    bar_width = 340
    bar_height = 16
    bar_left = bar_center[0] - bar_width // 2
    bar_right = bar_center[0] + bar_width // 2
    bar_top = bar_center[1] - bar_height // 2
    bar_bottom = bar_center[1] + bar_height // 2
    bar_tenth = bar_width // 10
    full_bar_region = (bar_left, bar_top, bar_right, bar_bottom)
else:
    print("Detected incompatible operating system! \
            Currently supported operating systems are:\nLinux and Windows")
    exit()


def uber_image_grabber(dxc=None, n=10, percentile=False):
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
    if platform == "Linux":
        if percentile:
            return ImageGrab.grab(bar_left + bar_tenth * (n - 1), bar_top, bar_left + bar_tenth * (n), bar_bottom)
        else:
            return ImageGrab.grab(full_bar_region)
    elif platform == "Windows":
        frame = None
        while frame is None:
            frame = dxc.grab(full_bar_region)
        return Image.fromarray(frame)


"""
Creating the pixel dictionary.
Keys are the percentiles, values are their pixel ranges.
TODO: WHY
"""
number_pixel_dict = {
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0],
    10: [0, 0],
}
for i in range(10):
    number_pixel_dict[i + 1] = [bar_left + bar_tenth * (i), bar_left + +bar_tenth * (i + 1)]


def uber_percentage_grabber(dxc):
    if platform == 'Linux':
        img = uber_image_grabber()

    elif platform == 'Windows':
        img = uber_image_grabber(dxc)

    # Count filled vs. background bar pixels
    count = 0
    cocount = 0
    for i in range(1, bar_width - 1):
        pixel = img.getpixel((i, 2))
        if pixel == (255, 255, 255) or pixel == (200, 226, 255):
            count += 1
        elif pixel == (53, 53, 53):
            cocount += 1

    if (count + cocount) == 0:
        return None

    uber_percent = count / (count + cocount)
    uber_percent = round(uber_percent * 100)
    assert (0 <= uber_percent <= 100)
    return uber_percent


async def main(rcon, logfile, dxc=None):
    client = Client("Team Frotress 2")  # :3

    connector = WebsocketConnector("ws://127.0.0.1:12345", logger=client.logger)

    console = log_tailer.LogTail(logfile)
    _ = console.read()

    try:
        await client.connect(connector)
    except:
        logging.error("Could not connect!")
        return

    client.logger.info("Connected to Intiface!")

    if len(client.devices) != 0:
        device = client.devices[0]

        if len(device.actuators) != 0:
            await device.actuators[0].command(0.1)

        else:
            logging.error("No actuators!")
            return

        await asyncio.sleep(1)
        await device.actuators[0].command(0)
    else:
        logging.error("No devices!")
        return

    logging.info("Executing Team Frotress config files")

    rcon.execute("exec teamfrotress")
    if ENABLE_WEAPONSWITCH:
        rcon.execute("exec teamfrotress_switcher")

    name = None
    logging.info("Getting name...")
    while name is None:
        try:
            name_response = rcon.execute("name")
            name_response_text = name_response.text
            name = re.match('"name" = "([^\n]+)" \( def. "unnamed" \)', name_response_text)
        except UnicodeDecodeError:
            pass

    name = name[1]

    logging.info(f"Got name: {name}")

    logging.info("Ready to play!")

    current_uber = 0
    last_uber = 0
    currently_ubered = False
    curr_class = ""
    curr_weapon = -1

    vibe = vibration_handler.VibrationHandler()

    while True:
        if curr_class == "medic" and curr_weapon == 2:
            uber_grabbed = uber_percentage_grabber(dxc)
        else:
            uber_grabbed = None

        # handle uber
        if uber_grabbed is not None:
            last_uber = current_uber
            current_uber = uber_grabbed

            # activate uber
            if last_uber > current_uber != 0:
                logging.info("Activated Uber!")
                currently_ubered = True
                vibe.start_uber()

            # else if we have risen in uber
            elif current_uber > last_uber:
                vibe.uber_milestone(current_uber, last_uber)

            # uber ended
            if currently_ubered and (current_uber == 0 or current_uber > last_uber):
                logging.info("Uber ended!")
                currently_ubered = False
                vibe.end_uber()

        # detect kills from console output
        while True:
            line = console.read_line()
            if line is None:
                break

            if switch_match := re.match("""\d\d\/\d\d\/\d\d\d\d - \d\d:\d\d:\d\d: teamfrotress_(\w+)""", line):
                if switch_match[1] in ["scout", "soldier", "pyro", "heavyweapons", "demoman", "engineer", "medic",
                                       "sniper",
                                       "spy"]:
                    curr_class = switch_match[1]
                    logging.info(f"New class: {curr_class}")
                elif switch_match[1] in ["slot1", "slot2", "slot3"]:
                    curr_weapon = int(switch_match[1][-1])
                    logging.info(f"Changed weapon to slot {curr_weapon}")

            if killfeed_match := re.match(
                    """\d\d\/\d\d\/\d\d\d\d - \d\d:\d\d:\d\d: ([^\n]{0,32}) killed ([^\n]{0,32}) with (\w+)(\.|(\. \(crit\)))""",
                    line):

                if killfeed_match[1] == name:  # we got a kill
                    logging.info(f"Kill logged, streak: {vibe.killstreak}")

                    vibe.kill()
                if killfeed_match[2] == name:  # we died :(
                    logging.info("Death logged")
                    vibe.death()

        await vibe.run_buzz(devices=client.devices)

        await asyncio.sleep(1.0 / UPDATE_SPEED)


if __name__ == "__main__":
    print("Press enter to launch TF2!")
    input()

    chars = string.digits + string.ascii_letters

    address = ("127.0.0.1", RCON_PORT)

    if os.path.isfile("rconpass.txt"):
        with open("rconpass.txt", "r") as f:
            rcon_password = f.read().strip()
    else:
        rcon_password = ''.join([random.choice(chars) for i in range(32)])
        with open("rconpass.txt", "w") as f:
            f.write(rcon_password)

    if platform == "Windows":
        tf2_args = [TF2_GAME_EXECUTABLE]
    else:
        tf2_args = ["steam -applaunch 440 "]

    added_args = (
            " -game tf -steam -secure -usercon +developer 1 +alias developer +ip 0.0.0.0 +alias ip +sv_rcon_whitelist_address 127.0.0.1 +alias sv_rcon_whitelist_address +rcon_password " + rcon_password + " +alias rcon_password +hostport " + str(
        RCON_PORT) + " +alias hostport +alias cl_reload_localization_files +net_start  +con_timestamp 1 +alias con_timestamp -condebug -conclearlog " + TF2_EXTRA_LAUNCH_OPTIONS).split()
    tf2_args.extend(added_args)

    subprocess.Popen(tf2_args)

    print("Wait until TF2 has made it to the main menu, then press enter")
    input()

    rcon = RCON(address, rcon_password)
    rcon.connect()
    rcon.authenticate()

    if platform == "Windows":
        dxc = dxcam.create()
    else:
        dxc = None

    print("Ensure Intiface Central is running and has your device connected, then press enter")
    input()

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    with open(TF2_CONSOLE_LOG, "r") as f:
        asyncio.run(main(rcon, f, dxc=dxc))
