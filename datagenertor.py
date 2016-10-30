#mkfifo pipeline
#ls -l > pipeline


import os, time, sys
pipe_name = 'pipeline'

def child( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        time.sleep(1)
        os.write(pipeout, str(counter)+"\n")
        print "datagened Number :- "+str(counter)
        counter = (counter+1)


if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
child();














# def parent( ):
#     pipein = open(pipe_name, 'r')
#     while True:
#         line = pipein.readline()[:-1]
#         print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))
