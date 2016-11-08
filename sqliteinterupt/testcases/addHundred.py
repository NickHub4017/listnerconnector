#!/usr/bin/python

import random
import os
import time

while True:
    inpath = "/tmp/inppipe"
    outpath="/tmp/outpipe"
    try:
        os.mkfifo(inpath)
    except:
        print "file is exsist"
    try:
        os.mkfifo(outpath)
    except:
        print "file is exsist"

    print "Wait for fifo read"
    fifoin= open(inpath, 'r')
    msg=fifoin.read()
    fifoin.close()
    print msg
    fifoout = open(outpath, 'w')
    fifoout.write(msg+"100")
    fifoout.close()

