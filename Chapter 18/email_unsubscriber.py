'''
Austin Richards 5/4/21

email_unsubscriber parses through the IMAP server of
a mailbox and searches for "unsubscribe" links in emails.
If found, it opens all of the links in a webbrowser-
allowing the user to click through and unsubscribe on 
all of them.
'''
import bs4
import imaplib
import webbrowser
import email
import pyinputplus as pyip
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def unsubscribe_all(mail):
    '''
    unsubscribe_all takes an imaplib object that has
    been logged in and has a folder selected.  It 
    goes through the folder and finds any unsubscribe
    links and opens them in a webbrowser for easy
    access for the user.
    '''
    result, data = mail.uid('search', None, 'ALL')
    mail_items = data[0].split()
    
    test_mail = mail_items[0]
    result2, email_data = mail.uid('fetch', test_mail, '(RFC822)')

    raw_email = email_data[0][1].decode('utf-8')
    full_email = email.message_from_string(raw_email)

    #TODO open all of the links in the webbrowser


# login info
user = open('email_creds.txt').read()
password = pyip.inputPassword('Input Password: ')
folder = 'INBOX'

# login to imap server, select folder
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user, password)
mail.select(folder)

# RUN IT!
unsubscribe_all(mail)
mail.close()
mail.logout()