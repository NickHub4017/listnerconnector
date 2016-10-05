from DeamonClient import DeamonClient
from DeamonServer import DeamonServer

class DeamonLinkFactory:

    def __init__(self,type):
        print type
        self.type=type

    def getConnection(self,port,ip):
        if(self.type=="server"):
            return DeamonServer(ip, port) #ToDo implement Deamon Server
        elif(self.type=="client"):
            return DeamonClient(ip, port)

