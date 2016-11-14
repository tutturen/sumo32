from library.motors import Motors
from abc import ABC, abstractmethod


class MotorRec(ABC):
    def __init__(self, speed, duration):
        self.speed = speed
        self.duration = duration

    @abstractmethod
    def apply(self, motors):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MoveLeft(MotorRec):
    def apply(self, motors):
        motors.left(self.speed, self.duration)

    def __str__(self):
        return 'MoveLeft(%.2f, %.2f)' % (self.speed, self.duration)


class MoveRight(MotorRec):
    def apply(self, motors):
        motors.right(self.speed, self.duration)

    def __str__(self):
        return 'MoveRight(%.2f, %.2f)' % (self.speed, self.duration)


class MoveForward(MotorRec):
    def apply(self, motors):
        motors.forward(self.speed, self.duration)

    def __str__(self):
        return 'MoveForward(%.2f, %.2f)' % (self.speed, self.duration)


class MoveBackward(MotorRec):
    def apply(self, motors):
        motors.forward(self.speed, self.duration)

    def __str__(self):
        return 'MoveBackward(%.2f, %.2f)' % (self.speed, self.duration)


class Stop(MotorRec):
    def __init__(self):
        super().__init__(0, 0)

    def apply(self, motors):
        motors.stop()

    def __str__(self):
        return 'Stop'


class MotOb:
    def __init__(self):
        self.motors = Motors()

    def react(self, rec):
        print('Reacting on: %s' % rec)
        rec.apply(self.motors)
