'''
Follow-along project from ATBS Chapter 19

form_filler.py opens a pre-set google form
and automatically enters the data from form_data
'''
import pyautogui
import webbrowser

def main():

    formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 1, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the\
            break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public\
            trust. Uphold the law.'},
           ]

    # initialization stuff
    pyautogui.PAUSE = 0.5 # this sets the universal pause between functions to half a second
    webbrowser.open('https://autbor.com/form', new=1)
    submit_another_response = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform?usp=form_confirm'

    for person in formData:
        # give the user a chance to kill the process, wait for webbrowser to load
        print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        pyautogui.sleep(5)
        print(f"Entering {person['name']}'s info...")

        # fill out the name and greatest fears field
        pyautogui.write(['\t', '\t'])
        pyautogui.write(person['name'] + '\t')
        pyautogui.write(person['fear'] + '\t')

        # fill out the Source of Wizard Powers field
        if person['source'] == 'wand':
            pyautogui.write(['down', 'enter'], 0.5)
        elif person['source'] == 'amulet':
            pyautogui.write(['down', 'down', 'enter'] , 0.5)
        elif person['source'] == 'crystal ball':
            pyautogui.write(['down', 'down', 'down', 'enter'] , 0.5)
        elif person['source'] == 'money':
            pyautogui.write(['down', 'down', 'down', 'down', 'enter'] , 0.5)

        # Fill out the RoboCop field.
        pyautogui.write(['\t', ' '] + ['right'] * (person['robocop'] - 1))

        # Fill out the Additional Comments field
        pyautogui.write('\t\t' + person['comments'] + '\t')

        # click submit, wait 5 seconds
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        print('Form submitted!')
        pyautogui.sleep(5)

        break #TODO remove this line when done testing

    # TODO: Wait until form page has loaded.

    # TODO: Click the Submit another response link.

main()