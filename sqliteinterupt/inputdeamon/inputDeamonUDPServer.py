import random
import socket
import json
import time
from inputHandler import inputHandler
import signal
import os
#
# def sigint_handler(signum, frame):
#     p = os.system('echo %s|sudo -S %s' % ('ua741', 'tcpkill ip host 127.0.0.1 port 8050'))
#     print 'Stop pressing the CTRL+C!'
#
# signal.signal(signal.SIGINT, sigint_handler)




class inputDeamonUDPServer:
    def __init__(self, ipinp="127.0.0.1", portinp=9090):
        self.ip = ''
        self.port = portinp
        self.buffersize = 1024
        self.sock=None
        self.server_address = (self.ip, self.port)

    def getconnection(self, ipinp, portinp):
        self.ip = ''
        self.port = portinp
        self.server_address = (self.ip, self.port)
        return self;
    def serve(self):
        self.sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)
        #s.listen(1) #ToDo enable if want
        self.handler = inputHandler()
        while(1):
            try:
                data, address = self.sock.recvfrom(1024)
                self.handler.writedata(data)
            except Exception as e:
                #if(s.)
                print "Msg is ",e
                break
