TF2_GAME_EXECUTABLE = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\hl2.exe"
TF2_CONSOLE_LOG = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\console.log"
TF2_EXTRA_LAUNCH_OPTIONS = "-novid -nojoy -nosteamcontroller -nohltv -particles 1 -precachefontchars -noquicktime"

INTIFACE_SERVER_ADDR = "ws://127.0.0.1:12345"  # The address intiface central is listening on

RCON_PORT = 2541  # Change if you have another port interfering

# Binds custom weapon switching functionality to track weapon changes
ENABLE_WEAPONSWITCH = True

UPDATE_SPEED = 5  # Speed in updates per second, values higher than 10 are not recommended for performance

BASE_VIBE = 0.0  # Base vibration speed that motor will always be on

ACTIVATE_COMMAND = ""  # TF2 console command to execute when vibrator is turned on
DEACTIVATE_COMMAND = ""  # Command to execute when vibrator is turned off

KILL_STRENGTH = 0.3  # Base kill vibration strength (0 to disable)
KILL_TIME = 1  # Kill vibration time

KILL_CRIT_STRENGTH_MULTIPLIER = 2.0  # Crit kill vibration multiplier
KILL_CRIT_TIME_MULTIPLIER = 1.0  # Crit kill time multiplier

# When at KILLSTREAK_MAX, vibration strength is KILL_STRENGTH * KILLSTREAK_STRENGTH_MULTIPLIER
# When you get first kill, vibration strength is KILL_STRENGTH * 1.0
KILLSTREAK_STRENGTH_MULTIPLIER = 2  # Amount that reaching KILLSTREAK_MAX should multiply strength
KILLSTREAK_TIME_MULTIPLIER = 1.5  # Amount that reaching KILLSTREAK_MAX should multiply time

KILLSTREAK_MAX = 20  # Max killstreak for scaling

DEATH_STRENGTH = 0  # Death vibration strength
DEATH_TIME = 0  # Death vibration time

UBER_ACTIVE_STRENGTH = 0.5  # Uber activation vibration strength (0 to disable)
UBER_STREAK_MULTIPLIER = 1.1  # Multipies uber strength by this per uber

UBER_MILESTONES = [25, 50, 75, 99]
UBER_MILESTONE_STRENGTH = 0.2  # Uber milestone passed vibration strength (0 to disable)
UBER_MILESTONE_TIME = 1  # Uber milestone vibration time

# When you pass the highest milestone, this will multiply UBER_MILESTONE_STRENGTH / UBER_MILESTONE_TIME
# When at the lowest milestone, multiplier will be only 1.0
UBER_MILESTONE_STRENGTH_MULTIPLIER = 1.0
UBER_MILESTONES_TIME_MULTIPLIER = 1.0  # See above
