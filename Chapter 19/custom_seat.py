'''
Austin Richards 5/16/21

custom_seat.py will create custom printable images of
party seating cards.  Each card will have the recipient's
name, generated from guests.txt and will be sized 4in x 5in.
'''
import os
from PIL import Image, ImageDraw, ImageFont

os.chdir('Chapter 19')
os.makedirs('Seating Cards', exist_ok=True)
names = open('guests.txt').readlines()
names = [name.rstrip() for name in names]

for name in names:
    # create a new image and draw object
    im = Image.new('RGBA', (288, 360), 'white')
    draw = ImageDraw.Draw(im)

    # create a font object and draw the text
    font_path = 'C:\\Windows\\Fonts\\arial.ttf'
    arial_font = ImageFont.truetype(font_path, 32)
    draw.text((1, 1), name, fill='indigo')

    #TODO: Add the decorative art to the invitation (using paste method?)

    # save the image with the recipient's name
    im.save(f'Seating Cards\\{name}.png')
