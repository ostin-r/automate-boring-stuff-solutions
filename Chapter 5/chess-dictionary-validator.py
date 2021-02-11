'''
Austin Richards 2/8/21

Chess dictionary validator will take a dictionary with keys and values in the form
'location':'colorpiece' and check wether it is a valid board

Valid board criteria:
- each player can only have 16 pieces at most (at most 8 pawns, 1 queen, and 2 of the rest)
- each piece exists on the board
- BONUS: make the dictionary able to detect if bishops are duplicates based on board location
'''

board = {'1h': 'bking', '6c': 'wqueen', '5h': 'bqueen', '3e': 'wking', '6a':'bbishop', '6c':'bbishop'}

locs   = list(board.keys())
pieces = list(board.values())
board_list = list(board.items())

message = 'Pass'
valid_board = 'bking' and 'wking' in board.values()

if not valid_board:
    message = 'Not enough kings'

for pos in locs:
    
    if int(pos[0]) > 8 or int(pos[0]) < 1:
        valid_board = False
        message = 'Invalid Location'

    if pos[1] > 'h':
        valid_board = False
        message = 'Invalid Location'

piece_count = {}

for character in pieces:
    piece_count.setdefault(character, 0)
    piece_count[character] += 1

if piece_count.get('wking', 0) > 1 or piece_count.get('bking', 0) > 1:
    valid_board = False
    print('Too many kings')

if piece_count.get('wqueen', 0) > 1 or piece_count.get('bqueen', 0) > 1:
    valid_board = False
    message = 'Too many queens'

if piece_count.get('wbishop', 0) > 2 or piece_count.get('bbishop', 0) > 2:
    valid_board = False
    message = 'Too many bishops'

if piece_count.get('wknight', 0) > 2 or piece_count.get('bknight', 0) > 2:
    valid_board = False
    message = 'Too many knights'

if piece_count.get('wrook', 0) > 2 or piece_count.get('brook', 0) > 2:
    valid_board = False
    message = 'Too many rooks'

if piece_count.get('wpawn', 0) > 8 or piece_count.get('bpawn', 0) > 8:
    valid_board = False
    message = 'Too many pawns'

# BONUS IMPLEMENTATION
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ['1', '2', '3', '4', '5', '6', '7', '8']

black_squares = []

for i in range(0, len(x), 2):

    for j in range(0, len(y), 2):

        black_squares.append(x[i] + y[j])

for i in range(1, len(x), 2):

    for j in range(1, len(y), 2):

        black_squares.append(x[i] + y[j])

if piece_count.get('wbishop', 0) > 1:

    wbishop_locs = []

    for loc, piece in board_list:

        if piece == 'wbishop':

            wbishop_locs.append(loc)

    if wbishop_locs[0] in black_squares and wbishop_locs[1] in black_sqaures:
        valid_board = False
        message = 'Bishops cannot be on the same color space'

    if wbishop_locs[0] not in black_squares and wbishop_locs[1] not in black_squares:
        valid_board = False
        message = 'Bishops cannot be on the same color space'

if piece_count.get('bbishop', 0) > 1:

    bbishop_locs = []

    for loc, piece in board_list:

        if piece == 'bbishop':

            bbishop_locs.append(loc)

    if bbishop_locs[0] in black_squares and bbishop_locs[1] in black_sqaures:
        valid_board = False
        message = 'Bishops cannot be on the same color space'

    if bbishop_locs[0] not in black_squares and bbishop_locs[1] not in black_squares:
        valid_board = False
        message = 'Bishops cannot be on the same color space'
     
print(valid_board)
print(message)