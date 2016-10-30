##Client Receiving


import socket
from inputHandler import inputHandler
class inputDeamonClient:
    def __init__(self,ipinp="127.0.0.1",portinp=9090):
        self.ip=ipinp
        self.port=portinp
        self.buffersize=1024
    def connect(self):
        try:
            self.socket = socket.socket()
            self.socket.settimeout(5)
            self.socket.connect((self.ip, self.port))

            return True
        except:
            return False

    def getconnection(self,ipinp,portinp):
        self.ip = ipinp
        self.port = portinp
        return self;

    def getdata(self):
        if (self.socket is not None):
            currentstr = ""
            # isbegin=False

            self.handler = inputHandler()
            while (1):
                try:
                    print "wait for recv"
                    inputmessage = str(self.socket.recv(self.buffersize))
                    if(not inputmessage):
                        break

                    self.handler.writedata(inputmessage)
                except Exception as a:
                    print a," error"
                    self.socket.close()
                    break
        else:
            print "Sorry input deamon socket has an error"

    def disconnect(self):
        if (self.socket is not None):
            #self.socket.close()
            self.socket = None

