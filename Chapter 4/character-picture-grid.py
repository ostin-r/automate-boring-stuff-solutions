'''
Austin Richards 2/8/21

The third practice problem in ch. 4 is simply printing an image
with characters and the list data type in a 2x2 format.
(with convenction that x and y are indexed at grid[x][y], as decided by the author)
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



for j in range(len(grid[0])):        # hard coded sublist length because list is square

    for i in range(len(grid)):
        
        print(grid[i][j], end='')

    print('')

