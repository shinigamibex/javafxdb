
import math
from keras import models
from keras import optimizers
from keras import layers

num_layers = lambda a, moves: 20000 / (a*((64*moves) + 1))

class NeuralNet:
    def __init__(self, input_size):
        self.model = models.Sequential()
        self.input_size = input_size

        # input layer
        self.model.add(layers.Flatten())
        # self.model.add(layers.Dense(input_size*64, input_shape=(32,input_size, 64)))
        hidden = math.floor(num_layers(3, input_size))

        # builds the hidden layers
        self.build_layers(hidden)

        # output layer
        self.model.add(layers.Dense(1, activation="sigmoid"))
        sgd = optimizers.SGD(lr=0.1)
        self.model.compile(
            optimizer=sgd,
            loss="binary_crossentropy",
            metrics=['accuracy']
        )
    
    def build_layers(self, hidden):
        hidden_diff = math.ceil(((self.input_size * 64) - 5)/ hidden)
        for i in range(0, hidden):
            nodes = int(self.input_size * 64 - i * hidden_diff)
            self.model.add(layers.Dense(nodes, activation='relu'))

    def summary(self):
        self.model.summary()

    def fit(self, x, y, epochs):
        self.model.fit(x, y, epochs=epochs)

    def eval(self, x, y):
        test_loss, test_acc = self.model.evaluate(x, y)
        return test_acc

    def predict(self, x):
        return self.model.predict(x)