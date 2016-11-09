from bbcon import BBCon, SensObController
import behaviors
from library.zumo_button import ZumoButton


def main():
    print('Start -> Press knappen.')
    zumo_button = ZumoButton()
    zumo_button.wait_for_press()

    sensob_controller = SensObController()

    behaviorList = [
        behaviors.WiggleBehaviour(sensob_controller),
        behaviors.TurnLeftBehavior(sensob_controller),
        #behaviors.AvoidRightBehavior(sensob_controller),
        #behaviors.AvoidFrontBehavior(sensob_controller),
        #behaviors.PickedUpBehavior(sensob_controller)
    ]

    bbcon = BBCon(sensob_controller, behaviorList)
    while True:
        bbcon.run_one_timestep()
        if zumo_button.get_pressed():
            bbcon.stop()
            break

if __name__ == '__main__':
    main()
