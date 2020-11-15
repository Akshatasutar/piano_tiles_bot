from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#pyautogui.displayMousePosition
#rgb value of black 0,0,0
#          X, Y
#tile_1: 767, 433
#tile_2: 888, 433
#tile_3: 1023, 433
#tile_4: 1147, 433
positions = [767, 888, 1023, 1147]

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #press down
    time.sleep(0.01) #hold for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)  #press up

while keyboard.is_pressed('q') == False:
    #[0] is R, [1] is G, [2] is B
    if pyautogui.pixel(767, 433)[0] == 0:
       click(767, 433)
    if pyautogui.pixel(888, 433)[0] == 0:
       click(888, 433)
    if pyautogui.pixel(1023, 433)[0] == 0:
       click(1023, 433)
    if pyautogui.pixel(1147, 433)[0] == 0:
       click(1147, 433)
       
    #for pos in positions:
        #if pyautogui.pixel(pos, 433)[0] == 0:  
            #click(pos, 433)

