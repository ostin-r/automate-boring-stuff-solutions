'''
Follow along project from Chapter 19 of Automate the boring stuff.
I made some of my own edits as I don't like how 

add_logo.py takes a png file and adds a smaller version of it in
the corner of all image files in the specified folder.
'''
import os
from PIL import Image


def resize_image(size, filename):
    '''
    resize_image takes a max size and image filename as arguments
    and returns an image object that has resized the file.  This 
    resize function preserves the aspect ratio.
    '''
    im = Image.open(filename)
    width, height = im.size

    if width > size and height > size:
        if width > height:
            height = int((size / width) * height)
            width = size
        else:
            width = int((size / height) * width)
            height = size

        print(f'Resizing {filename}...')
        resized_im = im.resize((width, height))
        return resized_im
    else:
        return im


def main():
    SQUARE_FIT_SIZE = 300
    LOGO_FILENAME = 'catlogo.png'
    LOGO_SIZE = 10 # logo will be 10x time smaller than image

    # open the logo image and resize
    logo_img = resize_image(int(SQUARE_FIT_SIZE / LOGO_SIZE), LOGO_FILENAME)
    logo_width, logo_height = logo_img.size

    for filename in os.listdir('.'):
        #TODO maybe I should just resie the logo for EVERY file????

        # skip files that aren't images
        file_lower = filename.lower()
        if not (file_lower.endswith('.png') or file_lower.endswith('.jpg') \
            or file_lower.endswith('.gif') or file_lower.endswith('.bmp')) \
            or filename == LOGO_FILENAME:
                continue
        
        # open the image file, resize if necessary
        print(f'Processing {filename}...')
        im = resize_image(SQUARE_FIT_SIZE, filename)
        width, height = im.size

        #TODO check if the image is too small for the logo
            #TODO: check that ratio of width to logo_width and height to logo_heigth is >= LOGO_SIZE
                #TODO: change logo_width or logo_height such that width/logowidth = LOGO_SIZE
                # written as an equation: new_logo_width = width / LOGO_SIZE

        # add the logo to the image
        print(f'Adding logo to {filename}...')
        im.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

        # save the results in a new folder labelled "withLogo"
        os.makedirs('withLogo', exist_ok=True)
        im.save(os.path.join('withLogo', filename))
        print()

os.chdir('Chapter 19')
main()
