from bbcon import BBCon
from library.zumo_button import ZumoButton

def main():
    print('Start -> Press knappen.')
    ZumoButton().wait_for_press()
    bbcon = BBCon()
    for i in range(5):
        print('Running timestep %i' % i)
        bbcon.run_one_timestep()

if __name__ == '__main__':
    main()
