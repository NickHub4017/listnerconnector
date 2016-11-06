import random
import os
import time

while True:
    inpath = "/home/nrv/PycharmProjects/listnerconnector/inppipe"
    outpath="/home/nrv/PycharmProjects/listnerconnector/outpipe"
    try:
        os.mkfifo(inpath)
    except:
        print "file is exsist"
    try:
        os.mkfifo(outpath)
    except:
        print "file is exsist"

    fifo = open(outpath, 'w')
    for i in range(0, 150):
        print "send", str(i)
        fifo.write("Message from the sender! ")
        time.sleep(1)
    fifo.close()

