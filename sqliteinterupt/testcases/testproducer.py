import os
import sys
import random

path = "/home/nrv/PycharmProjects/listnerconnector/outpipe"
while(1):
    fifo = open(path,'w')

    fifo.write(""+str(random.random()))
    fifo.close()

