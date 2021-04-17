'''
Follow along project that functions
as a stopwatch from chapter 17 of ATBS
'''
import time

print('Press ENTER to begin, afterward, press enter to click the stopwatch.  Press Ctrl-C to quit')
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
        print(f'Lap {lap_num}: {total_time} ({lap_time})', end='')
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone.')