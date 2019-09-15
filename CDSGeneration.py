
from pwn import *
import struct
import os

sourceFileDir = "./CDatas"
with open("./CTokens.tok", "wb") as g:
    for f in os.listdir(sourceFileDir):
        p = process("tokenizer " + '/'.join([sourceFileDir, f]), shell = True)
        s = p.readline().strip().split()
        g.write(b''.join([struct.pack('h', int(i)) for i in s]) + b'\n')
