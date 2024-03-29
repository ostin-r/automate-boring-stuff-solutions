'''
A twilio test program.
'''
from twilio.rest import Client


def send_text(send_string):
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