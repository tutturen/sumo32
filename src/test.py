import library.robodemo as robodemo
import library.ultrasonic as ultrasonic
import library.reflectance_sensors as reflectance
import library.irproximity_sensor as ir
import time

class SensorPrinter():
    def __init__(self):
        self.ultrasonic_sensor = ultrasonic.Ultrasonic()
        self.ir = ir.IRProximitySensor()
        self.reflectance_sensor = reflectance.ReflectanceSensors(True)

    def print_ultrasonic(self):
        self.ultrasonic_sensor.update()
        value = self.ultrasonic_sensor.get_value()
        print(value)

    def print_ir_proximity(self):
        self.ir.update()
        value = self.ir.get_value()
        print(value)

    def print_reflectance(self):
        self.reflectance_sensor.update()
        value = self.reflectance_sensor.get_value()
        print(value)

def test_sensors():
    print('Testing sensors...')
    printer = SensorPrinter()
    while True:
        printer.print_ultrasonic()
        printer.print_ir_proximity()
        printer.print_reflectance()
        time.sleep(1)

def test_dance():
    print('Testing dancer...')
    robodemo.dancer()

if __name__ == '__main__':
    test_dance()
