'''
blank_row_inserter.py takes an excel file and
inserts 'm' blank rows at row 'n' (inbetween n and n+1)
'''
import os
import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def insert_blanks(file, n, m):

    wb = xl.load_workbook(file)
    sheet = wb.active

    # copy all data down 'm' rows
    print('copying data...')
    for row in range(1, sheet.max_row):
        if row > n:
            for col in range(0, sheet.max_column):
                # TODO: copy values down to n+m+1
    
    # TODO: insert blank lines at range(n, n+m+1)

os.chdir('Chapter 13')

insert_blanks('writeFormula.xlsx', 1, 4)

# TODO: Idea: maybe loop from bottom to top in order to preserve data better?