import os
import chess
from dataset import *
from game import *
import math
import neural_net

if __name__ == '__main__':
    moves = 20
    nn = neural_net.NeuralNet(moves)

    # nn.summary()
    
    df = load_dataset()
    games = parse_games(df, None)
    train, test = split_games(games, 0.8, moves, True)

    x_train, y_train = transform(train, moves)
    x_test, y_test = transform(test, moves)




    nn.fit(x_train, y_train, 10)
    
    nn.summary()

    acc = nn.eval(x_test, y_test)
    print("Acc: ", acc)
