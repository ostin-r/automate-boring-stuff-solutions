'''
command line version of the follow along emailing 
project on realpython.com !
'''
import ssl, smtplib, sys

user_email = 'austin.pythonmagic@gmail.com'

try:
    password = sys.argv[1]
    reciever_email = sys.argv[2]
    message = ' '.join(sys.argv[3:])
except:
    print('Invalid Input')

port = 465
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(user_email, password)
    server.sendmail(user_email, reciever_email, message)