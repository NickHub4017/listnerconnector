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

    fifoout = open(outpath, 'w')
    fifoin= open(inpath, 'r')
    msg=fifoin.read()
    fifoin.close()
    fifoout.write(msg+"100")
    fifoout.close()

