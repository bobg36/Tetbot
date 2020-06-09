from PIL import ImageGrab
import os
import time

x_pad = 655
y_pad = 510


def screenGrab():
    box = (x_pad, y_pad, x_pad + 1000, y_pad + 1200)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()
