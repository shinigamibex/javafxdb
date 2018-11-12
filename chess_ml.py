import os
from piece import *
from board import *


all_chess_games = []


chess_game = []

#needs to be updated
default_starting_board = {Piece.P1w:(2,1),
                          Piece.P2w:(2,2),
                          Piece.P3w:(2,3),
                          Piece.P4w:(2,4),
                          Piece.P5w:(2,5),
                          Piece.P6w:(2,6),
                          Piece.P7w:(2,7),
                          Piece.P8w:(2,8),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2),
                          Piece.P2w:(2,2)}

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
    #rank or file
    if (move_obj.start[0] or move_obj.start[1]):
        piece = get_piece_from_generic_location(move_obj.piece,move_obj.start)
    else:
        piece =get_piece_from_generic(move_obj.piece,move_obj.dest)

def get_piece_from_generic(gen_piece,dest):
    if(gen_piece == GenericPiece.Rook):
        return get_s_piece_from_straights(gen_piece,dest)
    if(gen_piece == GenericPiece.Pawn):
        return get_pawn_piece_from_dest(dest)
    if(gen_piece == GenericPiece.Bishop):
        return get_s_piece_from_diags(gen_piece,dest)
    if(gen_piece == GenericPiece.Knight):
        return get_s_piece_from_Ls(gen_piece,dest)


def get_piece_color(piece):
    if(piece[-1] == 'w'):
        return True
    else:
        return False

def get_s_piece_from_straights(gen_piece,location):
    #do columns first
    for i in range(1,9):
        p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(i,location[1]))
        if(p_at_loc ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(i,location[1])
    #then do rows
    for i in range(1,9):
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(location[0],i)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(i,location[1])

def get_s_piece_from_diags(gen_piece,location):
    #need 4 diagonals from the locatin:
    r=location[0]
    c=location[1]
    while (r<=8 and c <=8 and r >=1 and c >= 1):
        r+=1
        c+=1
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(r,c)
    r=location[0]
    c=location[1]
    while (r<=8 and c <=8 and r >=1 and c >= 1):
        r-=1
        c+=1
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(r,c)
    r=location[0]
    c=location[1]
    while (r<=8 and c <=8 and r >=1 and c >= 1):
        r+=1
        c-=1
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(r,c)
    r=location[0]
    c=location[1]
    while (r<=8 and c <=8 and r >=1 and c >= 1):
        r-=1
        c-=1
        if(map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c)) ==  gen_piece):
            if(get_piece_color(p_at_loc) == player):
                return check_for_piece_in_row_and_col(r,c)


#pawn can move up one or two from destination
def get_pawn_piece_from_dest(location):
    if player:
        p1 = check_for_piece_in_row_and_col([dest[0]-1,dest[1]])
        p2 = check_for_piece_in_row_and_col([dest[0]-2,dest[1]])
        if p1:
            return p1
        else:
            return p2
    else:
        p1 = check_for_piece_in_row_and_col([dest[0]+1,dest[1]])
        p2 = check_for_piece_in_row_and_col([dest[0]+2,dest[1]])
        if p1:
            return p1
        else:
            return p2



def get_s_piece_from_Ls(gen_piece,location):
    checks = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

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
