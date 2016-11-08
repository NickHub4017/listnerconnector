##Client Receiving


import socket
from outputHandler import outputHandler

class outputDeamonClientUDP:
    def __init__(self,ipout="127.0.0.1",portout=9090):
        self.ip=ipout
        self.port=portout
        self.buffersize=1024
        self.server_address = (self.ip, self.port)
    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #self.socket.settimeout(5)  #ToDo enable timeout
            #self.socket.connect((self.ip, self.port))
            return True
        except:
            return False

    def getconnection(self,ipout,portout):
        self.ip = ipout
        self.port = portout
        self.server_address = (self.ip, self.port)
        return self;

    def senddata(self):
        if (self.sock is not None):
            currentstr = ""
            # isbegin=False
            self.handler = outputHandler()
            while (1):
                try:
                    #print "wait for send"
                    msg=self.handler.readdatapipe()
                    self.sock.sendto(msg,self.server_address)
                except Exception as a:
                    print a," error"
                    break
        else:
            print "Sorry output deamon socket has an error"

    def disconnect(self):
        if (self.sock is not None):
            #self.socket.close()
            self.sock = None

