#class outputDeamonFactory
from outputDeamonClient import outputDeamonClient


class outputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getoutputDeamon(self,type):
        if(type=="client"):
            return outputDeamonClient()
        elif(type=="server"):
            return None #inputDeamonServer()
