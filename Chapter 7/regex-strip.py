'''
Austin Richards 2/18/21
An exercise in using regular expressions by implementing my own
version of the .strip() method for strings
'''
import re

def re_strip(text, delete_character=' '):

    pre_re = re.compile('^[{}]+'.format(delete_character))
    end_re = re.compile('[{}]+$'.format(delete_character))

    pre_text = pre_re.search(text)
    end_text = end_re.search(text)

    if pre_text is not None:
        cut_pre = len(pre_text.group())
        text = text[cut_pre:]
    
    if end_text is not None:
        cut_end = len(end_text.group())
        text = text[:(len(text) - cut_end)]

    return text

text = 'bananas_austin_abasabn'
text = re_strip(text, delete_character='bananas')
print(text)