'''
Austin Richards 2/18/21
An exercise in using regular expressions by implementing my own
version of the .strip() method for strings

The strip() method returns a copy of the string by removing both the leading
and trailing characters.
'''
import re

def re_strip(text, delete_character='a'):

    # TODO: go deeper into the types of strings that can be passed to regex

    pre_re = re.compile('^{}+'.format(delete_character))
    end_re = re.compile('{}+$'.format(delete_character))

    pre_text = pre_re.search(text)
    end_text = end_re.search(text)

    cut_pre = len(pre_text.group())
    cut_end = len(end_text.group())

    

    


re_strip('aaa AVOCADO aaa')