import time
from config import *


class VibrationHandler:
    def __init__(self):
        self.uber_strength = 0  # uber active strength
        self.timed_buzzes = []  # list of timed vibration activations
        self._curr_strength = 0  # current strength priv variable
        self.killstreak = 0  # killstreak tracking

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

    def kill(self):
        self.killstreak += 1
        # [0, 1]
        killstreak_coeff = min(self.killstreak, KILLSTREAK_MAX) / (KILLSTREAK_MAX)

        self.timed_buzz(KILL_STRENGTH *
                        # [1, KILLSTREAK_STRENGTH_MULTIPLIER]
                        (killstreak_coeff * (KILLSTREAK_STRENGTH_MULTIPLIER - 1) + 1),
                        KILL_TIME *
                        # [1, KILLSTREAK_TIME_MULTIPLIER]
                        (killstreak_coeff * (KILLSTREAK_TIME_MULTIPLIER - 1) + 1))

    def uber_milestone(self, uber_percent, last_uber_percent):
        for i, x in enumerate(UBER_MILESTONES):
            if uber_percent > x >= last_uber_percent:
                print(f"Hit milestone {x}")
                uber_milestone_coeff = i / len(UBER_MILESTONES) - 1
                self.timed_buzz(
                    UBER_MILESTONE_STRENGTH *
                    (uber_milestone_coeff * (UBER_MILESTONE_STRENGTH_MULTIPLIER - 1) + 1),
                    UBER_MILESTONE_TIME *
                    (uber_milestone_coeff * (UBER_MILESTONES_TIME_MULTIPLIER - 1) + 1)
                )

    def start_uber(self):
        self.uber_strength = UBER_ACTIVE_STRENGTH

    def end_uber(self):
        self.uber_strength = 0

    def update(self):
        self._curr_strength = 0

        now = time.time()

        for timer in self.timed_buzzes:
            if now <= timer[1]:
                self.current_strength = timer[0]

        self.current_strength = self.uber_strength

        self.timed_buzzes = list(filter(lambda x: x[1] > now, self.timed_buzzes))

        return self.current_strength

    # Takes a list of devices and activates devices based on vibration handling
    async def run_buzz(self, devices):
        vibe_strength = self.update()

        await devices[0].actuators[0].command(vibe_strength)
        # await devices[0].actuators[1].command(vibe_strength * 0.5)
        #
        # to set all actuators:
        #
        # for device in devices:
        #     for actuator in device.actuators:
        #         await actuator.command(vibe_strength)
        #
        # etc.
