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
calibrated = False
def print_reflectance():
    global calibrated
    sensor = reflectance.ReflectanceSensors()
    if not calibrated:
        for i in range(5):
            sensor.calibrate()
            time.sleep(1)
        calibrated = True
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

