#   functions to grab screen is here

#   =========below are commands to use pyautogui
#   =========to detect RGB and screen coords to set up your tetris
#	1. python
#   2. import pyautogui
#	3. pyautogui.displayMousePosition()

from PIL import ImageGrab
import os
import time

x_pad = 838
y_pad = 100


def screenGrabSave():
    box = (x_pad, y_pad, x_pad + 1524, y_pad + 1548)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def screenGrab():
    box = (x_pad, y_pad, x_pad + 1524, y_pad + 1548)
    im = ImageGrab.grab(box)
    return im


def main():
    screenGrab()


if __name__ == '__main__':
    main()
