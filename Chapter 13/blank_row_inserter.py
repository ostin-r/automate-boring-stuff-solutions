'''
blank_row_inserter.py takes an excel file and
inserts 'm' blank rows at row 'n'
'''
import os
import openpyxl as xl
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def insert_blanks(file, n, m):

    wb = xl.load_workbook(file)
    sheet = wb.active

    for row in range(1, sheet.max_row):
        # TODO: insert blanks at n up to n+m (if row > n and row < n + m)
        # TODO: don't loose the data though, need to copy that over
        # TODO: figure out how to copy an entire row (can it be done without looping?)
        pass

    return

os.chdir('Chapter 13')

insert_blanks('produceSales.xlsx', 3, 4)

# TODO: Idea: maybe loop from bottom to top in order to preserve data better?