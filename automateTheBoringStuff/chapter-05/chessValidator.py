def isValidChessBoard(pieces):

    validPieces = ['pawn' , 'knight' , 'bishop', 'rook','queen' , 'king']
    whitePieces = {'pawn':0 , 'knight' : 0 , 'bishop':0 , 'rook':0 , 'queen':0 , 'king':0}
    blackPieces = {'pawn':0 , 'knight' : 0 , 'bishop':0 , 'rook':0 , 'queen':0 , 'king':0}

    for position, piece in pieces.items():
        if piece[1:] not in validPieces:
            return False
        if piece[0] not in 'wb':
            return False
        if position not in [f'{i}{j}' for i in range(1,9) for j in 'abcdefgh']:
            return False
        if piece[0] == 'w':
            whitePieces[piece[1:]] += 1
        else:
            blackPieces[piece[1:]] += 1

    if(blackPieces['pawn'] >8 or blackPieces['bishop']>2 or blackPieces['knight']>2 or blackPieces['rook'] >2 or blackPieces['queen']>1 or blackPieces['king']!=1):
        return False
    if(whitePieces['pawn'] >8 or whitePieces['bishop']>2 or whitePieces['knight']>2 or whitePieces['rook'] >2 or whitePieces['queen']>1 or whitePieces['king']!=1):
        return False
    if(sum(whitePieces.values()) >16 or sum(blackPieces.values()) >16):
        return False
    
    return True

chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_board))
