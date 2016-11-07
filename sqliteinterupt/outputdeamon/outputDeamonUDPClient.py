##Client Receiving


import socket
from outputHandler import outputHandler

class outputDeamonClientUDP:
    def __init__(self,ipout="127.0.0.1",portout=9090):
        self.ip=ipout
        self.port=portout
        self.buffersize=1024
    def connect(self):
        try:
            self.socket = socket.socket()
            self.socket.settimeout(5)
            self.socket.connect((self.ip, self.port))
            return True
        except:
            return False

    def getconnection(self,ipout,portout):
        self.ip = ipout
        self.port = portout
        return self;

    def senddata(self):
        if (self.socket is not None):
            currentstr = ""
            # isbegin=False
            self.handler = outputHandler()
            while (1):
                try:
                    #print "wait for send"
                    msg=self.handler.readdatapipe()
                    self.socket.send(msg)
                except Exception as a:
                    print a," error"
                    self.socket.close()
                    break
        else:
            print "Sorry output deamon socket has an error"

    def disconnect(self):
        if (self.socket is not None):
            #self.socket.close()
            self.socket = None

