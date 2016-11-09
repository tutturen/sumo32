import random

class Arbitrator:
    def choose_behavior(self, behaviours):
        behaviour_weights = [behaviour.get_priority_weight() for behaviour in behaviours]
        total_weight = sum(behaviour_weights)

        rand_choice = random.random() * total_weight
        accumulated_weight = 0
        for i, behaviour_weight in enumerate(behaviour_weights):
            accumulated_weight += behaviour_weight
            if rand_choice <= accumulated_weight:
                return behaviours[i]
