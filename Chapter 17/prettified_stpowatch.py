'''
Austin Richards 4/20/21

prettified_stopwatch.py is an extension of the follow-along
project from chapter 17.  This version does the same thing
except it also prints the data in a pretty way (just by
justifying the text) and copies it to the clipboard so the
data could be placed in an email or text file.
'''
import time
import pyperclip
import logging as log

print('Press ENTER to begin, afterward, press ENTER to click the stopwatch.  Press Ctrl-C to quit')
input()
print('Started')

start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        '''
        TODO: print lap number, total time, and lap time as seperate values? use str.ljust() and str.rjust()
        print_string = f'Lap # {lap_num}: {total_time} ({lap_time})'
        print(print_string, end='')
        '''
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone.')