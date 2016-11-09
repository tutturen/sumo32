import motobs

from abc import ABC, abstractmethod

class Behavior(ABC):
    """Represents a behavior and its priority."""
    def __init__(self, sensob_controller):
        self.sensob_controller = sensob_controller

    """Get motor recommendations for this behaviour, and execute additional things if necessary."""
    @abstractmethod
    def get_motor_recs(self):
        pass

    """Get a number between 0 and 1 that represents the priority of this task.

    Greater numbers mean greater priority. This should be dynamic depending on various sensob readings.
    """
    @abstractmethod
    def get_priority_weight(self):
        pass


class WiggleBehaviour(Behavior):
    def get_motor_recs(self):
        return [
            motobs.move_left(0.4, 0.25),
            motobs.move_right(0.4, 0.5),
            motobs.move_left(0.4, 0.25),
            motobs.stop()
        ]

    def get_priority_weight(self):
        # TODO: Implement this
        return 0.2

class TurnLeftBehavior(Behavior):

    def get_motor_recs(self):
        return [
            motobs.move_left(0.5, 0.5)
        ]

    def get_priority_weight(self):
        is_something_left = self.sensob_controller.object_side_proximity.get_value()[0]
        return 0.8 if is_something_left else 0.0

class TurnRightBehavior(Behavior):
    def get_motor_recs(self):
        return [
            motobs.move_right(0.5, 0.5)
        ]

    def get_priority_weight(self):
        is_something_right = self.sensob_controller.object_side_proximity.get_value()[1]
        return 0.8 if is_something_right else 0.0