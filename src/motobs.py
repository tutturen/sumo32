from library.motors import Motors

class MotorRec:
    def __init__(self, action, speed, duration):
        self.action = action
        self.speed = speed
        self.duration = duration

    def __str__(self):
        return 'MotorRec(%s, %.2f, %.2f)' % (self.action, self.speed, self.duration)

# Motor recs
def move_left(speed, duration):
    return MotorRec('MOVE_LEFT', speed, duration)

def move_right(speed, duration):
    return MotorRec('MOVE_RIGHT', speed, duration)

def move_forward(speed, duration):
    return MotorRec('MOVE_FORWARD', speed, duration)

def move_backward(speed, duration):
    return MotorRec('MOVE_BACKWARD', speed, duration)

def stop():
    return MotorRec('STOP', 0, 0)

class MotOb:

    def __init__(self):
        self.motors = Motors()

    def react(self, rec):
        print('Reacting on: %s' % rec)
        if rec.action == 'MOVE_LEFT':
            print('MOVING LEFT')
            self.motors.left(rec.speed, rec.duration)
        elif rec.action == 'MOVE_RIGHT':
            self.motors.right(rec.speed, rec.duration)
        elif rec.action == 'MOVE_FORWARD':
            self.motors.forward(rec.speed, rec.duration)
        elif rec.action == 'MOVE_BACKWARD':
            self.motors.backward(rec.speed, rec.duration)
        elif rec.action == 'STOP':
            self.motors.stop()
