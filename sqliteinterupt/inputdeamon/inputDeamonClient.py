##Client Receiving


import socket
import logging
from inputHandler import inputHandler
logging.basicConfig(filename='inputdeamonclient.log',level=logging.DEBUG)

class inputDeamonClient:
    def __init__(self,ipinp="127.0.0.1",portinp=9090):
        self.ip=ipinp
        self.port=portinp
        self.buffersize=1024
        logging.debug('input client init with ip port buffer'+str(ipinp)+' '+str(portinp)+' '+str(self.buffersize))
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            self.socket.connect((self.ip, self.port))
            logging.debug('input client connect (TRY) with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
            return True
        except Exception as e:
            logging.debug(
                'input client connect (EXCEPT) with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
            print e,"MSG ERR"
            return False

    def getconnection(self,ipinp,portinp):
        self.ip = ipinp
        self.port = portinp
        logging.debug('input client getconnection with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
        return self;

    def getdata(self):
        logging.debug(
            'input client getdata with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))
        if (self.socket is not None):
            currentstr = ""
            # isbegin=False
            logging.debug(
                'input client getdata socket is not NONE with ip port buffer')
            self.handler = inputHandler()
            errorcount=0
            while (1):
                logging.debug('input client getdata first while loop')
                try:
                    logging.debug('input client getdata first while loop (TRY)')
                    print "wait for recv input client"
                    errorcount=errorcount+1
                    inputmessage = str(self.socket.recv(self.buffersize))
                    if(not inputmessage):

                        if(errorcount>10000):
                            try:
                                logging.debug('input client getdata first while loop (not inputmessage) 10000 occured')
                                self.socket.send("Check")
                                errorcount=0
                                logging.debug('input client getdata first while loop (not inputmessage) (Try) send check')
                            except Exception as e:
                                print "Disconnected input deamon"
                                logging.debug(
                                    'input client getdata first while loop (not inputmessage) (Except) send check fail '+e.message)
                                break
                        continue

                    self.handler.writedata(inputmessage)

                except Exception as a:
                    logging.debug('input client getdata first while loop (EXCEPT) :- '+a.message)
                    print a," error"
                    #self.socket.close()
                    break
        else:
            logging.debug('Demon socket has error')
            print "Sorry input deamon socket has an error"

    def disconnect(self):
        logging.debug('Disconnecting')
        if (self.socket is not None):
            #self.socket.close()
            self.socket = None

