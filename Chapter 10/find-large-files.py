'''
Austin Richards 3/3/21

find-large-files.py will walk through a directory and
print files larger than the specified amount to the user
(default 100 MB)
'''
import os

def get_large_files(directory, size):

    file_paths = []

    for path, dirs, files in os.walk(directory):

        for filename in files:
            
            full_path = os.path.join(path, filename)
            
            if os.path.getsize(full_path) > size:
                filepath = os.path.join(path, filename)
                file_paths.append(filepath)

    return file_paths

large_files = get_large_files('.', 4e3)
for file in large_files:
    print(file)