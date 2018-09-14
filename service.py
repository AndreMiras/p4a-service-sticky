from __future__ import print_function

from time import sleep


def main():
    i = 0
    while True:
        print("service:", i)
        sleep(1)
        i += 1


if __name__ == '__main__':
    main()
