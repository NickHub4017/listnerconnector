import os
class inputHandler:
    def __init__(self,inppipename="inppipe"):
        self.pipename="/home/nrv/PycharmProjects/listnerconnector/"+inppipename
        #print self.pipename
        try:
            #print "init"
            os.mkfifo(self.pipename)#ToDo make this common folder
        except:
            print "pipe exsists"


    def writedata(self,msg):
        #print self.pipeout
        try:
            #print msg, "wait for pipout"
            self.pipeout = open(self.pipename, 'w')
            self.pipeout.write(msg)
            self.pipeout.close()
        except Exception as e:
            print e

