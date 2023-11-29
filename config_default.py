TF2_GAME_EXECUTABLE = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\hl2.exe"
TF2_CONSOLE_LOG = "E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\console.log"
TF2_EXTRA_LAUNCH_OPTIONS = "-novid -nojoy -nosteamcontroller -nohltv -particles 1 -precachefontchars -noquicktime"

RCON_PORT = 2541

# Binds custom weapon switching functionality to track weapon changes
ENABLE_WEAPONSWITCH = True

UPDATE_SPEED = 5  # Speed in updates per second, values higher than 10 are not recommended for performance

KILL_STRENGTH = 0.5  # Base kill vibration strength (0 to disable)
KILL_TIME = 1  # Kill vibration time

# When at KILLSTREAK_MAX, vibration strength is KILL_STRENGTH * KILLSTREAK_STRENGTH_MULTIPLIER
# When you get first kill, vibration strength is KILL_STRENGTH * 1.0
KILLSTREAK_STRENGTH_MULTIPLIER = 1.4  # Amount that reaching KILLSTREAK_MAX should multiply strength
KILLSTREAK_TIME_MULTIPLIER = 3  # Amount that reaching KILLSTREAK_MAX should multiply time

KILLSTREAK_MAX = 20  # Max killstreak for scaling

DEATH_STRENGTH = 0  # Death vibration strength
DEATH_TIME = 0  # Death vibration time

UBER_ACTIVE_STRENGTH = 0.5  # Uber activation vibration strength (0 to disable)

UBER_MILESTONES = [25, 50, 75]
UBER_MILESTONE_STRENGTH = 0.2  # Uber milestone passed vibration strength (0 to disable)
UBER_MILESTONE_TIME = 1  # Uber milestone vibration time

# When you pass the highest milestone, this will multiply UBER_MILESTONE_STRENGTH / UBER_MILESTONE_TIME
# When at the lowest milestone, multiplier will be only 1.0
UBER_MILESTONE_STRENGTH_MULTIPLIER = 1.0
UBER_MILESTONES_TIME_MULTIPLIER = 1.0  # See above
