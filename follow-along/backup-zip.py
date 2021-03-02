'''
backup-zip.py is a follow along project in ch. 10 that 
contains the function backup_zip() which will copy a file, 
zip it, and then increment the name
'''
import zipfile, os
import pathlib as path


def backup_zip(folder):

    folder = os.path.abspath(folder)

    i = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(i) + '.zip'

        if os.path.exists(zip_filename):
            print('file already exists')
            break

        i += 1

        print('creating {}...'.format(zip_filename))
        #backupZip = zipfile.ZipFile(zip_filename, 'w')

        for foldername, subfolder, filename in os.walk(folder):
            print(filename.basename + '\n')

backup_zip(path.Path.cwd() / 'follow-along')