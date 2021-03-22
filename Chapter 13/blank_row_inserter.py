'''
blank_row_inserter.py takes an excel file and
inserts 'm' blank rows at row 'n' (inbetween n and n+1)
'''
import os, re
import openpyxl as xl
from openpyxl.utils import get_column_letter, column_index_from_string
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def insert_blanks(file, n, m):

    wb = xl.load_workbook(file)
    sheet = wb.active

    # copy all data down +m rows
    print('copying data...')
    for row in range(sheet.max_row, 1, -1): # decrement from bottom row (no data loss)
       if row > n:
            for col in range(1, sheet.max_column + 1):
                letter = get_column_letter(col)
                loc = letter + str(row)
                val = sheet[loc].value
                
                new_loc = letter + str(row + m)
                sheet[new_loc].value = val

                log.debug(f'Copying {val} from {loc} to {new_loc}')
    
    print('inserting blank rows...')
    for row in range(n + 1, n + m + 1):
        for col in range(1, sheet.max_column + 1):
            letter = get_column_letter(col)
            loc = letter + str(row)
            sheet[loc].value = ''
            log.debug(f'blank value at {loc}')

    wb.save('insertBlanksExample.xlsx')

def move_excel_function(value, m):
    '''
    moves a function excel and maintains relative reference for rows only
    '''
    # TODO: match a location using regex ex. 'A1' 'B32', do the following:
    # get the location of that location in the string (only need the row value)
    # if a $ preceeds the row don't change it
    # increase row by m
    return


os.chdir('Chapter 13')
insert_blanks('writeFormula.xlsx', 1, 2)