'''
Austin Richards 3/26/21

cell_transpose.py transposes all columns in a sheet
'''
import os
import logging as log
import openpyxl as xl
from openpyxl.utils import get_column_letter

log.basicConfig(level=log.DEBUG, format='%(asctime)s : %(message)s')


def transpose_all(file):
    wb = xl.load_workbook(file)
    sheet = wb.active
    data = [[] for x in range(sheet.max_column)] # a list of lists to hold column data

    for col in range(1, sheet.max_column + 1):
        col_letter = get_column_letter(col)

        for row in range(1, sheet.max_row + 1):
            current_value = sheet[col_letter + str(row)].value
            sheet[col_letter + str(row)].value = '' # cut
            data[col - 1].append(current_value)     # paste

    # TODO: put all the data back, with rows and cols flipped


os.chdir('Chapter 13')
transpose_all('transpose-this.xlsx')