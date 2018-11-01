import os
from piece import *
from board import *


all_chess_games = []


chess_game = []


current_board = {}
player = True

def do_full_game(game_list):
    current_board = default_starting_board.copy()
    #call player_move_multiple times
    for move in game_list:
        move = parse_move_string(move)
        player_move(piece,move)
        player = !player


def player_move(move):
    
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
