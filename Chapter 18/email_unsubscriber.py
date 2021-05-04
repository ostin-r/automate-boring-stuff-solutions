'''
Austin Richards 5/4/21

email_unsubscriber parses through the IMAP server of
a mailbox and searches for "unsubscribe" links in emails.
If found, it opens all of the links in a webbrowser-
allowing the user to click through and unsubscribe on 
all of them.
'''
import bs4, imapclient, webbrowser

#TODO: set up and log in to IMAP server

#TODO: for each mail in the INBOX, search for "unsubscribe" - add link to list of links

#TODO: for each link in the list, open it in the webbrowser