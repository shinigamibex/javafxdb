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
from keras import backend as K
# K.set_image_dim_ordering('th')

if __name__ == '__main__':
    game_len = 10



    # winner = game.winner
    # print(winner.value)
    train_x = []


    def transform_states(states):
        full_board_image = []
        for i in range(8):
            full_board_image.append([])
            for state in states:
                for j in range(8):

                    full_board_image[-1].append([state[(i*8)+j]])
        return full_board_image




    model = Sequential()
    model.add(Conv2D(128, kernel_size=(5, 5),
                     input_shape=(8, 8*game_len,1), padding='same',activation='relu',))

    # model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
    model.add(Conv2D(256, (5, 5), activation='relu'))
    # model.add(Conv2D(512, (4, 4), activation='relu'))
    # model.add(Conv2D(128, (5, 5), activation='relu'))
    # model.add(Conv2D(32, (5, 5), activation='relu'))

    # model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(10000, activation='relu'))
    model.add(Dense(1, activation='softmax'))
    model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    # print(len(train_x))

    df = load_dataset()

    split_train = []
    split_test = []
    for i in range(10,16):
        games = parse_games(df, i)

        split_train_s,split_test_s = split_games(games, 0.8, i, ends_at_moves = True)
        split_train.extend(split_train_s)
        split_test.extend(split_test_s)

    train_x,train_y = transform(split_train, game_len,transform_states)
    test_x,test_y = transform(split_test, game_len,transform_states)
    # print(len(games))
    # print(parse_games)


    model.fit(train_x,train_y,shuffle=False)
    print(model.evaluate(test_x,test_y))
