'''
Austin Richards 4/8/21

pdf_brute_force.py uses a brute force attack to attempt to 
decrypt a pdf that has presumably been encrypted with a
single english word
'''
import os, PyPDF2

def pdf_decrypt(pdf):
    words = open('dictionary.txt').readlines()
    upper_words = [word[:len(word)-1] for word in words]
    lower_words = [word[:len(word)-1].lower() for word in words]
    words = upper_words + lower_words

    pdf_file = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for word in words:
        if pdf_reader.decrypt(word):
            print('File decrypted!')
            print(f'Password: {word}')
            break

    if not pdf_reader.decrypt(word): print('Unable to break passcode.')

    
os.chdir('Chapter 15')
pdf_decrypt('watermark.pdf')