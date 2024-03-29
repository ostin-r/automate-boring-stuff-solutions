'''
quickgrab.py initializes where the game is on the screen via startGame()
and then grabs images of the game screen using screenGrab()

This program assumes a screen resolution of 2736 x 1824 and using google chrome
as the primary webbrowser.
x_pad and y_pad are used for easy maintenance for the game play area- these
are located 1 pixel outside the top left corner of the game.
Play Area = x_pad+1, y_pad+1, 1507, 1559
'''
from PIL import ImageGrab
import os
import time

# globals ------
x_pad = 39
y_pad = 618
# --------------

def screenGrab():
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()