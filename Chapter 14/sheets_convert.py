'''
Austin Richards 3/29/21

sheets_convert.py converts different spreadsheet
files by uploading them to google sheets and then
downloading them in the specified form.  Default is xlsx.
Valid file conversions are .xlsx, .csv, and .pdf
'''
import os
import logging as log
import ezsheets as sheets
from pathlib import Path as path

log.basicConfig(level=log.DEBUG, format='%(asctime)s : %(message)s')


def convert_sheet(file, file_type=None):
    google_file = sheets.upload(file)

    if file_type is None or file_type == 'xlsx':
        google_file.downloadAsExcel()
    elif file_type == 'csv':
        google_file.downloadAsCSV()
    elif file_type == 'pdf':
        google_file.downloadAsPDF()

    google_file.delete()


os.chdir('Chapter 14')
convert_sheet('files1&2.xlsx', 'pdf')