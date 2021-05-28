'''
Austin Richards 5/28/21

mouse_nudge.py subtley moves the mouse so that
the computer does not sleep while the user is away
'''
from pyautogui import sleep, move

print('Program started.  Press Ctrl-C to stop.')

while True:
    sleep(60)
    move(1, 1)
    move(-1, -1)