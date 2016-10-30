import os
class inputHandler:
    def __init__(self,inppipename="inppipe"):
        self.pipename=inppipename
        self.pipeout = os.open(self.pipename, os.O_WRONLY)

    def writedata(self,msg):
        os.write(self.pipeout, msg)

