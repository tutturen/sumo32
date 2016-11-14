from bbcon import BBCon, SensObController
import behaviors
import actionrecs
from library.zumo_button import ZumoButton


def main():
    print('Start -> Press knappen.')
    zumo_button = ZumoButton()
    zumo_button.wait_for_press()

    sensob_controller = SensObController()

    behaviorList = [
        behaviors.BackOffBehavior(sensob_controller),
        behaviors.WiggleBehaviour(sensob_controller, 30, 5),
        behaviors.TurnLeftBehavior(sensob_controller),
        behaviors.TurnRightBehavior(sensob_controller),
        behaviors.ApproachBehavior(sensob_controller, 30, 5),
        behaviors.PickedUpBehavior(sensob_controller),
        behaviors.DriveRandomlyBehavior(sensob_controller, [
            actionrecs.MoveForward(0.25, 1),
            actionrecs.MoveRight(0.5, 0.5),
            actionrecs.MoveLeft(0.5, 0.5),
        ]),
        behaviors.TakePictureBehavior(sensob_controller)
    ]

    bbcon = BBCon(sensob_controller, behaviorList)
    while True:
        bbcon.run_one_timestep()
        if zumo_button.get_pressed():
            bbcon.stop()
            break

if __name__ == '__main__':
    main()
