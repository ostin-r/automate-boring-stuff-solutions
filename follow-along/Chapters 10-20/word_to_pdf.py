'''
Follow-along project from chapter 15 of ATBS
that converts word documents to pdf documents
'''
import os
import docx
import win32com.client
import logging as log

log.basicConfig(level=log.DEBUG, format='%(message)s')
os.chdir('follow-along/Chapters 10-20')

word_file = os.path.abspath('helloworld.docx')
pdf_file = os.path.abspath('helloworld.pdf')
word_obj = win32com.client.Dispatch('Word.Application')

doc_obj = word_obj.Documents.Open(word_file)
doc_obj.SaveAs(pdf_file, FileFormat=17)