from pyautogui import *
import win32api , win32con
import time
import keyboard
import random

time.sleep(5)
 #255 52 59 Red Color
 # region values: Top Left 600,400
 # region values: Bot Right 1300,800
 # region value : 600,400,700,400
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q' or 'm') == False:
    target = locateOnScreen('target.png',confidence=0.9)
    x,y = center(target)
    click(x,y)
    time.sleep(0.005)