import os
from piece import *



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
