'''
Austin Richards 5/16/21

custom_seat.py will create custom printable images of
party seating cards.  Each card will have the recipient's
name, generated from guests.txt and will be sized 4in x 5in.
'''
import os
from PIL import Image, ImageDraw, ImageFont
from add_logo import resize_image

os.chdir('Chapter 19')
os.makedirs('Seating Cards', exist_ok=True)

names = open('guests.txt').readlines()
names = [name.rstrip() for name in names]

# initialize card size, get the art image and size it
WIDTH, HEIGHT = (288, 360)
art_im = resize_image(int(HEIGHT / 2), 'flower_decoration.png').convert('RGBA')

for name in names:
    # create a new image with black border
    im = Image.new('RGBA', (WIDTH, HEIGHT), 'black')
    fill = Image.new('RGBA', (WIDTH + 4, HEIGHT + 4), 'white')
    im.paste(fill, (2, 2), fill)

    # create draw object, font object
    draw = ImageDraw.Draw(im)
    font_path = 'C:\\Windows\\Fonts\\arial.ttf'
    arial_font = ImageFont.truetype(font_path, 60)

    # center the text by getting the size of the name
    name_width, name_height = draw.textsize(name, font=arial_font)
    name_location = (int((WIDTH - name_width) / 2), HEIGHT - 280)

    # draw text, add flower decoration, save image
    draw.text(name_location, name, fill='indigo', font=arial_font)
    im.paste(art_im, (80, 210), art_im)
    im.save(f'Seating Cards\\{name}.png')
