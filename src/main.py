from bbcon import BBCon
import behaviors
from library.zumo_button import ZumoButton


def main():
    print('Start -> Press knappen.')
    zumo_button = ZumoButton()
    zumo_button.wait_for_press()
    bbcon = BBCon([behaviors.WiggleBehaviour()])
    while True:
        bbcon.run_one_timestep()
        if zumo_button.get_pressed():
            bbcon.stop()
            break

if __name__ == '__main__':
    main()
