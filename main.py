from pyautogui import *
import win32api, win32con
import time
import keyboard
import random

time.sleep(2)


# 255 52 59 Red Color
# region values: Top Left 600,400
# region values: Bot Right 1300,800
# region value : 600,400,700,400
def clicker(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q' or 'm') == False:

    pic = screenshot('sc.png', region=(660, 350, 600, 400))

    width, height = pic.size

    for x in range(0, width,5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))

            if b == 195:
                clicker(x+660,y+350)
                time.sleep(0.1)
                break
