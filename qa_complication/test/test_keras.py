#!usr/bin/env python
# coding:utf-8


from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(input_dim=4, output_dim=9, activation="relu"))
model.add(Dense(output_dim=3, activation="softmax"))