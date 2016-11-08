#!/usr/bin/python
# import os
import sys

path = "/tmp/inppipe"

while(True):
    fifo = open(path, "r")
    print fifo.read()
    fifo.close()