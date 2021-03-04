'''
Austin Richards 3/4/21

del-numbspace.py will look for leading zeros in filenames of
the format text009.py and rename the file without the zeros
'''
import os, re, shutil

def get_all_paths(directory, abs_path):

    file_paths = []

    if abs_path:
        directory = os.path.abspath(directory)

    for path, dirs, files in os.walk(directory):

        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)

    return file_paths

filepath = get_all_paths('Chapter 10', False)
zero_regex = re.compile(r'[a-zA-Z]+(0+)\d+.*')

for file in filepath:

    mo = zero_regex.search(file)

    if mo is not None:
        new_name = re.sub(mo.group(1), '', file)
        #shutil.move(file, new_name)
        print('Renaming ' + file + ' to ' + new_name + '...')
