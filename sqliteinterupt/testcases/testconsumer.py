import os
import sys

path = "/home/nrv/PycharmProjects/listnerconnector/inppipe"
while(1):
    fifo = open(path,'r')
    print "Open Done"
    print fifo.read()
    fifo.close()

