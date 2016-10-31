from inputDeamonClient import inputDeamonClient
from inputDeamonServer import inputDeamonServer
class inputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getinputDeamon(self,type):
        if(type=="client"):
            return inputDeamonClient()
        elif(type=="server"):
            return inputDeamonServer()
