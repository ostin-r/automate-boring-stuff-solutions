'''
Austin Richards 5/28/21

mouse_nudge.py subtley moves the mouse so that
the computer does not sleep while the user is away
'''
import pyautogui as gui

print('Program started.  Press Ctrl-C to stop.')

while True:
    gui.sleep(60)
    gui.move(1, 1)
    gui.move(-1, -1)
    