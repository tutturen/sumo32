import time
from arbitrator import Arbitrator
import motobs

class BBCon:

    def __init__(self, behaviors):
        self.sensobs = []
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
        for sensob in self.sensobs:
            sensob.update()

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
