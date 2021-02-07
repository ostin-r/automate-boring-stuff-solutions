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
    
    for i in range(100):
        # read the current value
        # store current value, current_value
        # compare to previous value (skip this for first value, maybe using range())
        # if the previous value is the same, add 1 to current_streak
        # if current_streak is 5, add the streak to streak_count (but only once?)
        # if current streak is > 5, do nothing.  The streak doesn't need to be counted again
        # if the previous value is different, do nothing
        # basically only one if statement is needed (when streak count == 5)

