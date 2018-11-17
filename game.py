import chess
from enum import Enum
import numpy as np


class Player(Enum):
    White = 0
    Black = 1

class Game(object):
    uid = 0
    def __init__(self, winner, moves):
        super().__init__()
        # self.board = board
        self.winner = winner
        self.moves = moves
        self.id = Game.uid
        Game.uid += 1

    def __str__(self):
        return "Game({}, {}, {})".format(self.id, self.winner, len(self.moves))

def parse_games(df):
    games = []
    for _, d in df.iterrows():
        # we need the board inorder to parse the move
        board = chess.Board()
        winner = d['winner']
        moves = d['moves'].split()
        m = []
        for _moves in moves:
            move = board.parse_san(_moves)
            board.push(move)
            m.append(move)

        if winner == 'white':
            winner = Player.White
        else:
            winner = Player.Black
        games.append(Game(winner, m))
    return games

def piece_value(p):
    return {
        'N': 3,
        'R': 5,
        'B': 3,
        'K': 1,
        'Q': 9,
        'P': 1
    }[p]

def parse_fen_row(row):
    nrow = []
    for cell in row:
        if cell.isdigit():
            for _ in range(0, int(cell)):
                nrow.append(0)
        elif cell.isupper():
            nrow.append(piece_value(cell))
        else:
            nrow.append(-piece_value(cell.upper()))
    return nrow


def parse_fen(fen):
    rows = fen.split('/')
    # rows.reverse()
    board = []
    for row in rows:
        board.extend(parse_fen_row(row))
    return board


def get_board_states(game, num_moves):
    board = chess.Board()
    board_states = []
    for i in range(0, num_moves):
        board.push(game.moves[i])
        fen = board.board_fen()
        board_states.append(np.array(parse_fen(fen)))
    return np.array(board_states)

def get_board_state(game, move_index):
    board = chess.Board()
    for i in range(0, move_index):
        board.push(game.moves[i])
    return parse_fen(board.board_fen())

def transform(games, num_moves, trans = None):
    x = []
    y = []
    for game in games:
        states = get_board_states(game, num_moves)
        if not trans is None:
            states = trans(states)
        x.append(states)
        y.append(game.winner.value)
    return np.array(x), np.array(y)

    