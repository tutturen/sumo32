import random

class Arbitrator:
    def choose_behavior(self, behaviors):
        behavior_weights = [behavior.get_priority_weight() for behavior in behaviors]
        total_weight = sum(behavior_weights)

        rand_choice = random.random() * total_weight
        accumulated_weight = 0
        for i, behavior_weight in enumerate(behavior_weights):
            accumulated_weight += behavior_weight
            if rand_choice <= accumulated_weight:
                return behaviors[i]
