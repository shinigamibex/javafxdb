import os
from piece import *
from board import *


all_chess_games = []


chess_game = []


current_board = {}
#True is white
#Fasle is black
player = True

def do_full_game(game_list):
    current_board = default_starting_board.copy()
    #call player_move_multiple times
    for move in game_list:
        move = parse_move_string(move)
        player_move(piece,move)
        player = !player


def player_move(move):
    move_obj = parse_move_string(move)
    if (move_obj.start[0] or move_obj.start[1]):
        get_piece_from_generic_location(move_obj.type,move_obj.start)
    else:
        get_piece_from_generic(move.type)

def get_piece_from_generic(gen_piece):
    pass

def get_piece_color(piece):
    if(piece[-1] == 'w'):
        return True
    else:
        return False

def get_s_piece_from_straights(gen_piece,location):
    for i in range(1,9):
        p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(i,location[1]))
        if(p_at_loc ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(i,location[1])
    for i in range(1,9):
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(location[0],i)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(i,location[1])

def get_s_piece_from_diags(gen_piece,location):
    pass

def get_s_piece_from_Ls(gen_piece,location):
    pass

def get_s_pawn(gen_piece,location):
    pass


def get_piece_from_generic_location(gen_piece,location):
    if(move_obj.start[0] and move_obj.start[1]):
        return check_for_piece_in_row_and_col(move_obj.start[0],move_obj.start[1]):
    else if (move_obj.start[1]):
        return check_for_piece_in_col(gen_piece,move_obj.start[1])
    else if (move_obj.start[0]):
        return check_for_piece_in_row(gen_piece,move_obj.start[0])

def check_for_piece_in_row(gen_piece,row):
    for piece,loc in enumerate(current_board):
        if(loc[1]==row and map_specific_to_generic_piece(piece)==gen_piece):
            if(get_piece_color(piece) == player):
                return piece

def check_for_piece_in_col(gen_piece,col):
    for piece,loc in enumerate(current_board):
        if(loc[0]==col and map_specific_to_generic_piece(piece)==gen_piece):
            if(get_piece_color(piece) == player):
                return piece

def check_for_piece_in_row_and_col(row,col):
    for piece,loc in enumerate(current_board):
        if(loc == "{}{}".format(row,col)):
            if(get_piece_color(piece) == player):
                return piece

def map_specific_to_generic_piece(specific_piece):
    if(specific_piece[0] == 'P'):
        return GenericPiece.Pawn
    if(specific_piece[0] == 'R'):
        return GenericPiece.Rook
    if(specific_piece[0] == 'Q'):
        return GenericPiece.Queen
    if(specific_piece[0] == 'B'):
        return GenericPiece.Bishop
    if(specific_piece[0] == 'N'):
        return GenericPiece.Knight
    if(specific_piece[0] == 'K'):
        return gen_Piece.King

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
