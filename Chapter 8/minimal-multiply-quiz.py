'''
Austin Richards 2/21/21
'''
import random, time

questionAmount = 5
correctAnswers = 0

for questionNumber in range(questionAmount):

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans  = num1 * num2

    prompt = 'Question {0}: {1} x {2} ='.format(questionNumber, num1, num2)
    print(prompt)

    incorrectCount = 0
    startTime = time.time()

    while True:
        try:
            userInput = int(input())

            timeout = time.time() - startTime
            if timeout > 8.0:
                if userInput == ans:
                    print('Correct, but took too long\n')
                    time.sleep(1)
                    break
                else:
                    print('Incorrect, took too long\n')
                    time.sleep(1)
                    break

            if userInput == ans:
                correctAnswers += 1
                print('Correct\n')
                time.sleep(1)
                break

            elif userInput != ans and incorrectCount < 2:
                incorrectCount += 1
                print('Incorrect, try again')

            else:
                print('Incorrect, too many guesses\n')
                time.sleep(1)
                break

        except ValueError:
            print('Please enter a number.')

print('Score: {0} / {1} ({2}%)'.format(correctAnswers, questionAmount, 100*correctAnswers/questionAmount))