from library.motors import Motors
from abc import ABC, abstractmethod


class ActionOb(ABC):
    @abstractmethod
    def apply(self, rec):
        pass


class MotOb(ActionOb):
    def __init__(self):
        self.motors = Motors()

    def apply(self, rec):
        rec.apply_to_motors(self.motors)


class CamOb(ActionOb):
    def __init__(self, camera):
        self.camera = camera

    def apply(self, rec):
        rec.apply_to_camera(self.camera)
