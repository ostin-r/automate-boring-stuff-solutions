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
import pyinputplus as pyip

def unsubscribe_all(mailbox='INBOX'):
    #TODO: for each mail in the INBOX, search for "unsubscribe" - add link to list of links

    #TODO: for each link in the list, open it in the webbrowser
    pass


# login info
user = open('email_creds.txt').read()
password = pyip.inputPassword('Input Password: ')
folder = 'INBOX'

# login to imap server, select folder
email = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    box = email.login(user, password)
    print('login successful')
except imaplib.IMAP4.error:
    print('login failed')
email.select(folder)