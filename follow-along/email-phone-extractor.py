'''
Austin Richards 2/15/21
'''
import re, pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for group in phone_regex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])

    if group[8] != '':
        phoneNum += ' x' + group[8]

    matches.append(phoneNum)

for group in email_regex.findall(text):
    matches.append(group)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Data copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found.')