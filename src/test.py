import library.robodemo as robodemo
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

# reflectance

if __name__ == '__main__':
    print('Testing ultrasonic...')
    #robodemo.dancer()
    while True:
        print_ultrasonic()
        time.sleep(1)

