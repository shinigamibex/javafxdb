# Importing the Keras libraries and packages

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import numpy as np

# batch_size = 128
# num_classes = 10
# epochs = 12
#
# # input image dimensions
# img_rows, img_cols = 28, 28
#
# # the data, split between train and test sets
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
