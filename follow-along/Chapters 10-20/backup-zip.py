'''
backup-zip.py is a follow along project in ch. 10 that 
contains the function backup_zip() which will copy a file, 
zip it, and then increment the name
'''
import zipfile, os
from pathlib import Path as path


def backup_zip(folder):

    folder = os.path.abspath(folder) # sets the folder to absolute path

    # make the zip filename if it doesn't already exist.  If it does, increment.
    i = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(i) + '.zip' # creates an incremented filename
        if not os.path.exists(zip_filename): # if it doesn't exist, break and make it. Else, increment
            break
        i += 1

    print('creating {}...'.format(zip_filename))
    backupZip = zipfile.ZipFile(zip_filename, 'w') # create a zipfile object with name folder_x.zip

    # zip each file and write them to backupZip (zipfile object)
    for foldername, subfolders, filenames in os.walk(folder):

        print('adding files in {}'.format(str(foldername)))
        backupZip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'

            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue

            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done')

backup_zip('Chapter 9')