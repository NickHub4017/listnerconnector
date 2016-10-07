import socket
from ControlHandler import ControlHandler
class DeamonClient:
    def __init__(self,inpport=1000,inpip="127.0.0.1"):
        print inpport," ",inpip
        self.port=int(inpport)
        self.ip=inpip
        self.socket=None
        self.buffersize=1024

    def connect(self):
        self.socket = socket.socket()
        self.socket.connect((self.ip, self.port))

    def getdata(self):
        if(self.socket is not None):
            currentstr=""
            #isbegin=False
            while(1):#ToDo remove onetime buffer read and add dynamic reading.
                self.controlmessage=str(self.socket.recv(self.buffersize))
                self.handler=ControlHandler()
                self.handler.insertcontrolmessage(self.controlmessage)




