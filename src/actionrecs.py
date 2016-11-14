from abc import ABC, abstractmethod

import time


class ActionRec(ABC):
    @abstractmethod
    def apply_to_motors(self, motors):
        pass

    @abstractmethod
    def apply_to_camera(self, camera):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MotorRec(ActionRec):
    def __init__(self, speed, duration):
        self.speed = speed
        self.duration = duration

    def apply_to_camera(self, camera):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MoveLeft(MotorRec):
    def apply_to_motors(self, motors):
        motors.left(self.speed, self.duration)

    def __str__(self):
        return 'MoveLeft(%.2f, %.2f)' % (self.speed, self.duration)


class MoveRight(MotorRec):
    def apply_to_motors(self, motors):
        motors.right(self.speed, self.duration)

    def __str__(self):
        return 'MoveRight(%.2f, %.2f)' % (self.speed, self.duration)


class MoveForward(MotorRec):
    def apply_to_motors(self, motors):
        motors.forward(self.speed, self.duration)

    def __str__(self):
        return 'MoveForward(%.2f, %.2f)' % (self.speed, self.duration)


class MoveBackward(MotorRec):
    def apply_to_motors(self, motors):
        motors.forward(self.speed, self.duration)

    def __str__(self):
        return 'MoveBackward(%.2f, %.2f)' % (self.speed, self.duration)


class Stop(ActionRec):
    def apply_to_motors(self, motors):
        motors.stop()

    def apply_to_camera(self, camera):
        pass

    def __str__(self):
        return 'Stop'


class TakePicture(ActionRec):
    def apply_to_motors(self, motors):
        pass

    def apply_to_camera(self, camera):
        camera.get_value().save('./images/' + str(time.time()) + '.jpg', 'JPEG')

    def __str__(self):
        return 'TakePicture'
