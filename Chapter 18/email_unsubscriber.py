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
log.disable(log.CRITICAL)


def unsubscribe_all(mail):
    '''
    unsubscribe_all takes an imaplib object that has
    been logged in and has a folder selected.  It 
    goes through the folder and finds any unsubscribe
    links and opens them in a webbrowser for easy
    access for the user.
    '''
    # get all of the email uids that contain the word unsubscribe
    result, data = mail.uid('search', None, 'TEXT unsubscribe')
    uids = data[0].split()

    for uid in uids:
        # get email, convert to string data, create email object
        result2, email_data = mail.uid('fetch', uid, '(RFC822)')
        raw_email = email_data[0][1].decode('utf-8')
        msg = email.message_from_string(raw_email)
        print(msg["From"])

        # get content type and parse if html
        for part in msg.walk():
            content_type = part.get_content_type()

            if 'html' in content_type:
                # get html from the email, create bs4 object
                html_ = part.get_payload()
                soup = bs4.BeautifulSoup(html_, 'html.parser')

                # parse the links, look for keyword unsubscribe
                for link in soup.find_all('a'):
                    if 'unsubscribe' in str(link.string).lower():
                        print(f'unsubscribe link found in {msg["From"]}, opening link...')
                        print(f'link: {link.get("href")}\n')
                        webbrowser.open(link.get('href'))


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