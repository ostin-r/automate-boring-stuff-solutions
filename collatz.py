'''
Austin Richards 2.3.21 20:08
This function is one of the practice problems defined in chapter 2 of 
'automate the boring stuff with python' called the collatz problem.

The collatz sequence eventually converges to 1, which mathemeticians haven't 
figured out why.  Pretty neat.
'''
import time

def collatz(number):
    if number % 2 == 0:
        ans = number // 2
        print(ans)
        return ans

    else:
        ans = (number * 3) + 1 
        print(ans)
        return ans

try:
    number = int(input('Enter any number: '))

    while number != 1:
        number = collatz(number)
        time.sleep(0.3)

except:
    print('Error: please enter an integer')