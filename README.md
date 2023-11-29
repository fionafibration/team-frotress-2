# Team Frotress 2

Controls smart sex toys based on kills, deaths, and uber in Team Fortress 2, using the Intiface Central backbone to connect to hardware

Linux suppport is currently slightly broken pending further testing

Uber tracking requires the use of the OMPHUD-sexy edit

# Features
- Custom vibration strength and time for kills, death, using Uber, and passing milestones of Ubercharge percent
- Multipliers for critical kills, killstreaks, and "Uberstreaks"
- Planned support for further features involving config file scripting, such as weapon & class specific functionality
- Planned suport for assist tracking features as well (if anyone knows a good way to do this please reach out!)

# Setup

Copy config_default.py to config.py and fill out your game executable and console.log paths (console.log will be in tf
folder)

If you want medic functionality, install OMPHUD-sexy on your game, make sure every class config has `$classname` in it somewhere, i.e. medic.cfg has a
line `$medic`, heavyweapons.cfg has a line `$heavyweapons`. 

# Customising for multiple devices/motors

Edit the run_buzz method in vibration_handler.py to your liking


