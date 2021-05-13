'''
Follow along project from Chapter 19 of Automate the boring stuff.
I made some of my own edits as I don't like how 

add_logo.py takes a png file and adds a smaller version of it in
the corner of all image files in the specified folder.
'''
import os
from PIL import Image

os.chdir('Chapter 19')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
            continue
    
    print(f'Processing {filename}...')
    im = Image.open(filename)
    width, height = im.size

    #TODO make this resizing section into a function for later use
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    print(f'Adding logo to {filename}...')
    im.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    os.makedirs('withLogo', exist_ok=True)
    im.save(os.path.join('withLogo', filename))
    print()
