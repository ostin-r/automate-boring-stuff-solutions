'''
Austin Richards 2/23/21

random-quiz-generator.py is a follow-along project in Ch. 9 of
Automate the Boring Stuff.  It uses basic file i/o to generate
35 quizzes each with randomly placed questions.
'''
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(2):
    
    quizFile = open('quiz-{}.txt'.format(quizNum + 1), 'w')

    ansFile  = open('ans-{}.txt'.format(quizNum + 1), 'w')

    quizHeader = 'Name:\n\nDate:\n\nPeriod:\n\nState Capitols Quiz (form {})\n'.format(quizNum + 1)
    quizFile.write(quizHeader)

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('{0}. What is the capital of {1}\n'.format(questionNum + 1, states[questionNum]))
        
        for i in range(4):
            quizFile.write('{0}. {1}\n'.format('ABCD'[i], answerOptions[i]))
        
        quizFile.write('\n')
        ansFile.write('{0} : {1}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
ansFile.close()