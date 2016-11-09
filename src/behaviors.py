import time

from abc import ABC, abstractmethod


class Behaviour(ABC):
    """Represents an behaviour and its priority."""
    def __init__(self):
        pass

    """Execute the behaviour.

    The Behaviour should manipulate the peripherals on the robot in this function.
    """
    @abstractmethod
    def execute(self, robot):
        pass

    """Get a number between 0 and 1 that represents the priority of this task.

    Greater numbers mean greater priority. This should be dynamic depending on various sensob readings.
    """
    @abstractmethod
    def get_priority_weight(self, robot):
        pass

class WiggleBehaviour(Behaviour):
    def execute(self, robot):
        robot.motob.update([1, -1])
        time.sleep(0.25)
        robot.motob.update([-1, 1])
        time.sleep(0.5)
        robot.motob.update([1, -1])
        time.sleep(0.25)
        robot.motob.update([0, 0])

    def get_priority_weight(self, robot):
        # TODO: Implement this
        return 1