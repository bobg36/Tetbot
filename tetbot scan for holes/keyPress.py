# key press functions
import os
import time
import win32api
import win32con

sleepTime = 0.05


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")


def waitStart():
    started = False
    while (started == False):
        for i in range(1, 256):
            if win32api.GetAsyncKeyState(i):
                if(i == 87):
                    started = True
        time.sleep(0.1)


def moveLeft():
    win32api.keybd_event(win32con.VK_LEFT, 0, 0x0000, 0)
    time.sleep(sleepTime)
    win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_KEYUP, 0)


def moveRight():
    win32api.keybd_event(win32con.VK_RIGHT, 0, 0x0000, 0)
    time.sleep(sleepTime)
    win32api.keybd_event(win32con.VK_RIGHT, 0, win32con.KEYEVENTF_KEYUP, 0)


def moveUp():
    win32api.keybd_event(win32con.VK_UP, 0, 0x0000, 0)
    time.sleep(sleepTime)
    win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_KEYUP, 0)


def hardDrop():
    win32api.keybd_event(win32con.VK_SPACE, 0, 0x0000, 0)
    time.sleep(sleepTime)
    win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_KEYUP, 0)


def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''

    win32api.keybd_event(0x57, 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
