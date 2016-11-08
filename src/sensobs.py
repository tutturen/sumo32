from abc import ABC, abstractmethod


class Sensob(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass
