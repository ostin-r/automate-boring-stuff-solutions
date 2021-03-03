'''
Austin Richards 3/2/21

selective_copy.py contains the function select_copy
which will walk through a directory and selectively copy
files with a certain extension.
'''
import re, os, shutil

def select_copy(source, dest, ext):

    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    
    ext_regex = re.compile('\.{}$'.format(ext))

    # TODO: walk through the specified source path and copy any files that match into destination
    for path, dirs, files in os.walk(source):
        
        for file in files:

            if ext_regex.search(file) is not None:
                new_source = os.path.join(path, file)
                shutil.copy(new_source, dest)

select_copy('Chapter 8', 'project_copies', 'py')
# copies all .py files in Chapter 8 to project_copies folder