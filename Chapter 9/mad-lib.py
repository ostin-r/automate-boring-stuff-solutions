'''
Austin Richards 2/25/21

mad-lib.py reads a .txt file with a blank madlib and creates a new text file
with the filled in version
'''
import re
import pyinputplus as pyip
from pathlib import Path

madLib_blank = open(Path.cwd() / 'Chapter 9' / 'mad-lib-blank.txt')
blank_contents = madLib_blank.read()

# TODO: use regex (loop) to identify the next word that needs to be replaced and update the contents
'''
create a list, (or string?) with the types of speech we want to search for
put that list into a regex 
loop through all items in re.findall()
    if item == 'ADJECTIVE'
        prompt user to enter an adjective
        replace that item in the updated text with re.sub()
    elif item == 'VERB':
        prompt user to enter a verb
        replace that item in the updated text re.sub()
        ...
    
'''

# TODO: after looping through all blank word types, write the newly filled contents to a new .txt file