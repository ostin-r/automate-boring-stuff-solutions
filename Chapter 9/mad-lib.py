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
    ADVERB|
    \ VERB|
    PRONOUN|
    \ NOUN
    INTERJECTION|
    ''', re.VERBOSE)

for word in keyword_regex.findall(contents):
    
    if word == 'ADJECTIVE':
        user_input = pyip.inputStr(prompt='Enter an adjective: ')
        contents = re.sub('ADJECTIVE', user_input, contents, count=1)

    elif word == 'VERB':
        user_input = pyip.inputStr(prompt='Enter a verb: ')
        contents = re.sub('VERB', user_input, contents, count=1)

    elif word == 'ADVERB':
        user_input = pyip.inputStr(prompt='Enter an adverb: ')
        contents = re.sub('ADVERB', user_input, contents, count=1)   

    elif word == 'NOUN':
        user_input = pyip.inputStr(prompt='Enter a noun: ')
        contents = re.sub('VERB', user_input, contents, count=1)

    elif word == 'PRONOUN':
        user_input = pyip.inputStr(prompt='Enter a pronoun: ')
        contents = re.sub('PRONOUN', user_input, contents, count=1)

    elif word == 'INTERJECTION':
        user_input = pyip.inputStr(prompt='Enter an interjection: ')
        contents = re.sub('INTERJECTION', user_input, contents, count=1)

print(contents)
# TODO: after looping through all blank word types, write the newly filled contents to a new .txt file