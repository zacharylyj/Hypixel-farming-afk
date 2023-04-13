import random
import time
import keyboard
import pyautogui
from Xlib import X, display
import Xlib.XK
import Xlib.ext.xtest

times = 19.4

def keyS():
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.keyDown('s')

def keyA():
    pyautogui.mouseDown(button='left')
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
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    
time.sleep(2)
disp = display.Display()
root = disp.screen().root
win_id = None
while not win_id:
    win_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType).value[0]
window = disp.create_resource_object('window', win_id)
window.set_input_focus(X.RevertToParent, X.CurrentTime)
time.sleep(1)
pyautogui.typewrite(['esc'])


while not(keyboard.is_pressed('ctrl')):
    while not(keyboard.is_pressed('ctrl')):
        keyS()
        time.sleep(times)
        resetup()
        keyA()
        time.sleep(times)
        resetup()
    pyautogui.mouseUp(button='left')
    while not(keyboard.is_pressed('=')):
        print("waiting")