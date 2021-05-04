'''
Austin Richards 5/2/21

random_chore.py takes a list of emails (roommates, presumably) and sends
them a randomly assigned chore for the week.  This program also avoids
repeating any chores that the person did the last week.
'''
import random
import pprint
import ezgmail as gmail
import chore_record

# initialize gmail
gmail.init()

# chores, emails, and previous week's chores done
chores = ['Dishes', 'Vacuum', 'Bathroom', 'Walk Dog']
emails = {'Austin':'austin@outlook.com', 'Also Austin':'austin2@gmail.com'}
print(chore_record.prev_chore)

for name, email in emails.items():
    # assign chore, check they didn't do it last week, and update the list of what they did
    while True:
        rand_chore = random.choice(chores)
        if rand_chore != chore_record.prev_chore[name]:
            chore_record.prev_chore[name] = rand_chore
            chores.remove(rand_chore)
            break

    # send an email letting them know which chore to do this week
    subject = 'Weekly Chores!'
    body = f'Dear {name},\nYou have been assigned to the following chore this week: {rand_chore}\n\nCheers!'
    print(f'Sending email to {name}. Chore: {rand_chore}')
    #gmail.send(email, subject, body)

# write changes to chore record
data = pprint.pformat(chore_record.prev_chore)
print(data)
file = open('chore_record.py', 'w')
file.write(f'prev_chore ={data}\n')
file.close()