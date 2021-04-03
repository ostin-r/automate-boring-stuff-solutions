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
    file_path = os.path.abspath(file_path)
    print(f'Going through files in {file_path}')
    files = get_all_paths(file_path)
    files = [file for file in files if file.endswith('.pdf')] # only get pdf files

    for file in files:
        file_name = Path(file).name
        pdf_file = open(file, 'rb')
        pdf_reader = PyPDF.PdfFileReader(pdf_file)
        pdf_writer = PyPDF.PdfFileWriter()
        pdf_writer.encrypt(passcode)

        if pdf_reader.isEncrypted:
            print(f'{file_name} already encrypted')
            continue
        
        print(f'Encrypting {file_name}...')
        for page in range(pdf_reader.numPages):
            new_page = pdf_reader.getPage(page)
            pdf_writer.addPage(new_page)

        encrypted_name = Path(file).stem + '_encrypted.pdf'
        new_filepath = os.path.join(Path(file).parent, encrypted_name)
        with open(new_filepath, 'wb') as encrypted_file:
            pdf_writer.write(encrypted_file)
        print(f'Successfully encrypted {file_name}\n')

        #TODO: close the new file

        #TODO: attempt to decrypt and read the new file to check that it worked

        #TODO: delete the previous file if the above worked


encrypt_pdfs('Chapter 15', 'bananas')