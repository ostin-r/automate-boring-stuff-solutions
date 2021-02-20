'''
Austin Richards 2/18/21
An exercise in using regular expressions by implementing my own
version of the .strip() method for strings

The strip() method returns a copy of the string by removing both the leading
and trailing characters.
'''
import re

def re_strip(text, delete_character=' '):

    # TODO: go deeper into the types of strings that can be passed to regex

    pre_re = re.compile('^{}+'.format(delete_character))
    end_re = re.compile('{}+$'.format(delete_character))

    pre_text = pre_re.search(text)
    end_text = end_re.search(text)

    if pre_text is not None:
        cut_pre = len(pre_text.group())
        text = text[cut_pre:]
    
    if end_text is not None:
        cut_end = len(end_text.group())
        text = text[:(len(text) - cut_end)]

    return text

text = '---austin-----------'
text = re_strip(text, delete_character='-')
print(text)