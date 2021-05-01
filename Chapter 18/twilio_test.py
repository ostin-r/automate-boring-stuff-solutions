'''
Austin Richards 4/29/21

A program to test twilio out!
'''
import os
from pathlib import Path
from twilio.rest import Client


def text_me(send_string):
    '''
    sends a text to my cell.  Must use double quotes for input,
    otherwise twilio just won't send the text and won't throw 
    any exceptions.
    '''
    # get credentials and cell numbers
    sid, auth_token, twilio_num, my_cell = open('twilio-creds.txt').read().splitlines()

    # send message
    client = Client(sid, auth_token)
    message = client.messages \
                    .create(
                        body=send_string,
                        from_=twilio_num,
                        to=my_cell
                    )


#text_me("Hello!!!")