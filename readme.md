# sumo32 robot

## behaviours

Tries to find objects to take pictures of. When an object is located, it wiggles back and forth, waiting to be picked up

- If no objects are detected - drive around randomly
- If something is is detected by the ultrasonic in front - go towards it
- If something is too close to the ultrasonic in front - back away
- If something is in an appropriate distance to the ultrasonic in front - stop and wiggle
- If all the reflective sensors are low - take pictures
- If something is on the side of the robot - turn towards it

##BBCON
- add_behavior()
- add_sensob()
- activate_behavior()
- deactivate_behavior()
- wait()
- run_one_timestep()

##SenOb
- update()
- get_value()
- reset()

##Behavior
- update(): MotorRec

##MotOb
- update(rec: MotorRec)

##Arbitrator
- choose_action(behaviors: Array<Behavior>)
