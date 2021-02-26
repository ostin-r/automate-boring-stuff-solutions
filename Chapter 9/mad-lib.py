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
print(blank_contents)

# TODO: use regex (loop) to identify the next word that needs to be replaced and update the contents
'''
create a list, (or string?) with the types of speech we want to search for
put that list into a regex 
loop through all items in re.findall()
    if item == 'ADJECTIVE'
        prompt user to enter an adjective
        replace in new string with re.sub()
    elif item == 'VERB':
        prompt user to enter a verb
        replace in new string using re.sub()
'''
keyword_regex = re.compile(r'''
    ADJECTIVE|
    VERB|
    ADVERB|
    PRONOUN|
    INTERJECTION|
    NOUN|
    ''', re.VERBOSE)

mo = keyword_regex.search(blank_contents)
try:
    print(mo.group())
except:
    print('no match')

# TODO: after looping through all blank word types, write the newly filled contents to a new .txt file