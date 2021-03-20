'''
Follow along project from Ch. 13 to read 
data from a spreadsheet
'''
import os
import openpyxl as xl
import pprint

os.chdir('follow-along/Chapters 10-20')

print('Opening workbook...')
wb = xl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# TODO: fill in county data with each county's population and tracts
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts':0, 'pop':0})
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

print('Writing results...')
with open('result-file.py', 'w') as file:
    file.write('all_data = ' + pprint.pformat(county_data))
print('Done!')