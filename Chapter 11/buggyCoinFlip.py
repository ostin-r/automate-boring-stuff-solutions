import random

def string_to_flip(user_input):
    if user_input == 'heads':
        user_input = 1
    elif user_input == 'tails':
        user_input = 0
    return user_input

guess = ''
toss = random.randint(0, 1) # 0 is tails, 1 is heads

while guess not in (0, 1):
    print('Guess the coin toss! Enter heads or tails:')
    guess = string_to_flip(input())

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = string_to_flip(input())
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')