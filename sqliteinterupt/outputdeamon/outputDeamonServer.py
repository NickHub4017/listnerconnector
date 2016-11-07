import random
import socket
import json
import time

import signal
import os
from outputHandler import outputHandler
#
# def sigint_handler(signum, frame):
#     p = os.system('echo %s|sudo -S %s' % ('ua741', 'tcpkill ip host 127.0.0.1 port 8050'))
#     print 'Stop pressing the CTRL+C!'
#
# signal.signal(signal.SIGINT, sigint_handler)




class outputDeamonServer:
    def __init__(self, ipout="127.0.0.1", portout=9090):
        self.ip = ''
        self.port = portout
        self.buffersize = 1024
        self.socket=None

    def getconnection(self, ipout, portout):
        self.ip = ''
        self.port = portout
        return self;
    def serve(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(1)
        self.socket =s
        while(1):
            try:
                try:
                    conn, addr = s.accept()
                except Exception as e:
                    print "@ accept",e
                    s.shutdown()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind((self.ip, self.port))
                    s.listen(1)
                    self.socket = s
                print 'Connection address outputdeamon server:', addr
                #while(1):
                print "in main Loop"
                if (self.socket is not None):# ToDO Remove this if or refactor
                    currentstr = ""
                    # isbegin=False
                    #break
                    self.handler = outputHandler()
                    while (1):
                        try:
                            msg = self.handler.readdatapipe()
                            conn.send(msg)
                            time.sleep(1)
                            print "send Done"
                        except Exception as a:
                            print a, " error"
                            conn.close()
                            break
                else:
                    print "Sorry input deamon socket has an error"


            except Exception as e:
                #if(s.)
                print e
                break
