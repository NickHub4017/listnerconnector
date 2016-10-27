
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
            while (1):
                inputmessage = str(self.socket.recv(self.buffersize))
                self.handler = inputHandler()
                print "---"
                self.handler.writedata(inputmessage)
        else:
            print "Sorry input deamon socket has an error"

    def disconnect(self):
        if (self.socket is not None):
            self.socket.close()
            self.socket = None

