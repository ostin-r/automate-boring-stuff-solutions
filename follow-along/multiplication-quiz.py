'''
Austin Richards 2/20/21

Follow along project from chapter 8: multiplication quiz
'''
import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = 'Question {0}: {1} x {2} \n'.format(questionNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^{}$'.format(num1 * num2)],
                        blockRegexes=[('.*', 'Incorrect!')],
                        timeout=4, limit=0)

    except pyip.TimeoutException:
        print('Out of time!\n')
    except pyip.RetryLimitException:
        print('\n')

    else:
        print('Correct!\n')
        correctAnswers += 1

    time.sleep(1)

print('Score: {0} / {1}'.format(correctAnswers, numberOfQuestions))