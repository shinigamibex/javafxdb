# Importing the Keras libraries and packages

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import numpy as np
import os
import chess
from dataset import *
from game import *

if __name__ == '__main__':
    df = load_dataset()
    game = parse_games(df)[0]

    states = get_board_states(game, 5)
    # print(states)

    # print(get_board_state(game, 5))

    full_board_image = []
    for i in range(8):
        for state in states:
            for j in range(8):
                full_board_image.append(state[(i*8)+j])
    print(full_board_image)

    
