'''
Austin Richards 2/16/21

date-detection.py recognizes dates in the dd/mm/yyyy format
'''
import re, pyperclip

text = pyperclip.paste()

date_regex = re.compile(r'''
    (\d{2})
    /
    (\d{2})
    /
    (\d{4})
    ''', re.VERBOSE)

days = []
months = []
years = []

for date in date_regex.findall(text):
    days.append(date[0])
    months.append(date[1])
    years.append(date[2])

# TODO: check if dates are valid