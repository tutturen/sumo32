import time

from library.motors import Motors
from abc import ABC, abstractmethod


class ActionRec(ABC):
    @abstractmethod
    def apply_to_motors(self, motors):
        pass

    @abstractmethod
    def apply_to_camera_(self, camera):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MotorRec(ActionRec):
    def __init__(self, speed, duration):
        self.speed = speed
        self.duration = duration

    def apply_to_camera_(self, camera):
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


class Stop(MotorRec):
    def __init__(self):
        super().__init__(0, 0)

    def apply_to_motors(self, motors):
        motors.stop()

    def __str__(self):
        return 'Stop'


class TakePicture(ActionRec):
    def apply_to_motors(self, motors):
        pass

    def apply_to_camera_(self, camera):
        camera.update().save('images/' + str(time.time()) + '.jpg', 'JPEG')

    def __str__(self):
        return 'TakePicture'


class MotOb:
    def __init__(self):
        self.motors = Motors()

    def react(self, rec):
        print('Reacting on: %s' % rec)
        rec.apply_to_motors(self.motors)
