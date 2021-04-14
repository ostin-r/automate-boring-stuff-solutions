'''
Austin Richards 4/14/21

excel_to_csv.py automates the conversion of many xlsx
files into csv files.  This program names the csv file
in the format <filename>_<sheetname>.csv
'''
import logging
import os, csv, openpyxl

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
    all_paths = [path for path in get_all_paths(directory) if path.endswith('.xlsx')]
    os.makedirs(f'csvFiles_{os.path.basename(directory)}', exist_ok=True)
    #TODO put the new directory in the directory being edited, save the name of the new directory
    # so that it can be referenced later when adding files
    
    for excel_file in all_paths:
        workbook = openpyxl.load_workbook(excel_file)

        for sheet_name in workbook.get_sheet_names():
            sheet = workbook.get_sheet_by_name(sheet_name)

            #TODO create the csv file based on the name of the file

            #TODO loop through every row in the xlsx file and copy it to the csv

        #TODO: close the new csv file

xl_to_csv('Chapter 16')