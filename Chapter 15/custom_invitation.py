'''
Austin Richards 4/5/21

custom_invitation.py creates personalied invitations and puts
them all on separate pages in a .docx file.  Invitations are
personalized by reading a .txt file of recipient names.
'''
import os
import docx


def custom_invitation(text_file):
    names_file = open(text_file, 'r')
    #names = names_file.readlines()
    names_file.close()

    names = ['Austin']

    for name in names:
        #TODO: write the invitation, with the name
        greeting = 'It would be a pleasure to have the company of\n'
        address = 'at 11010 Memory Lane on the evening of\n'
        date = 'April 1st\n'
        time = "at 7 o'clock"

        doc = docx.Document()

        add_greeting = doc.add_paragraph(greeting)
        add_address = doc.add_paragraph(address)
        add_date = doc.add_paragraph(date, )
        add_time = doc.add_paragraph(time, 'Quote')
        add_time.alignment = 1

        doc.save('invitations.docx')


os.chdir('Chapter 15')
custom_invitation('name_list.txt')