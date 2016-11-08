##Client Receiving


import socket
import logging
from inputHandler import inputHandler
logging.basicConfig(filename='inputdeamonclientudp.log',level=logging.DEBUG)

class inputDeamonClientUDP:
    def __init__(self,ipinp="127.0.0.1",portinp=9090):
        self.ip=ipinp
        self.port=portinp
        self.buffersize=1024
        self.server_address = (self.ip,self.port)
        logging.debug('input client udp init with ip port buffer'+str(ipinp)+' '+str(portinp)+' '+str(self.buffersize))
    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.settimeout(5)
            self.server_address = (self.ip, self.port)
            logging.debug('input client udp connect (TRY) with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
            return True
        except:
            logging.debug(
                'input client udp connect (EXCEPT) with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
            return False

    def getconnection(self,ipinp,portinp):
        self.ip = ipinp
        self.port = portinp
        logging.debug('input client udp getconnection with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
        return self;

    def getdata(self):
        self.sock.sendto("sending", self.server_address)

        logging.debug(
            'input client udp getdata with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
        if (self.sock is not None):
            currentstr = ""
            # isbegin=False
            logging.debug(
                'input client udp getdata socket is not NONE with ip port buffer')
            self.handler = inputHandler()
            errorcount=0
            while (1):
                try:
                    logging.debug('input client udp getdata first while loop')
                    data, server = self.sock.recvfrom(4096)
                    self.handler.writedata(data)
                except Exception as a:
                    logging.debug('input client udp getdata first while loop (EXCEPT) :- '+a.message)
                    print a," error"
                    #self.sock.close()
                    break
        else:
            logging.debug('Demon socket has error')
            print "Sorry input deamon udp socket has an error"

    def disconnect(self):
        logging.debug('Disconnecting')
        if (self.sock is not None):
            self.sock.close()
            self.sock = None

