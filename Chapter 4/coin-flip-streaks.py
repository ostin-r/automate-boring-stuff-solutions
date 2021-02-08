'''
Austin Richards 2/7/21

My solution to ch. 4 "coin flip streaks" problem.  This program
will count the amount of streaks of either heads or tails >= 6
in a list of 100 randomly generated "coin flips".

This code will then be repeated 10,000 times to get a better idea
of how often these streaks occur in a random set.
'''
import random

streak_count = 0

for experimentNumber in range(100):

    flip_list = []

    for i in range(100):

        coin_flip = random.randint(0,1)

        if coin_flip == 0:
            flip_list.append('T')

        else:
            flip_list.append('H')
    
    current_streak = 0

    for i in range(1, 100):
        current_value = flip_list[i]
        previous_value = flip_list[i-1]

        if previous_value == current_value:
            current_streak += 1

            if current_streak == 5:
                streak_count += 1

        else:
            current_streak = 0

