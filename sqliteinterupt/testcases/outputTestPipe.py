#!/usr/bin/python
# import os
import sys

path = "/tmp/outpipe"

while(True):
    fifo = open(path, "r")
    print fifo.read()
    fifo.close()