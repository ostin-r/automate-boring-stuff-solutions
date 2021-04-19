'''
Follow-along project from Ch. 17 of ATBS by Al Sweigart

simple_countdown.py is a program that counts down from a
specified amount of time and plays a sound when the count-
down is 0
'''
import os
import time
import subprocess


def countdown(time_left):
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left -= 1

    subprocess.Popen(['start', 'alarm.wav'], shell=True)

os.chdir('follow-along/Chapters 10-20')
countdown(10)