'''
Austin Richards 4/3/21

pdf_paranoia.py uses the os.walk() function to go through
every .PDF file in a folder and subfolders and encrypt them
and resave them with the original filename plus a suffix of
_encrypted.pdf
'''
import os
import PyPDF2 as PyPDF
from pathlib import Path


def get_all_paths(directory):

    file_paths = []
    for path, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)

    return file_paths


def encrypt_pdfs(file_path, passcode):
    #TODO: for pdf files in os.walk(), do the following:

        #TODO: create an object: open the file in read binary

        #TODO: create a pdf reader object by reading the above object

        #TODO: create a writer object

        #TODO: copy the file by adding the pages in reader to writer

        #TODO: encrypt the writer with the passcode

        #TODO: open a new filename in write binary, write the writer object

        #TODO: close the new file

        #TODO: attempt to decrypt and read the new file to check that it worked

        #TODO: delete the previous file if the above worked
    pass
