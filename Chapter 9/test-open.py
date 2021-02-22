'''
Austin Richards 2/22/21

testing basic reading/writing of text files
'''
from pathlib import Path

hello_file = open(Path.home() / 'hello.txt') # returns a File object that can be used to read/write