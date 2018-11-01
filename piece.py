
from enum import Enum
class Piece(Enum):
    Paw = 0
    Pbw = 1
    Pcw = 2
    Pdw = 3
    Pew = 4
    Pfw = 5
    Pgw = 6
    Phw = 7
    Pab = 8
    Pbb = 9
    Pcb = 10
    Pdb = 11
    Peb = 12
    Pfb = 13
    Pgb = 14
    Phb = 15
    Raw = 16
    Rab = 17
    Rbw = 18
    Rbb = 19
    Kw = 20
    Kb = 21
    Naw = 22
    Nab = 23
    Nbw = 24
    Nbb = 25
    Qw = 26
    Qb = 27
    Caw = 28
    Cbw = 29
    Cab = 30
    Cbb = 31

class GenericPiece(Enum):
    Pawn = 0
    Knight = 1
    Castle = 2
    Rook = 3
    King = 4
    Queen = 5

class MoveType(Enum):
    MovePiece = 0
    TakePiece = 1
    Castle1 = 2
    Castle2 = 3
    EnPassant = 4

class Move(object):
    def __init__(self, ty, dest, start, piece):
        super().__init__()
        self.type = ty
        self.dest = dest
        self.start = start
        self.piece = piece

    def __str__(self):
        return "{} {} {} {}".format(self.type, self.dest, self.start, self.piece)


def parse_move_string(move_string):
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
        if p == 'N':
            piece = GenericPiece.Knight
        elif p == 'R':
            piece = GenericPiece.Rook
        elif p == 'C':
            piece = GenericPiece.Castle
        elif p == 'K':
            piece = GenericPiece.King
        elif p == 'Q':
            piece = GenericPiece.Queen

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
    return Move(moveType, dest, start, piece)

if __name__ == '__main__':
    print(parse_move_string('Rh1xe3'))
