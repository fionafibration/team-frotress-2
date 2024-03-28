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
    print("Copy config_default.py to config.py and edit it to set up!")
    exit()

# Checking resolution and setting screenshot regions for uber bar
# Currently WIP, want to add 2560x1440 support but for now its hardcoded to 1920x1080
medic_uber_support = True
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
        medic_uber_support = False
        print("Detected incompatible resolution! \
                        Currently supported resolutions are:\n1920x1080\nMedic Uber Charge functionality will not work")
    else:
        medic_uber_support = False
        print("Detected incompatible resolution! \
                Currently supported resolutions are:\n1920x1080\nMedic Uber Charge functionality will not work")
# This does not check for resolution and really should
elif platform == 'Windows':
    print("Detected Windows OS. If your resolution is not 1920x1080, Medic Uber Charge functionality will not work.")
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


def uber_image_grabber(dxc=None):
    if platform == "Linux":
        return ImageGrab.grab(full_bar_region)
    elif platform == "Windows":
        frame = None
        while frame is None:
            frame = dxc.grab(full_bar_region)
        return Image.fromarray(frame)


def uber_percentage_grabber(dxc):
    if platform == 'Linux':
        img = uber_image_grabber()

    elif platform == 'Windows':
        img = uber_image_grabber(dxc)

    # Count filled vs. background bar pixels
    count = 0
    cocount = 0

    # we grab a little bit extra so clip it
    for i in range(1, bar_width - 2):
        pixel = img.getpixel((i, 2))
        # normal and full charge colours respectively
        if pixel == (255, 255, 255) or pixel == (200, 226, 255):
            count += 1
        # background colour
        if pixel == (53, 53, 53):
            cocount += 1

    # Check to ensure nothing is occluding our
    if count + cocount != bar_width - 3:
        return None

    uber_percent = count / (bar_width - 3)
    uber_percent = round(uber_percent * 100)
    if 0 <= uber_percent <= 100:
        return uber_percent
    else:
        return None


async def main(rcon, logfile, dxc=None):
    client = Client("Team Frotress 2")  # :3

    connector = WebsocketConnector(INTIFACE_SERVER_ADDR, logger=client.logger)

    console = log_tailer.LogTail(logfile)
    _ = console.read()

    try:
        await client.connect(connector)
    except:
        logging.error("Could not connect!")
        return

    client.logger.info("Connected to Intiface!")

    if len(client.devices) == 0:
        logging.error("No devices!")
        return

    logging.info("Executing Team Frotress config files")

    # enables class and weapon switch functionality
    rcon.execute("exec teamfrotress")
    if ENABLE_WEAPONSWITCH:
        rcon.execute("exec teamfrotress_switcher")

    # get steam username to detect killfeed data
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

    vibe = vibration_handler.VibrationHandler(logging, rcon)

    while True:
        # detect kills & class / weapon switches from console log
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
                    vibe.killstreak = 0
                    vibe.uberstreak = 0

                elif switch_match[1] in ["slot1", "slot2", "slot3"]:
                    curr_weapon = int(switch_match[1][-1])

            if killfeed_match := re.match(
                    """\d\d\/\d\d\/\d\d\d\d - \d\d:\d\d:\d\d: ([^\n]{0,32}) killed ([^\n]{0,32}) with (\w+)\. ?(\(crit\))?""",
                    line):

                if killfeed_match[1] == name:  # we got a kill
                    logging.info(
                        f"Kill logged, streak: {vibe.killstreak}{', crit' if killfeed_match[4] is not None else ''}")
                    vibe.kill(killfeed_match[4] is not None)
                if killfeed_match[2] == name:  # we died :(
                    logging.info("Death logged")
                    vibe.death()

        if curr_class == "medic" and medic_uber_support and (curr_weapon == 2 or curr_weapon == 3):
            uber_grabbed = uber_percentage_grabber(dxc)
            # logging.info(f"New uber: {uber_grabbed}")
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

        # run vibrator
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
        tf2_args = ["~/.steam/bin32/steam-runtime/run.sh", TF2_GAME_EXECUTABLE]

    added_args = (
            " -game tf -steam -secure -usercon +developer 1 +alias developer +ip 0.0.0.0 +alias ip +sv_rcon_whitelist_address 127.0.0.1 +alias sv_rcon_whitelist_address +rcon_password " + rcon_password + " +alias rcon_password +hostport " + str(
        RCON_PORT) + " +alias hostport +alias cl_reload_localization_files +net_start +con_timestamp 1 +alias con_timestamp -condebug -conclearlog " + TF2_EXTRA_LAUNCH_OPTIONS).split()
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
