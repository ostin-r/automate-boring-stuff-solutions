'''
Austin Richards 2/18/21
password_strength() checks a password for at least 8 characters,
one number, one upper case character, and one lower case character
'''
import re

def password_strength(password):

    num_regex   = re.compile(r'\d')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')

    if len(password) < 8:
        return 'weak, password too short'    

    if num_regex.search(password) is None:
        return 'weak, no numbers'

    if upper_regex.search(password) is None:
        return 'weak, no upper case characters'

    if lower_regex.search(password) is None:
        return 'weak, no lower case characters'

    return 'strong'

strength = password_strength('insert_password_here')