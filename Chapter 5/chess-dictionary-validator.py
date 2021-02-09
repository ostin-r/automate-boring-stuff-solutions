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

valid_board = True
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

locs   = list(board.keys())
pieces = list(board.values())

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

if piece_count.get('wknight', 0) > 2 or piece_count.get('knight', 0) > 2:
    valid_board = False

if piece_count.get('wrook', 0) > 2 or piece_count.get('brook', 0) > 2:
    valid_board = False

if piece_count.get('wpawn', 0) > 8 or piece_count.get('bpawn', 0) > 8:
    valid_board = False

print(valid_board)