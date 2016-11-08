from inputDeamonClient import inputDeamonClient
from inputDeamonServer import inputDeamonServer
from inputDeamonUDPServer import inputDeamonUDPServer
from inputDeamonUDPClient import inputDeamonClientUDP
class inputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getinputDeamon(self,type,protocol="tcp"):
        if(type=="client" and protocol=="tcp"):
            return inputDeamonClient()
        elif(type=="server" and protocol=="tcp"):
            return inputDeamonServer()
        elif (type == "server" and protocol == "udp"):
            return inputDeamonUDPServer()
        elif (type == "client" and protocol == "udp"):
            return inputDeamonClientUDP()