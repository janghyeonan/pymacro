import pyautogui
from pynput import keyboard
import time
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
        if key.char == '1':
            pyautogui.moveTo(x=890, y=343)
            pyautogui.doubleClick()
            pyautogui.moveTo(x=350, y=500)
        elif key.char == '`':
            pyautogui.moveTo(x=800, y=41114462)
            pyautogui.doubleClick()
        elif key.char == '2':
            pyautogui.moveTo(x=800, y=700)
        elif key.char == '3':
            pyautogui.click()
        elif key.char == '4':
            pyautogui.moveTo(x=1020, y=180)
            pyautogui.doubleClick()
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))
def on_release(key):
    print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
