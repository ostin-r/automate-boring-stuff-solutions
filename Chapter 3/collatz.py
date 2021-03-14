'''
Austin Richards 2.3.21 20:08
This function is one of the practice problems defined in chapter 2 of 
'automate the boring stuff with python' called the collatz problem.

The collatz sequence eventually converges to 1, which mathemeticians haven't 
figured out why.  Pretty neat.
'''
import time

def collatz(number):
    if number <= 0:
        raise Exception("Number must be a positive integer")

    elif type(number) != int:
        raise Exception("Number must be an integer")

    elif number % 2 == 0:
        ans = number // 2
        return ans

    else:
        ans = (number * 3) + 1
        return ans


while True:
    number = input('Enter a positive integer, or type q to quit: ')

    if number == 'q':
        print('Program closed')
        break

    try:
        number = int(number)
        while number != 1:
            number = collatz(number)
            print(number)
            time.sleep(0.2)

    except:
        print("Error: Invalid Input")