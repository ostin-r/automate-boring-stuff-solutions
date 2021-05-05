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

def unsubscribe_all(email):
    '''
    unsubscribe_all takes an imaplib object that has
    been logged in and has a folder selected.  It 
    goes through the folder and finds any unsubscribe
    links and opens them in a webbrowser for easy
    access for the user.
    '''
    status, mail_data = email.search(None, 'ALL')
    
    for num in mail_data[0].split():
        status, data = email.fetch(num, '(RFC822)')
        #TODO figure out how to get the HTML and parse for unsubscribe

        #TODO add the link to a list, 

    #TODO open all of the links in the webbrowser


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

# RUN IT!
unsubscribe_all(email)
email.close()
email.logout()