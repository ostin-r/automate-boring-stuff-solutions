'''
Austin Richards 3/30/21

find_mistakes.py parses through the public spreadsheet 
provided by Al, and determines which lines contain an error.
'''
import os
import logging as log
import ezsheets

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss.sheets[0]
max_row = 15000
incorrect_rows = []

for row in range(2, max_row + 1):
    data = sheet.getRow(row)
    data = [int(x) for x in data[:3]]
    beans_per_jar, jars, total = data[:3]

    if beans_per_jar * jars != total:
        incorrect_rows.append(row)

print(incorrect_rows)