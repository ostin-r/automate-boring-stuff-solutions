'''
Austin Richards 2/8/21

Chess dictionary validator will take a dictionary with keys and values in the form
'location':'piece_type' and check wether it is a valid board
(wether there are the correct amount of pieces, they are placed on the board, etc.)

Valid board criteria:
- each player can only have 16 pieces at most (at most 8 pawns, 1 queen, and 2 of the rest)
- each piece exists on the board and is not in the same place as any other pieces
- BONUS: make the dictionary able to detect if bishops are duplicates based on board location
'''

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'wbishop', '5h': 'bqueen', '3e': 'wking', '2f':'wbishop', '6a':'bbishop', '6c':'bbishop'}

locs   = list(board.keys())
pieces = list(board.values())
board_list = list(board.items())

valid_board = 'bking' and 'wking' in board.values()

for pos in locs:
    
    if int(pos[0]) > 8 or int(pos[0]) < 1:
        valid_board = False

    if pos[1] > 'h':
        valid_board = False

piece_count = {}

for character in pieces:
    piece_count.setdefault(character, 0)
    piece_count[character] += 1

if piece_count.get('wqueen', 0) > 1 or piece_count.get('bqueen', 0) > 1:
    valid_board = False

if piece_count.get('wbishop', 0) > 2 or piece_count.get('bbishop', 0) > 2:
    valid_board = False

if piece_count.get('wknight', 0) > 2 or piece_count.get('bknight', 0) > 2:
    valid_board = False

if piece_count.get('wrook', 0) > 2 or piece_count.get('brook', 0) > 2:
    valid_board = False

if piece_count.get('wpawn', 0) > 8 or piece_count.get('bpawn', 0) > 8:
    valid_board = False

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

    if wbishop_locs[0] not in black_squares and wbishop_locs[1] not in black_squares:
        valid_board = False

if piece_count.get('bbishop', 0) > 1:

    bbishop_locs = []

    for loc, piece in board_list:

        if piece == 'bbishop':

            bbishop_locs.append(loc)

    if bbishop_locs[0] in black_squares and bbishop_locs[1] in black_sqaures:
        valid_board = False

    if bbishop_locs[0] not in black_squares and bbishop_locs[1] not in black_squares:
        valid_board = False
            
print(bbishop_locs)
print(wbishop_locs)
print(valid_board)