import motobs

from abc import ABC, abstractmethod


class Behaviour(ABC):
    """Represents an behaviour and its priority."""
    def __init__(self):
        pass

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


class WiggleBehaviour(Behaviour):
    def get_motor_recs(self):
        return [
            motobs.move_left(0.4, 0.25),
            motobs.move_right(0.4, 0.5),
            motobs.move_left(0.4, 0.25),
            motobs.stop()
        ]

    def get_priority_weight(self):
        # TODO: Implement this
        return 1