import os
class outputHandler:
    def __init__(self,outpipename="outpipe"):
        self.pipename="/home/nrv/PycharmProjects/listnerconnector/"+outpipename
        #print self.pipename
        try:
            #print "init"
            os.mkfifo(self.pipename)#ToDo make this common folder
        except:
            print "pipe exsists"


    def readdatapipe(self):
        #print self.pipeout
        try:
            #print msg, "wait for pipout"
            self.pipeout = open(self.pipename, 'r')
            msg=self.pipeout.read()
            self.pipeout.close()
            return msg;
        except Exception as e:
            print e

