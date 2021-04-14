'''
Austin Richards 4/14/21

excel_to_csv.py automates the conversion of many xlsx
files into csv files.  This program names the csv file
in the format <filename>_<sheetname>.csv
'''
import logging
import os, csv, openpyxl
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')

def get_all_paths(directory):
    file_paths = []
    for path, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)
    return file_paths

def xl_to_csv(directory):
    directory = os.path.abspath(directory)
    new_dir = os.path.join(directory, 'converted_csv_files')
    os.makedirs(new_dir, exist_ok=True)
    all_paths = [path for path in get_all_paths(directory) if path.endswith('.xlsx')]
    
    for excel_file in all_paths:
        workbook = openpyxl.load_workbook(excel_file)
        excel_filename = Path(excel_file).stem

        for sheet_name in workbook.sheetnames:
            csv_filename = f'{excel_filename}_{sheet_name}.csv'
            csv_file = os.path.join(new_dir, csv_filename)
            logging.debug(csv_file)

            #TODO loop through every row in the xlsx file and copy it to the csv
            sheet = workbook[sheet_name]

        #TODO: close the new csv file


xl_to_csv('Chapter 16')