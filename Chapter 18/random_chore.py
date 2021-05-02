'''
Austin Richards 5/2/21

random_chore.py takes a list of emails (roommates, presumably) and sends
them a randomly assigned chore for the week.  This program also avoids
repeating any chores that the person did the last week.
'''
import random
import ezgmail as gmail

# initialize gmail
gmail.init()

# chores, emails, and previous week's chores done
chores = ['Dishes', 'Vacuum', 'Bathroom', 'Walk Dog']
emails = {'Austin':'austinjrichards@outlook.com', 'Also Austin':'austin.pythonmagic@gmail.com'}
prev_chore = {'Austin':'Vacuum', 'Also Austin':'Walk Dog'}

for name, email in emails.items():
    # assign chore, check they didn't do it last week, and update the list of what they did
    while True:
        rand_chore = random.choice(chores)
        if rand_chore != prev_chore[name]:
            prev_chore[name] = rand_chore
            chores.remove(rand_chore)
            break

    # send an email letting them know which chore to do this week
    subject = 'Weekly Chores!'
    body = f'Dear {name},\nYou have been assigned to the following chore this week: {rand_chore}\n\nCheers!'
    gmail.send(email, subject, body)