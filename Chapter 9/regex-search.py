'''
Austin Richards 2/27/21

regex-search.py takes a user-supplied regular expression
and searches all .txt files in the current working directly,
then prints all matches to the user
'''
import re, os
from pathlib import Path

os.chdir('Chapter 9')

user_input = input('Enter a regex expression to search files in the current working directory:\n')
user_regex = re.compile(user_input)

for filePath in Path.cwd().glob('*.txt'):

    textFile = open(filePath).read()

    for match in user_regex.findall(textFile):
        print(match + ' in ' + filePath.name)