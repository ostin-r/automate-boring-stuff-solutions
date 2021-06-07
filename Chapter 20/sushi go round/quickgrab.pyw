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
x_pad = 227
y_pad = 599
# --------------

def screenGrab():
    '''
    saves an image of the play area to the hard drive
    '''
    box = (x_pad+1, y_pad+1, x_pad+1280, y_pad+960)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()