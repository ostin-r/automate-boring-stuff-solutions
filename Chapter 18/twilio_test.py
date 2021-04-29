'''
Austin Richards 4/29/21

A program to test twilio out!
'''
import os
from twilio.rest import Client
import logging as log

os.chdir('Chapter 18')
log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')

# get credentials and cell numbers
sid, auth_token, twilio_num, my_cell = open('twilio-creds.txt').read().splitlines()


# send a message
twi_client = Client(sid, auth_token)
message = twi_client.messages.create(body='Hello!', from_=twilio_num, to=my_cell)