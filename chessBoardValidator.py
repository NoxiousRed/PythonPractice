def isValidChessBoard(board_dict):
     # check for EXACTLY one black and one white king
    if 'bking' not in board_dict.values() or 'wking' not in board_dict.values():
        return False
    bking = 0
    wking = 0
    for king in board_dict.values():
        if king == 'bking':
            bking+=1
        if king == 'wking':
            wking+=1
        if bking > 1 or wking > 1:
            return False
    
    # check for a maximum of 16 pieces per player
    whitePieces = 0
    blackPieces = 0
    for item in board_dict.values():
        if item[0] == 'w':
            whitePieces+=1
        if item[0] == 'b':
            blackPieces+=1
        if whitePieces > 16 or blackPieces > 16:
            return False
    
    # check for at most 8 pawns per player
    white_pawns = 0
    black_pawns = 0
    for pawn in board_dict.values():
        if pawn == 'bpawn':
            black_pawns+=1
        if pawn == 'wpawn':
            white_pawns+1
        if white_pawns > 8 or black_pawns > 8:
            return False
    
    # check for a valid location
    board_keys = {'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' ',
                  'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
                  'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
                  'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
                  'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
                  'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
                  'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
                  'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' '}
    for v in board_dict.keys():
        if v not in board_dict.keys():
            return False
    
    # check if the name starts with a "w" or "b"
    for pieces in board_dict.values():
        if pieces[0] != "b" and pieces[0] != "w":
            return False             
    
    # check if the piece name is valid
    piece_names = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for names in board_dict.values():
        if names[1:] not in piece_names:
            return False
    return True    

print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))