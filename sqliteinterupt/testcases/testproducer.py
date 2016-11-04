import os
import sys
import random
import time

path = "/home/nrv/PycharmProjects/listnerconnector/outpipe"
while(1):
    fifo = open(path,'w')
    time.sleep(2)
    fifo.write(""+str(random.random()))
    fifo.close()

