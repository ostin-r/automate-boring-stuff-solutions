'''
backup-zip.alternate is a follow along example from geekstogeeks
to help me understanding using os.walk() and writing to zip files
'''
import os, zipfile

def get_all_paths(directory):

    file_paths = []

    for path, dirs, files in os.walk(directory):

        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)

    return file_paths


def backup_zip(directory):

    file_paths = get_all_paths(directory)

    i = 1
    while True:
        zip_name = os.path.basename(directory) + '-backup-' + str(i) + '.zip'
        if not os.path.exists(zip_name):
            break
        i += 1

    print('The following files will be zipped:')
    for file in file_paths:
        print(file)

    with zipfile.ZipFile(zip_name, 'w') as new_zip:
        for file in file_paths:
            new_zip.write(file)


directory = './follow-along/Chapters 3-9'
backup_zip(directory)