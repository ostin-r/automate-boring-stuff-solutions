'''
Austin Richards 2/21/21
'''
import random, time

questionAmount = 3
correctAnswers = 0

for questionNumber in range(questionAmount):

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans  = num1 * num2

    prompt = 'Question {0}: {1} x {2} ='.format(questionNumber, num1, num2)
    print(prompt)

    incorrectCount = 0

    while True:
        try:
            userInput = int(input())

            if userInput == ans:
                correctAnswers += 1
                print('Correct\n')
                break

            elif userInput != ans and incorrectCount < 2:
                incorrectCount += 1
                print('Incorrect, try again')

            else:
                print('Incorrect, too many guesses')
                break

        except ValueError:
            print('Please enter a number.')
