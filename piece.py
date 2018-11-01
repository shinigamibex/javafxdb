
from enum import Enum
class Piece(Enum):
    aw = 0
    bw = 1
    cw = 2
    dw = 3
    ew = 4
    fw = 5
    gw = 6
    hw = 7
    ab = 8
    bb = 9
    cb = 10
    db = 11
    eb = 12
    fb = 13
    gb = 14
    hb = 15
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

class MoveType(Enum):
    MovePiece = 0
    TakePiece = 1
    Castle1 = 2
    Castle2 = 3
    EnPassant = 4

class Move(object):
    def __init__(self, ty, loc, piece):
        super().__init__()
        self.type = ty
        self.loc = loc
        self.piece = piece


def parse_move_string(move_string, player):
    pass
