'''
Ch. 10 follow along project.  replace-dates.py will look for american
dates in filenames and change them to eurpean style dates.
'''
import shutil, os, re
from pathlib import Path as path

os.chdir('follow-along')
print('\n' + str(path.cwd()))

date_regex = re.compile(r'''
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d{2})
    (.*?)$
    ''', re.VERBOSE)

for filename in os.listdir('.'):

    mo = date_regex.search(filename)

    if mo is None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    end_part = mo.group(8)

    euro_name = before_part + day_part + '-' + month_part + '-' + year_part + end_part

    abs_cwd = os.path.abspath('.')
    filename = os.path.join(abs_cwd, filename)
    euro_name = os.path.join(abs_cwd, euro_name)

    shutil.move(filename, euro_name)