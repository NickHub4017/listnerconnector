import os
class inputHandler:
    def __init__(self,inppipename="inppipe"):
        self.pipename="/tmp/"+inppipename
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
            print msg
            self.pipeout.write(msg)
            self.pipeout.close()
        except Exception as e:
            print e

