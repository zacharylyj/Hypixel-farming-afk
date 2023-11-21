from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con  
       
def lclick(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      

time.sleep(3)
print("now")
i = 1
while(not(keyboard.is_pressed('ctrl'))):
    if(keyboard.is_pressed('[')):
        i = 0
        print("start")
    while(i == 0):   
        if(keyboard.is_pressed(']')):
            i = 1
            print("stop")

        if (pyautogui.pixel(777, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(777,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(832, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(832,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(886, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(886,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(940, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(940,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(993, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(993,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(1047, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(1047,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))
        if (pyautogui.pixel(1100, 417)[0] == 56):
            #time.sleep(0.1)
            lclick(1100,497)
            time.sleep(0.05)
            win32api.SetCursorPos((60,500))

