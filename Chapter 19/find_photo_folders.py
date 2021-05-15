'''
Austin Richards 5/15/21

find_photo_folders goes through ever folder on the specified
directory and looks for image files and specifically sorts out
whether they are a camera photo or just an image based on size.
Folders containing more than 50% photo files are considered a
"photo folder" and are returned to the user.

Please note that the author gave a "skeleton" version of the code
for this project that I did not use.  There are many ways to skin
a cat I hear.
'''
import os
from pathlib import Path
from PIL import Image
from path_def import get_all_paths


def main():
    # get all of the image files
    img_file_types = ['.jpg', '.png']
    all_imgs = [path for path in get_all_paths('.') if path[-4:] in img_file_types]
    image_dict = {}

    for filename in all_imgs:
        # open the image file, get the name of the folder it is in
        img = Image.open(filename)
        width, height = img.size
        folder = Path(filename).parent

        # images larger than 500 are likely photos
        if (width and height) > 500:
            image_dict.setdefault(folder, []) # create a key for each folder
            image_dict[folder].append(Path(filename).name) # add filename to the list in the key
    
    # check the total size of image folders
    for directory in image_dict.keys():
        dir_path = os.path.abspath(directory)
        total_files = len(os.listdir(dir_path))
        photo_files = len(image_dict[directory])
        
        # if the folder contains more than 50%, alert the user
        if photo_files / total_files > 0.5:
            print(f'Photo folder found: {directory}')


main()
