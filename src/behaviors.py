from random import randint

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
    def __init__(self, sensob_controller, preferred_distance, threshold):
        super().__init__(sensob_controller)
        self.preferred_distance = preferred_distance
        self.threshold = threshold

    def get_motor_recs(self):
        return [
            motobs.move_left(0.2, 0.25),
            motobs.move_right(0.2, 0.5),
            motobs.move_left(0.2, 0.25),
            motobs.stop()
        ]

    def get_priority_weight(self):
        distance = self.sensob_controller.ultrasonic_tracking.get_value()
        if distance < 50:
            delta = distance - self.preferred_distance
            if abs(delta) < self.threshold:
                return 0.4

        return 0

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


class ApproachBehavior(Behavior):
    def __init__(self, sensob_controller, preferred_distance, threshold):
        super().__init__(sensob_controller)
        self.preferred_distance = preferred_distance
        self.threshold = threshold

    def get_motor_recs(self):
        distance = self.sensob_controller.ultrasonic_tracking.get_value()
        if distance < self.preferred_distance:
            return [
                motobs.move_backward(0.3, 0.5)
            ]
        else:
            return [
                motobs.move_forward(0.3, 0.5)
            ]

    def get_priority_weight(self):
        distance = self.sensob_controller.ultrasonic_tracking.get_value()
        if distance < 50:
            delta = distance - self.preferred_distance
            if abs(delta) > self.threshold:
                return 0.4

        return 0


class PickedUpBehavior(Behavior):
    def get_motor_recs(self):
        return [
            motobs.stop()
        ]

    def get_priority_weight(self):
        if self.sensob_controller.picked_up.get_value():
            return 1
        else:
            return 0


class DriveRandomlyBehavior(Behavior):
    def __init__(self, sensob_controller, motor_recs):
        super().__init__(sensob_controller)
        self.motor_recs = motor_recs

    def get_motor_recs(self):
        return [
            self.motor_recs[randint(len(self.motor_recs) - 1)]
        ]

    def get_priority_weight(self):
        return 0.01
