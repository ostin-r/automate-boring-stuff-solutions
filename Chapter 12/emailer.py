'''
This is a follow along project on sending emails with 
python found on realpython.com/python-send-email
'''
import smtplib, ssl
import pyinputplus as pyip

port = 465
user_email = 'austin.pythonmagic@gmail.com'
password = pyip.inputPassword('Enter your password: ')
reciever_email = pyip.inputEmail('Enter your recipient\'s email: ')
message = pyip.inputStr('Enter the message: ')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(user_email, password)
    server.sendmail(user_email, reciever_email, message)