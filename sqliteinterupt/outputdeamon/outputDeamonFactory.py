#class outputDeamonFactory
from outputDeamonClient import outputDeamonClient
from outputDeamonServer import outputDeamonServer
from outputDeamonUDPClient import outputDeamonClientUDP


class outputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getoutputDeamon(self,type,protocol="tcp"):
        if(type=="client" and protocol=="tcp"):
            return outputDeamonClient()
        elif(type=="server" and protocol=="tcp"):
            return outputDeamonServer()
        elif (type == "client" and protocol == "udp"):
            return outputDeamonClientUDP()
