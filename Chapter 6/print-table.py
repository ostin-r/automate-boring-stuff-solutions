'''
Austin Richards 2/13/21

A text exercise from ch. 6 which will take
a list of lists and print it in a nice-looking
grid with each column righ-justified.
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

title = 'Items'

col_width = [0] * len(tableData)
lengths = [[], [], []]

for i in range(len(tableData)):

    for item in tableData[i]:
        lengths[i].append(len(item))
    
    col_width[i] = max(lengths[i])

for y in range(len(tableData[0])):

    for x in range(len(tableData)):
        print(tableData[x][y].rjust(col_width[x]), end=' ')

    print('')