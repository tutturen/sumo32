import actions
from abc import ABC, abstractmethod


class Behaviour(ABC):
    """Represents an Action and its priority."""
    def __init__(self):
        pass

    """Create a new Action object to be executed by the robot.

    This allows the Behaviour to execute an action with state, which can not be held by the Behaviour itself.
    """
    @abstractmethod
    def create_action(self):
        pass

    """Get a number between 0 and 1 that represents the priority of this task.

    Greater numbers mean greater priority. This should be dynamic depending on various sensob readings.
    """
    @abstractmethod
    def get_priority_weight(self, robot):
        pass


class WiggleBehaviour(Behaviour):
    def create_action(self):
        return actions.WiggleAction()

    def get_priority_weight(self, robot):
        # TODO: Implement this
        return 1