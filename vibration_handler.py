import time
from config import *


class VibrationHandler:
    def __init__(self, logger, rcon):
        self.logger = logger
        self.rcon = rcon
        self.uber_strength = 0  # uber active strength
        self.timed_buzzes = []  # list of timed vibration activations
        self._curr_strength = 0  # current strength priv variable
        self.last_strength = 0
        self.killstreak = 0  # killstreak tracking
        self.uberstreak = 0

    @property
    def current_strength(self):
        return self._curr_strength

    @current_strength.setter
    def current_strength(self, new_strength):
        if new_strength > self._curr_strength:
            self._curr_strength = new_strength

    def timed_buzz(self, strength, time_end):
        self.timed_buzzes.append((strength, time.time() + time_end))
        self.current_strength = strength

    def death(self):
        self.killstreak = 0
        self.timed_buzz(DEATH_STRENGTH, DEATH_TIME)

    def kill(self, crit=False):
        self.killstreak += 1
        # [0, 1]
        killstreak_coeff = min(self.killstreak, KILLSTREAK_MAX) / (KILLSTREAK_MAX)

        self.timed_buzz(KILL_STRENGTH *
                        # [1, KILLSTREAK_STRENGTH_MULTIPLIER]
                        (killstreak_coeff * (KILLSTREAK_STRENGTH_MULTIPLIER - 1.0) + 1.0) *
                        KILL_CRIT_STRENGTH_MULTIPLIER if crit else 1.0,
                        KILL_TIME *
                        # [1, KILLSTREAK_TIME_MULTIPLIER]
                        (killstreak_coeff * (KILLSTREAK_TIME_MULTIPLIER - 1.0) + 1.0) *
                        KILL_CRIT_TIME_MULTIPLIER if crit else 1.0)

    def uber_milestone(self, uber_percent, last_uber_percent):
        for i, x in enumerate(UBER_MILESTONES):
            if uber_percent > x >= last_uber_percent:
                self.logger.info(f"Hit Uber milestone {x}")
                uber_milestone_coeff = i / len(UBER_MILESTONES) - 1
                self.timed_buzz(
                    UBER_MILESTONE_STRENGTH *
                    (uber_milestone_coeff * (UBER_MILESTONE_STRENGTH_MULTIPLIER - 1.0) + 1.0),
                    UBER_MILESTONE_TIME *
                    (uber_milestone_coeff * (UBER_MILESTONES_TIME_MULTIPLIER - 1.0) + 1.0)
                )

    def start_uber(self):
        self.uber_strength = UBER_ACTIVE_STRENGTH * (UBER_STREAK_MULTIPLIER ** self.uberstreak)

    def end_uber(self):
        self.uber_strength = 0
        self.uberstreak += 1

    def update(self):
        self.last_strength = self.current_strength
        self._curr_strength = BASE_VIBE

        now = time.time()

        for timer in self.timed_buzzes:
            if now <= timer[1]:
                self.current_strength = timer[0]

        self.current_strength = self.uber_strength

        self.timed_buzzes = list(filter(lambda x: x[1] > now, self.timed_buzzes))

        if self.current_strength > BASE_VIBE and self.last_strength <= BASE_VIBE
            if ACTIVATE_COMMAND:
                self.rcon.execute(ACTIVATE_COMMAND)
        elif self.current_strength <= BASE_VIBE and self.last_strength > BASE_VIBE
            if DEACTIVATE_COMMAND:
                self.rcon.execute(DEACTIVATE_COMMAND)

        return self.current_strength

    # Takes a list of devices and activates devices based on vibration handling
    async def run_buzz(self, devices):
        vibe_strength = self.update()

        # activate all actuators
        for device in devices.values():
            for actuator in device.actuators:
                await actuator.command(vibe_strength)
        #
        # could also do this
        # await devices[0].actuators[0].command(vibe_strength)
        # await devices[0].actuators[1].command(vibe_strength * 0.5)
        # etc.
