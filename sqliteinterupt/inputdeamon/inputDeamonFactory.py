from inputDeamonClient import inputDeamonClient
class inputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getinputDeamon(self,type):
        if(type=="client"):
            return inputDeamonClient()
        elif(type=="server"):
            return None #ToDo add inputDeamonServer
