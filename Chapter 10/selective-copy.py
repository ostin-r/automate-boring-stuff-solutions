'''
Austin Richards 3/2/21

selective_copy.py contains the function select_copy
which will walk through a directory and selectively copy
files with a certain extension.
'''
import re, os, shutil

def get_all_paths(directory):

    file_paths = []

    for path, dirs, files in os.walk(directory):

        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)

    return file_paths


def select_copy(source, dest, ext):

    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    
    ext_regex = re.compile('\.{}$'.format(ext))
    file_paths = get_all_paths(source)

    for file in file_paths:
        if ext_regex.search(file) is not None:
            source = os.path.join(source, file)
            shutil.copy(source, dest)


select_copy('Chapter 9', '.', 'py')
# copies all .py files in Chapter 8 to project_copies folder