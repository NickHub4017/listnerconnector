import os

path = "program2.fifo"
try:
    os.mkfifo(path)
except:
    print "file is exsist"

fifo = open(path, 'w')
for i in range(0,150):
    print "send",str(i)
    fifo.write("Message from the sender!\n")
fifo.close()