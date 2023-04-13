import random
import time
import keyboard
import win32api
import win32con
from pyautogui import *
import pyautogui
import pywinauto

times = 46

def keyD():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    pyautogui.keyDown('d')
    

def keyA():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    pyautogui.keyDown('a')
    

def keyWl():
    pyautogui.keyDown('w')
    time.sleep(1.4)
    pyautogui.keyUp('w')
    time.sleep(0.01)
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')

def keyWr():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    pyautogui.keyDown('w')
    time.sleep(1.4)
    pyautogui.keyUp('w')
    time.sleep(0.01)
    pyautogui.keyDown('d')
    time.sleep(0.5)
    pyautogui.keyUp('d')


def resetup():
    pyautogui.keyUp('a')
    pyautogui.keyUp('d')


time.sleep(2)
app = pywinauto.application.Application().connect(title='SkyClient (Forge 1.8.9)')
window = app.window(title='SkyClient (Forge 1.8.9)')
window.set_focus()
time.sleep(0.5)
window.type_keys('{ESC}')
time.sleep(0.2)


while not(keyboard.is_pressed('ctrl')):
    keyA()
    time.sleep(times + random.randint(0, 110)/100)
    resetup()
    keyWr()
    keyD()
    time.sleep(times + random.randint(0, 110)/100)
    resetup()
    keyWl()
win32apei.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)