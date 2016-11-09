from abc import ABC, abstractmethod

class Sensob(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class ObjectSideProximity(Sensob):
    def __init__(self, irporoximity_sensor):
        self.ir_proximity_sensors = irporoximity_sensor

    def update(self):
        return self.ir_proximity_sensors.update()

    def get_value(self):
        return self.ir_proximity_sensors.get_value()

    def reset(self):
        self.ir_proximity_sensors.reset()


class PickedUp(Sensob):
    def __init__(self, reflectance_sensors, reflectance_treshold):
        self.reflectance_sensors = reflectance_sensors
        # sets the treshold sum for the sensors for which the robot will take a picture
        self.reflectance_treshold = reflectance_treshold

    def update(self):
        self.reflectance_sensors.update()

    def get_value(self):
        values = self.reflectance_sensors.get_value()
        return sum(values) < self.reflectance_treshold

    def reset(self):
        self.reflectance_sensors.reset()


class UltrasonicTracking(Sensob):
    def __init__(self, ultrasonic_sensors, max_tracking_distance_cm, min_tracking_distance_cm):
        self.ultrasonic_sensor = ultrasonic_sensors
        self.max_tracking_distance_cm = max_tracking_distance_cm
        self.min_tracking_distance_cm = min_tracking_distance_cm

    def update(self):
        return self.ultrasonic_sensor.update()

    def get_value(self):
        value = self.ultrasonic_sensor.get_value
        return value < self.max_tracking_distance_cm and value > self.min_tracking_distance_cm

    def reset(self):
        self.ultrasonic_sensor.update()
