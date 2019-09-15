# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:37:18 2019

C-type function vulnerability analyzer
Embed + Conv + MaxPool + Dense

@author: Kyle
"""

#import csv
#import pickle
#import base64
import numpy as np
#import random
#import requests
#import json
#import os
import random
import struct
import keras_metrics

from keras.backend import expand_dims
from keras.models import Sequential
from keras.layers import Embedding, Lambda, Conv2D, MaxPooling2D, Flatten, Dropout, Dense
#from keras.utils import to_categorical
#from keras.models import load_model

def shuffle(u, v):
    combined = list(zip(u, v))
    random.shuffle(combined)
    return zip(*combined)

def readDath(fileName):
    X, Y = [], []
#    i = 0
    # load data
    with open(fileName, "rb") as f:
        line = f.read(1003)
        while len(line):
#            print(line[0])
            if not line[0]:
                Y.append([1, 0])
            else:
                Y.append([0, 1])
#                i += 1
                
#            print(len(line[2: -1]))
            X.append(list(struct.unpack('h' * 500, line[2: -1])))
            line = f.read(1003)
            
#    print(i)
    X, Y = shuffle(X, Y)
    return np.array(X), np.array(Y)

def readDatb(fileName):
    X, Y = [], []
    # load data
    with open(fileName, "rb") as f:
        line = f.read(502)
        while len(line):
            if not line[0]:
                Y.append([1, 0])
            else:
                Y.append([0, 1])
                
        X.append(list(struct.unpack('b' * 500, line[1: -1])))
        line = f.read(502)
        
    X, Y = shuffle(X, Y)
    return np.array(X), np.array(Y)
    
# set up datasets
# X_tr, Y_tr = readDath("./CVE119_train.tok")
# X_va, Y_va = readDath("./CVE119_val.tok")
# X_te, Y_te = readDath("./CVE119_test.tok")

# dataset format: features: tokenset []  label: VULN (T / F)
xmax = 1 << 12
# l = 500
# k = 13
# m = 9

# model = Sequential()
# model.add(Embedding(xmax, k, input_length = l))
# model.add(Lambda(lambda x: expand_dims(x, 3)))
# model.add(Conv2D(512, (m, k), activation = "relu"))
# model.add(MaxPooling2D(pool_size = (l - m + 1, 1)))
# model.add(Flatten())
# model.add(Dropout(0.5))
# model.add(Dense(64, activation = "relu"))
# model.add(Dense(16, activation = "relu"))
# model.add(Dense(2, activation = "softmax"))
# model.summary()

# model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = [keras_metrics.binary_precision(), keras_metrics.binary_recall()])
# model.fit(X_tr, Y_tr, validation_data = (X_va, Y_va), epochs = 10)
# EVAL = model.evaluate(X_te, Y_te)
# PRED = model.predict(np.array([X_te[0]]))

class VulnDetect:
    def __init__(self, model_file=None, weights_file=None):
        self.model_file = model_file
        self.weights_file = weights_file
        self.l = 500
        self.k = 13
        self.m = 9

        self.model = None
        # See if there is a given model and weights file
        if self.model_file is not None:
            json_file = open(self.model_file, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            self.model = model_from_json(loaded_model_json)

            if self.weights in not None:
                self.model.load_weights(weights_file)

        else:
            self.model = Sequential()
            self.model.add(Embedding(xmax, k, input_length = l))
            self.model.add(Lambda(lambda x: expand_dims(x, 3)))
            self.model.add(Conv2D(512, (m, k), activation = "relu"))
            self.model.add(MaxPooling2D(pool_size = (l - m + 1, 1)))
            self.model.add(Flatten())
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation = "relu"))
            self.model.add(Dense(16, activation = "relu"))
            self.model.add(Dense(2, activation = "softmax"))

        # Print out the model and compile it
        self.model.summary()
        self.model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = [keras_metrics.binary_precision(), keras_metrics.binary_recall()])

    def train(self):
        # set up datasets
        X_tr, Y_tr = readDath("./CVE119_train.tok")
        X_va, Y_va = readDath("./CVE119_val.tok")
        model.fit(X_tr, Y_tr, validation_data = (X_va, Y_va), epochs = 10)
        # serialize model to JSON
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")

    def test(self):
        X_te, Y_te = readDath("./CVE119_test.tok")
        EVAL = model.evaluate(X_te, Y_te)

    def predict(self, code):
        return model.predict(np.array([code]))



