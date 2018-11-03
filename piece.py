
from enum import Enum
class Piece(Enum):
    P1w = 0
    P2w = 1
    P3w = 2
    P4w = 3
    P5w = 4
    P6w = 5
    P7w = 6
    P8w = 7
    P1b = 8
    P2b = 9
    P3b = 10
    P4b = 11
    P5b = 12
    P6b = 13
    P7b = 14
    P8b = 15
    R1w = 16
    R1b = 17
    R2w = 18
    R2b = 19
    Kw = 20
    Kb = 21
    N1w = 22
    N1b = 23
    N2w = 24
    N2b = 25
    Qw = 26
    Qb = 27
    B1w = 28
    B2w = 29
    B1b = 30
    B2b = 31

class GenericPiece(Enum):
    Pawn = 0
    Knight = 1
    Rook = 2
    Bishop = 3
    King = 4
    Queen = 5

class MoveType(Enum):
    MovePiece = 0
    TakePiece = 1
    Castle1 = 2
    Castle2 = 3
    EnPassant = 4
    PawnPromotion = 5

class Move(object):
    def __init__(self, ty, dest, start, piece, promo = None):
        super().__init__()
        self.type = ty
        self.dest = dest
        self.start = start
        self.piece = piece
        self.promotion = promo

    def __str__(self):
        return "{} {} {} {}".format(self.type, self.dest, self.start, self.piece)

def get_piece(c):
    return {'B': GenericPiece.Bishop,
            'R': GenericPiece.Rook,
            'N': GenericPiece.Knight,
            'K': GenericPiece.King,
            'Q': GenericPiece.Queen}[c]

def parse_move_string(move_string):

    move_string = move_string.replace('+', '') # removes check symbols
    move_string = move_string.replace('#', '') # removes checkmate symbols

    # checks for castle type 1
    if move_string == 'O-O':
        return Move(MoveType.Castle1, None, None, None)
    # checks for castle type 2
    elif move_string == 'O-O-O':
        return Move(MoveType.Castle2, None, None, None)

    index = move_string.find('(ep)')
    hasEn = False
    promo = None
    if index != -1:
        # it is alway at the end
        move_string = move_string.substr(index)
        hasEn = True

    if move_string[-1].isupper():
        promo = get_piece(move_string[-1])
        move_string = move_string[0:-2]


    piece = GenericPiece.Pawn
    column = None
    row = None
    dest = None
    start = None
    moveType = MoveType.MovePiece

    # this is a for non pawn moves
    if move_string[0].isupper():
        p = move_string[0]
        move_string = move_string[1:]
        piece = get_piece(p)

    while len(move_string) > 2:
        if move_string[0].islower() or move_string[0].isdigit():
            c = move_string[0]
            move_string = move_string[1:]
            if (not c == 'x') and c.isalpha():
                column = ord(c) - ord('a') + 1
            elif (not c == 'x') and c.isdigit():
                row = int(c)
            elif c == 'x':
                moveType = MoveType.TakePiece
    dest = (int(move_string[1]), ord(move_string[0]) - ord('a') + 1)
    start = (column, row)
    if hasEn:
        moveType = MoveType.EnPassant
    if not promo is None:
        return Move(MoveType.PawnPromotion, dest, start, piece, promo)
    return Move(moveType, dest, start, piece)
