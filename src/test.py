#import library.robodemo as robodemo
import library.ultrasonic as ultrasonic
import library.reflectance_sensors as reflectance
import library.irproximity_sensor as ir
import time

# ultrasonic
def print_ultrasonic():
    sensor = ultrasonic.Ultrasonic()
    sensor.update()
    value = sensor.get_value()
    print(value)

# ir-proximity
def print_ir_proximity():
    sensor = ir.IRProximitySensor()
    sensor.update()
    value = sensor.get_value()
    print(value)

# reflectance
def print_reflectance():
    sensor = reflectance.ReflectanceSensors()
    sensor.update()
    value = sensor.get_value()
    print(value)

if __name__ == '__main__':
    print('Testing ultrasonic...')
    #robodemo.dancer()
    while True:
        print_ultrasonic()
        print_ir_proximity()
        print_reflectance()
        time.sleep(1)

