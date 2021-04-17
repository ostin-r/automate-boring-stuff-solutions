'''
introduction to multi-threading with python
'''
import threading, time


def take_a_nap():
    time.sleep(5)
    print('wake up!')


print('start of program')
thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()
print('end of program')