'''
Follow along project from Chapter 19 of Automate the boring stuff

add_logo.py takes a png file and adds a smaller version of it in
the corner of all image files in the specified folder.
'''
import os
from PIL import Image
from selective_copy import get_all_paths

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

#TODO do a list comprehension to get image files