'''
Austin Richards 2/7/21

My solution to ch. 4 "coin flip streaks" problem.  This program
will count the amount of streaks of either heads or tails >= 6
in a list of 100 randomly generated "coin flips".

This code will then be repeated 10,000 times to get a better idea
of how often these streaks occur in a random set.
'''
import random

numberOfStreaks = 0

for experimentNumber in range(100):

    flip_list = []

    for i in range(100):

        coin_flip = random.randint(0,1)

        if coin_flip == 0:
            flip_list.append('T')

        else:
            flip_list.append('H')
    
    
