from abc import ABC, abstractmethod


class Action(ABC):
    """Continuously manipulates the peripherals of the robot, and holds the state for this manipulation."""
    def __init__(self):
        pass

    """Update the Action.

    The Action should also manipulate the peripherals on the robot in this function.
    """
    @abstractmethod
    def update(self, robot):
        pass


class WiggleAction(Action):
    def __init__(self):
        self.time = 0
        self.direction_multiplier = 1

    def update(self, robot):
        robot.motob.update([self.direction_multiplier, -self.direction_multiplier])
        self.time += 1
        if self.time > 40:
            self.direction_multiplier *= -1
