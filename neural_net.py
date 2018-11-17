
import math
from keras import models
from keras import layers

num_layers = lambda a, moves: 20000 / (a*((64*moves) + 1))

class NeuralNet:
    def __init__(self, input_size):
        self.model = models.Sequential()
        self.input_size = input_size

        # input layer
        self.model.add(layers.Flatten())
        hidden = math.floor(num_layers(3, input_size))

        # builds the hidden layers
        self.build_layers(hidden)

        # output layer
        self.model.add(layers.Dense(1, activation="relu"))





    
    def build_layers(self, hidden):
        hidden_diff = math.ceil((self.input_size * 64 * 1.5) / hidden)
        for i in range(0, hidden):
            nodes = int(self.input_size * 64 * 1.5 - i * hidden_diff)
            self.model.add(layers.Dense(nodes, activation='relu'))


        # for
        # layer_counts = 

        # for _ in range(0, hidden):

