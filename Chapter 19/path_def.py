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
