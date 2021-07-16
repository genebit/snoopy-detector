
import pyautogui
import keyboard
import sys

mouse_position = None

running = True
while running:
    try:
        mouse_position = pyautogui.position()

        print('Mouse is at: ({0} {1})'.format(mouse_position.x, mouse_position.y))

        # if keyboard.read_hotkey():
        #     print('A key is pressed')
        #     break

    except Exception as err:
        print('An error occured', err)
        break
