#! python3
''' 
A follow along program in Automate the Boring Stuff
for replying to emails quickly by using the pyperclip
module to quickly paste prepared responses
'''
import pyperclip
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' added to clipboard.' )
else:
    print('There is no text for ' + keyphrase)
