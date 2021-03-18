'''
mcb.py is a multi-clipboard program by Al Sweigart, a follow along project in Ch. 9
of automate the boring stuff. I added a few features (delete, clear)

usage (vscode):
python mcb.py save <keyword> - saves clipboard to keyword
python mcb.py <keyword> - retrieves text from keyword to clipboard
python mcb.py list - copies all keywords to the clipboard
python mcb.py delete <keyword> - deletes the keyword and associated text
python mcb.py clear - deletes the entire multi-clipboard storage
'''
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:

    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    
    if sys.argv[1].lower() == 'list':

        if len(list(mcbShelf.keys())) == 0:
            pyperclip.copy('no keys saved')
        
        else:
            text = str(list(mcbShelf.keys()))
            pyperclip.copy(text)

    elif sys.argv[1] in mcbShelf:
        text = mcbShelf[sys.argv[1]]
        pyperclip.copy(text)

    elif sys.argv[1].lower() == 'clear':
        mcbShelf.clear()
 
mcbShelf.close()