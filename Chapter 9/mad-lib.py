'''
Austin Richards 2/25/21

mad-lib.py reads a .txt file with a blank madlib and creates a new text file
with the filled in version
'''
import re
import pyinputplus as pyip
from pathlib import Path

madLib_blank = open(Path.cwd() / 'Chapter 9' / 'mad-lib-blank.txt')
contents = madLib_blank.read()

keyword_regex = re.compile(r'''
    ADJECTIVE|
    NOUN|
    ADVERB|  # match adverb before verb to avoid replacing just the 'verb' in 'adverb'
    VERB|
    INTERJECTION
    ''', re.VERBOSE)

keywords = ['ADJECTIVE', 'ADVERB', 'VERB', 'NOUN', 'INTERJECTION']

for word in keyword_regex.findall(contents):
    statement  = 'Enter a ' + word.lower() + ': '
    user_input = pyip.inputStr(prompt=statement)
    contents   = re.sub(word, user_input, contents, count=1)

print(contents)
# TODO: after looping through all blank word types, write the newly filled contents to a new .txt file