import os
import chess
from dataset import *
from game import *



if __name__ == '__main__':
    df = load_dataset()
    game = parse_games(df)[0]

    states = get_board_states(game, 5)
    print(states)

    print(get_board_state(game, 5))





# all_chess_games = []
#
#
# chess_game = []
#
# #needs to be updated
# default_starting_board = {Piece.P1w:(2,1),
#                           Piece.P2w:(2,2),
#                           Piece.P3w:(2,3),
#                           Piece.P4w:(2,4),
#                           Piece.P5w:(2,5),
#                           Piece.P6w:(2,6),
#                           Piece.P7w:(2,7),
#                           Piece.P8w:(2,8),
#
#                           Piece.R1w:(1,1),
#                           Piece.N1w:(1,2),
#                           Piece.B1w:(1,3),
#                           Piece.Qw:(1,4),
#                           Piece.Kw:(1,5),
#                           Piece.B2w:(1,6),
#                           Piece.N2w:(1,7),
#                           Piece.R2w:(1,8),
#
#                           Piece.P1b:(7,2),
#                           Piece.P2b:(7,2),
#                           Piece.P3b:(7,2),
#                           Piece.P4b:(7,2),
#                           Piece.P5b:(7,2),
#                           Piece.P6b:(7,2),
#                           Piece.P7b:(7,2),
#                           Piece.P8b:(7,2),
#
#                           Piece.R1b:(8,1),
#                           Piece.N1b:(8,2),
#                           Piece.B1b:(8,3),
#                           Piece.Qb:(8,4),
#                           Piece.Kb:(8,5),
#                           Piece.B2b:(8,6),
#                           Piece.N2b:(8,7),
#                           Piece.R2b:(8,8),
#                           }
#
# current_board = {}
# #True is white
# #Fasle is black
# player = True
# take_piece = False
#
# move = Move(MoveType.MovePiece,(3,1),(None,None),GenericPiece.Pawn)
#
#
#
#
#
# def player_move(move):
#     global player, take_piece
#     move_obj=move
#     # move_obj = parse_move_string(move)
#     #rank or file
#     take_piece = False
#     if(move_obj.type == MoveType.TakePiece):
#         take_piece = True
#         piece = check_for_piece_in_row_and_col(move_obj.dest[0],move_obj.dest[1])
#         current_board[piece]=None
#
#     if(move_obj.type == MoveType.TakePiece or move_obj.type == MoveType.MovePiece):
#         if (move_obj.start[0] or move_obj.start[1]):
#             piece = get_piece_from_generic_location(move_obj.piece,move_obj.start)
#         else:
#             piece = get_piece_from_generic(move_obj.piece,move_obj.dest)
#         update_board(move_obj,piece)
#     print(piece)
#
# def pawn_take_piece_get_position(location):
#
#     pass
#
# def get_piece_from_generic(gen_piece,dest):
#     if(gen_piece == GenericPiece.Rook):
#         return get_s_piece_from_straights(gen_piece,dest)
#     if(gen_piece == GenericPiece.Pawn):
#         return get_pawn_piece_from_dest(dest)
#     if(gen_piece == GenericPiece.Bishop):
#         return get_s_piece_from_diags(gen_piece,dest)
#     if(gen_piece == GenericPiece.Knight):
#         return get_s_piece_from_Ls(gen_piece,dest)
#     if(gen_piece == GenericPiece.Queen or gen_piece == GenericPiece.King):
#         return get_single_piece(gen_piece)
#
#
#
# def get_piece_color(piece):
#     if(str(piece)[-1] == 'w'):
#         return True
#     else:
#         return False
#
# def get_s_piece_from_straights(gen_piece,location):
#     global player
#     #need 4 diagonals from the locatin:
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r+=1
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if p_at_loc == None:
#             break
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r-=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         c+=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         c-=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#
# def get_s_piece_from_diags(gen_piece,location):
#     global player
#     #need 4 diagonals from the locatin:
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r+=1
#         c+=1
#
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if p_at_loc == None:
#             break
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r-=1
#         c+=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r+=1
#         c-=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#     r=location[0]
#     c=location[1]
#     while (r<=8 and c <=8 and r >=1 and c >= 1):
#         r-=1
#         c-=1
#         if p_at_loc == None:
#             break
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(r,c))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(r,c)
#
#
# #pawn can move up one or two from destination
# def get_pawn_piece_from_dest(dest):
#     print("pawn 2")
#     global player
#     global take_piece
#     if take_piece:
#         print("NOT HERE")
#         if player:
#             p1 = check_for_piece_in_row_and_col(dest[0]-1,dest[1]-1)
#             p2 = check_for_piece_in_row_and_col(dest[0]-1,dest[1]+1)
#             if p1 and map_specific_to_generic_piece(p1) == GenericPiece.Pawn:
#                 return p1
#             else:
#                 return p2
#         else:
#             p1 = check_for_piece_in_row_and_col(dest[0]+1,dest[1])
#             p2 = check_for_piece_in_row_and_col(dest[0]+2,dest[1])
#             if p1 and map_specific_to_generic_piece(p1) == GenericPiece.Pawn:
#                 return p1
#             else:
#                 return p2
#
#     else:
#         if player:
#             p1 = check_for_piece_in_row_and_col(dest[0]-1,dest[1])
#             p2 = check_for_piece_in_row_and_col(dest[0]-2,dest[1])
#             if p1:
#                 return p1
#             else:
#                 return p2
#         else:
#             p1 = check_for_piece_in_row_and_col(dest[0]+1,dest[1])
#             p2 = check_for_piece_in_row_and_col(dest[0]+2,dest[1])
#             if p1:
#                 return p1
#             else:
#                 return p2
#
#
#
# def get_s_piece_from_Ls(gen_piece,location):
#     global player
#     checks = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
#     for i in checks:
#         p_at_loc = map_specific_to_generic_piece(check_for_piece_in_row_and_col(location[0]+i[0],location[1]+i[1]))
#         if(p_at_loc ==  gen_piece):
#             if(get_piece_color(p_at_loc) == player):
#                 return check_for_piece_in_row_and_col(location[0]+i[0],location[1]+i[1])
#
#
#
#
# def get_piece_from_generic_location(gen_piece,location):
#     if(move_obj.start[0] and move_obj.start[1]):
#         return check_for_piece_in_row_and_col(move_obj.start[0],move_obj.start[1])
#     elif (move_obj.start[1]):
#         return check_for_piece_in_col(gen_piece,move_obj.start[1])
#     elif (move_obj.start[0]):
#         return check_for_piece_in_row(gen_piece,move_obj.start[0])
#
# def check_for_piece_in_row(gen_piece,row):
#     global player
#     for piece,loc in enumerate(current_board):
#         if(loc[1]==row and map_specific_to_generic_piece(piece)==gen_piece):
#             if(get_piece_color(piece) == player):
#                 return piece
#
# def check_for_piece_in_col(gen_piece,col):
#     global player
#
#     for piece,loc in enumerate(current_board):
#         if(loc[0]==col and map_specific_to_generic_piece(piece)==gen_piece):
#             if(get_piece_color(piece) == player):
#                 return piece
#
# def check_for_piece_in_row_and_col(row,col):
#     global player
#     # print(current_board)
#     for i,piece in enumerate(current_board):
#         print(current_board[piece])
#         if(current_board[piece][0] == row and current_board[piece][1] == col ):
#             if(get_piece_color(piece) == player):
#                 return piece
#
# def get_single_piece(gen_piece):
#     global player
#
#     for piece,loc in enumerate(current_board):
#         if(get_piece_color(piece) == player and piece == gen_piece):
#             return piece
#
# def map_specific_to_generic_piece(specific_piece):
#     if(specific_piece[0] == 'P'):
#         return GenericPiece.Pawn
#     if(specific_piece[0] == 'R'):
#         return GenericPiece.Rook
#     if(specific_piece[0] == 'Q'):
#         return GenericPiece.Queen
#     if(specific_piece[0] == 'B'):
#         return GenericPiece.Bishop
#     if(specific_piece[0] == 'N'):
#         return GenericPiece.Knight
#     if(specific_piece[0] == 'K'):
#         return gen_Piece.King
#
# #update board position
# def update_board(move, piece):
#     global current_board
#     if check_for_piece_in_row_and_col(move.dest[0],move.dest[1]):
#         print("ERRORRRRRR piece is not supposed to be there, get rid of it")
#     current_board[piece] = move.dest
#     pass
#
# #remove piece from board
# def take_piece(move, piece):
#     pass
#
# def castle1():
#     pass
#
# def castle2():
#     pass
#
# def en_passan(move, piece):
#     pass
#
# def do_full_game(game_list):
#     global player, take_piece, current_board
#     current_board = default_starting_board.copy()
#     #call player_move_multiple times
#
#     for move in game_list:
#         # move = parse_move_string(move)
#         player_move(move)
#         player = not player
#     print(current_board)
#
# do_full_game([move])
