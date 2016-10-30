import os
import sys

path = "program2.fifo"
fifo = open(path, "r")
for line in fifo:
    print "Received: " + line,
fifo.close()