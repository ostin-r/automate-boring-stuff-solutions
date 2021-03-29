'''
Austin Richards 3/29/21

sheets_convert.py converts different spreadsheet
files by uploading them to google sheets and then
downloading them in the correct form
'''
import os
import logging as log
import ezsheets as sheets
from pathlib import Path as path

log.basicConfig(level=log.DEBUG, format='%(asctime)s : %(message)s')


def convert_sheet(file, file_type):
    #TODO: upload the file to google sheets

    #TODO: download the file in the desired form

    #TODO: delete the file

    return


os.chdir('Chapter 13')
convert_sheet('files1&2.xlsx', 'xlsx')