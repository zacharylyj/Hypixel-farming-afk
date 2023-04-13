import random
import time
import keyboard
import win32api
import win32con
from pyautogui import *
import pyautogui
import pywinauto


times = 19.4

def keyS():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    pyautogui.keyDown('s')

def keyA():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    pyautogui.keyDown('a')

def keyW():
    time.sleep(0.01)
    pyautogui.keyDown('w')
    time.sleep(0.05)
    pyautogui.keyUp('w')
    time.sleep(0.01)
    pyautogui.keyDown('s')
    time.sleep(0.055)
    pyautogui.keyUp('s')
    time.sleep(0.05)

def resetup():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    
time.sleep(2)
app = pywinauto.application.Application().connect(title='SkyClient (Forge 1.8.9)')
window = app.window(title='SkyClient (Forge 1.8.9)')
window.set_focus()
time.sleep(1)
window.type_keys('{ESC}')


while not(keyboard.is_pressed('ctrl')):
    while not(keyboard.is_pressed('ctrl')):
        keyS()
        time.sleep(times)
        resetup()
        keyA()
        time.sleep(times)
        resetup()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    while not(keyboard.is_pressed('=')):
        print("waiting")