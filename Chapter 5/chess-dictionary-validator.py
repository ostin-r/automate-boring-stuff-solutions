'''
Austin Richards 2/8/21

Chess dictionary validator will take a dictionary with keys and values in the form
'location':'piece_type' and check wether it is a valid board
(wether there are the correct amount of pieces, they are placed on the board, etc.)
'''

layout = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

'''
Valid board criteria:
- each player can only have 16 pieces at most
    - at most 8 pawns, 1 queen, and 2 of the rest
- each piece exists on the board
-BONUS: make the dictionary able to detect if bishops are duplicates based on board location
'''

# check that pieces are in a valid location, and that there are no repeats

# check that there are the correct number of each piece (ex. only two queens, one white one black)