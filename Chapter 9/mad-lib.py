'''
Austin Richards 2/25/21

mad-lib.py reads a .txt file with a blank madlib and creates a new text file
with the filled in version
'''
import re
import pyinputplus as pyip
from pathlib import Path

madLibBLank = open(Path.cwd() / 'Chapter 9' / 'mad-lib-blank.txt')

# TODO: get the contents of the blank mad lib

# TODO: use regex (loop) to identify the next word that needs to be replaced and update the contents

# TODO: after looping through all blank word types, write the newly filled contents to a new .txt file