# Team Frotress 2

Controls buttplug based on kills, deaths, and uber in Team Fortress 2

Requires the use of the OMPHUD edit in the repository for Uber capturing & other configuration details!

# Setup

Copy config_default.py to config.py and fill out your game executable and console.log paths (console.log will be in tf
folder)

Install OMPHUD-sexy on your game, make sure every class config has `$classname` in it somewhere, i.e. medic.cfg has a
line `$medic`, heavyweapons.cfg has a line `$heavyweapons`. 

# More than one device or actuator

Edit the run_buzz method in vibration_handler.py to your liking


