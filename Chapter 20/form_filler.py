'''
Follow-along project from ATBS Chapter 19

form_filler.py opens a pre-set google form
and automatically enters the data from form_data
'''
import pyautogui

def main():

    formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
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
    print('Ensure that the browser window is active and the form is loaded.')

    # TODO: give the user a chance to kill the process
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    pyautogui.sleep(5)

    # TODO: Wait until the form page has loaded.

    # TODO: Fill out the Name Field.

    # TODO: Fill out the Greatest Fear(s) field.

    # TODO: Fill out the Source of Wizard Powers field.

    # TODO: Fill out the RoboCop field.

    # TODO: Fill out the Additional Comments field.

    # TODO: Click Submit.

    # TODO: Wait until form page has loaded.

    # TODO: Click the Submit another response link.
    pass

main()