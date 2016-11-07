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


    for i in range(0, 150):
        fifo = open(outpath, 'w')
        print "send", str(i)
        fifo.write("Message from the sender! ")
        fifo.close()
        time.sleep(1)


