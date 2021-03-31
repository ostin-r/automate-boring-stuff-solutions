'''
Ch. 15 follow-along project for selectively merging
multiple .PDF files
'''
import os
import PyPDF2 as PyPDF

os.chdir('follow-along/Chapters 10-20')
files = []
for filename in os.listdir():
    if filename.endswith('.pdf'):
        files.append(filename)
files.sort(key = str.lower)

writer = PyPDF.PdfFileWriter()

for filename in files:
    file_obj = open(filename, 'rb')
    reader = PyPDF.PdfFileReader(file_obj)

    for page in range(1, reader.numPages):
        page_obj = reader.getPage(page)
        writer.addPage(page_obj)

pdf_output = open('allminutes.pdf', 'wb')
writer.write(pdf_output)
pdf_output.close()