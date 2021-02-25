'''
mcb.py is a multi-clipboard program by Al Sweigart, a follow along project in Ch. 9
of automate the boring stuff

usage (vscode):
python mcb.py save <keyword> - saves clipboard to keyword
python mcb.py <keyword> - retrieves text from keyword to clipboard
python mcb.py list - copies all keywords to the clipboard
'''
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    
    if sys.argv[1].lower() == 'list':
        text = str(list(mcbShelf.keys()))
        pyperclip.copy(text)

    elif sys.argv[1] in mcbShelf:
        text = mcbShelf[sys.argv[1]]
        pyperclip.copy(text)

mcbShelf.close()