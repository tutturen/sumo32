import time
from arbitrator import Arbitrator
import motobs

from library.irproximity_sensor import IRProximitySensor
from library.reflectance_sensors import ReflectanceSensors
from library.ultrasonic import Ultrasonic
import sensobs

class SensObController():

    def __init__(self):
        self.sensor = {
            'proximity': IRProximitySensor(),
            'reflectance': ReflectanceSensors(),
            'ultrasonic': Ultrasonic()
        }
        self.object_side_proximity = sensobs.ObjectSideProximity(self.sensor['proximity'])
        self.picked_up = sensobs.PickedUp(self.sensor['reflectance'], 1)
        self.ultrasonic_tracking = sensobs.UltrasonicTracking(self.sensor['ultrasonic'], 100, 10)

    def update(self):
        # Update all sensors one time
        for key in self.sensor:
            self.sensor[key].update()

class BBCon:

    def __init__(self, sensob_controller, behaviors):
        self.sensob_controller = sensob_controller
        self.behaviors = behaviors
        self.arbitrator = Arbitrator()
        self.motobs = [motobs.MotOb()]

    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)
    
    def wait(self):
        time.sleep(0.5)

    def run_one_timestep(self):
        # Update all sensobs
        print('Updating sensobs')
        self.sensob_controller.update()

        # Update all behaviors
        # for behavior in self.active_behaviors:
        #     behavior.update()

        # Let arbitrator choose action
        chosen_behavior = self.arbitrator.choose_behavior(self.behaviors)

        print('Chosen behavior: %s' % chosen_behavior)

        motor_recs = chosen_behavior.get_motor_recs()

        # Update the motobs based on the motor recommendations
        for motor_rec in motor_recs:
            for motob in self.motobs:
                motob.react(motor_rec)

    def stop(self):
        for motob in self.motobs:
            motob.react(motobs.stop())
