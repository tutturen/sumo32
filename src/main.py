from bbcon import BBCon


def main():
    bbcon = BBCon()
    for i in range(5):
        print('Running timestep %i' % i)
        bbcon.run_one_timestep()

if __name__ == '__main__':
    main()
