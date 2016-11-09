import time
import behaviors
from arbitrator import Arbitrator
from motobs import MotOb

class BBCon:

    def __init__(self):
        self.sensobs = []
        self.behaviors = []
        self.active_behaviors = [behaviors.WiggleBehaviour()]
        self.arbitrator = Arbitrator()
        self.motobs = [MotOb()]

    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)
    
    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def wait(self):
        time.sleep(0.5)

    def run_one_timestep(self):
        # Update all sensobs
        print('Updating sensobs')
        for sensob in self.sensobs:
            sensob.update()
        # Update all behaviors
        # for behavior in self.active_behaviors:
        #     behavior.update()

        # Let arbitrator choose action
        chosen_behavior = self.arbitrator.choose_behavior(self.active_behaviors)

        print('Chosen behavior: %s' % chosen_behavior)

        motor_recs = chosen_behavior.get_motor_recs()

        print('Motor recs: %s' % motor_recs)

        # Update the motobs based on the motor recommendations
        for motor_rec in motor_recs:
            for motob in self.motobs:
                motob.react(motor_rec)
        # Wait
        self.wait()

        # REset all sensobs
        for sensob in self.sensobs:
            sensob.reset()
          
    
