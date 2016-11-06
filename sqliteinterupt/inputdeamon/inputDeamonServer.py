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




class inputDeamonServer:
    def __init__(self, ipinp="127.0.0.1", portinp=9090):
        self.ip = ''
        self.port = portinp
        self.buffersize = 1024
        self.socket=None

    def getconnection(self, ipinp, portinp):
        self.ip = ipinp
        self.port = portinp
        return self;
    def serve(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(1)

        while(1):
            try:
                conn, addr = s.accept()
                print 'Connection address:', addr
                #while(1):
                if (True):
                    currentstr = ""
                    # isbegin=False
                    #break
                    self.handler = inputHandler()
                    while (1):
                        try:
                            print "wait for recv"
                            inputmessage = str(conn.recv(self.buffersize))  ##Check is it must be conn?
                            if (not inputmessage):
                                break
                            #print inputmessage
                            self.handler.writedata(inputmessage)
                        except Exception as a:
                            print a, " error"
                            #self.socket.close()
                            break
                else:
                    print "Sorry input deamon socket has an error"


            except Exception as e:
                #if(s.)
                print "Msg is ",e
                break
