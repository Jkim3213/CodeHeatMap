# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 06:31:09 2019

CLI Interface for Model Prediction

@author: Kyle
"""

from keras.models import load_model
import sys
import cvulnlexer
import numpy as np
from keras_metrics import *
import math

if __name__ == "__main__":
    # load the model
    model = load_model("./doesnotwork.h5")
    if len(sys.argv) != 1:
        print("Usage: python ./CodeHeat.py [C / C++ source file]")
        
    srcFile = open(sys.argv[0], 'r')
    mapp = cvulnlexer.TOK(srcFile.read())
    header = "Block\tLine Start\tPos Start\tP(vuln)"
    print(header)
    print('-' * math.floor(1.5 * len(header)))
    for i, (blockStart, iVec) in enumerate(mapp.items()):
        pdist = model.predict(np.array([iVec]))
#        print(f"{i + 1}\t{blockStart[0]}\t{blockStart[1]}\t{100 * pdist[0][0]}")
        print("%d\t%d\t\t%d\t\t%0.2f%%" % (i + 1, blockStart[0], blockStart[1], 100 * pdist[0][0]))