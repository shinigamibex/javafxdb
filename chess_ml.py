import os

from enum import Enum
class Piece(Enum):
    aw = 1
    bw = 2
    cw = 3
    dw = 3
    ew = 3
    fw = 3
    gw = 3
    hw = 3
    ab = 1
    bb = 2
    cb = 3
    db = 3
    eb = 3
    fb = 3
    gb = 3
    hb = 3
    Raw = 3
    Rab = 4
    Rbw =3
    Rbb = 6
    Kw = 2
    Kb = 3
    Naw = 4
    Nab = 4
    Nbw = 4
    Nbb = 4
    Qw = 3
    Qb = 3
    Caw = 3
    Cbw = 3
    Cab = 4
    Cbb = 6


all_chess_games = []


chess_game = []

default_starting_board = {}
current_board = {}
player = True

def do_full_game(game_list):
    #call player_move_multiple times
    for move in game_list:
        piece,move = parse_move_string(move)
        player_move(piece,move)
        player = !player


def player_move(piece, move):
    #at end
    #if take move take_move()
    #if castle do castle1()
    pass

def parse_move_string(move_string):
    pass

def check_if_piece_exists(board,piece):
    pass

def check_piece_at_loc(board,location):
    pass

def move_piece(move, piece):
    pass

def take_piece(move, piece):
    pass

def castle1():
    pass

def castle2():
    pass

def en_passan(move, piece):
    pass
