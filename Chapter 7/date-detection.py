'''
Austin Richards 2/16/21

date-detection.py recognizes dates in the dd/mm/yyyy format
'''
import re, pyperclip, copy

def isLeapYear(year):
    leap_year = False

    if year % 4 == 0:
        leap_year = True

        if year % 100 == 0 and year % 400 != 0:
            leap_year = False

    return leap_year

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

months_30 = [4, 6, 9, 11]
months_31 = [1, 3, 5, 7, 8, 10, 12]

for i in range(len(months)):
    if int(months[i]) > 12:
        years[i], months[i], days[i] = [0, 0, 0]

    else:
        if int(months[i]) in months_30:
            if int(days[i]) > 30:
                years[i], months[i], days[i] = [0, 0, 0]

        elif int(months[i]) in months_31:
            if int(days[i]) > 31:
                years[i], months[i], days[i] = [0, 0, 0]

        else:
            pass

for i in range(len(years)):
    if int(years[i]) < 1000 or int(years[i]) > 2999:
        years[i], months[i], days[i] = [0, 0, 0]


print(isLeapYear(1600))
