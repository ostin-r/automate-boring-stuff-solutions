'''
Austin Richards 4/3/21

pdf_paranoia.py contains encrypt_pdfs() to go through
every .PDF file in a folder and subfolders and encrypt them
and resave them with the original filename plus a suffix of
_encrypted.pdf. In addition, decrypt_pdfs does the opposite
and changes the suffix to _decrypted.pdf
'''
import os
import PyPDF2 as PyPDF
from PyPDF2.utils import PdfReadError
import logging as log
from pathlib import Path

log.basicConfig(level=log.DEBUG, format='%(asctime)s : %(message)s')


def get_all_paths(directory):
    '''
    returns strings of all of the file paths in the given directory
    I think this approach of filling a list is less clunky than using
    os.walk() within my function, encrypt_pdfs
    '''
    file_paths = []
    for path, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)
    return file_paths


def encrypt_pdfs(file_path, passcode):
    # get all the .pdf file paths
    file_path = os.path.abspath(file_path)
    print(f'Going through files in {file_path}')
    files = get_all_paths(file_path)
    files = [file for file in files if file.endswith('.pdf')] # only get pdf files

    for file in files:
        # initialize filename, pdf reader and writer, encrypt the writer
        file_name = Path(file).name
        pdf_file = open(file, 'rb')
        pdf_reader = PyPDF.PdfFileReader(pdf_file)
        pdf_writer = PyPDF.PdfFileWriter()
        pdf_writer.encrypt(passcode)

        # skip files that are already encrypted
        if pdf_reader.isEncrypted:
            print(f'{file_name} already encrypted')
            continue
        
        # write pages into the newly encrypted writer
        print(f'Encrypting {file_name}...')
        for page in range(pdf_reader.numPages):
            new_page = pdf_reader.getPage(page)
            pdf_writer.addPage(new_page)

        # create a new name and save to a new path
        encrypted_name = Path(file).stem + '_encrypted.pdf'
        new_filepath = os.path.join(Path(file).parent, encrypted_name)
        with open(new_filepath, 'wb') as encrypted_file:
            pdf_writer.write(encrypted_file)

        # check that the copy worked, delete the unencrypted file
        try:
            encrypted_reader = PyPDF.PdfFileReader(open(new_filepath, 'rb'))
            encrypted_reader.decrypt(passcode)
            test_page = encrypted_reader.getPage(0)
            pdf_file.close()
            os.unlink(file)
            print(f'{file_name} encrypted to {Path(new_filepath).name} successfully')
        except PdfReadError:
            print('Error: file not encrypted correctly')


def decrypt_pdfs(file_path, passcode):
    #TODO: get all the .pdf file paths in the path
    pass


encrypt_pdfs('Chapter 15', 'bananas')