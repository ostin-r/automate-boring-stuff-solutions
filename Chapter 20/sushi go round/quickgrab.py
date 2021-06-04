'''
quickgrab.py is the backbone of the sushi go round bot- it is how it sees the screen
'''
from PIL import ImageGrab
import os
import time

def screenGrab():
    box = (228, 579, 1507, 1538)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()