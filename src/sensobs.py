from abc import ABC, abstractmethod


class Sensob(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_value(self):
        pass


class ObjectSideProximity(Sensob):
    def __init__(self, irporoximity_sensor):
        self.ir_proximity_sensors = irporoximity_sensor

    def get_value(self):
        return self.ir_proximity_sensors.get_value()


class PickedUp(Sensob):
    def __init__(self, reflectance_sensors, reflectance_treshold):
        self.reflectance_sensors = reflectance_sensors
        # sets the treshold sum for the sensors for which the robot will take a picture
        self.reflectance_treshold = reflectance_treshold

    def get_value(self):
        values = self.reflectance_sensors.get_value()
        return sum(values) < self.reflectance_treshold

class UltrasonicTracking(Sensob):
    def __init__(self, ultrasonic_sensors, max_tracking_distance_cm, min_tracking_distance_cm):
        self.ultrasonic_sensor = ultrasonic_sensors
        self.max_tracking_distance_cm = max_tracking_distance_cm
        self.min_tracking_distance_cm = min_tracking_distance_cm

    def get_value(self):
        return self.ultrasonic_sensor.get_value()

class BlackImage(Sensob):
    def __init__(self, camera):
        self.camera = camera

    def is_dark(self, pixel):
        return (pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50)

    def get_value(self):
        im = self.camera.get_value()
        dark_pixels = 0
        for pixel in im.getdata():
            if self.is_dark(pixel):
                dark_pixels += 1
        ratio = dark_pixels / len(im.getdata())
        return ratio

