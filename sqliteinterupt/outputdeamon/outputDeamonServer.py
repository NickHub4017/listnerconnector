import logging
import random
import socket
import json
import time
import sys
import signal
import os
from outputHandler import outputHandler
#
# def sigint_handler(signum, frame):
#     p = os.system('echo %s|sudo -S %s' % ('ua741', 'tcpkill ip host 127.0.0.1 port 8050'))
#     print 'Stop pressing the CTRL+C!'
#
# signal.signal(signal.SIGINT, sigint_handler)

logging.basicConfig(filename='outputserver.log',level=logging.DEBUG)


class outputDeamonServer:
    def __init__(self, ipout="127.0.0.1", portout=9090):
        self.ip = ''
        self.port = portout
        self.buffersize = 1024
        self.socket=None
        logging.debug(
            '27 output server client init with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))

    def getconnection(self, ipout, portout):
        self.ip = ''
        self.port = portout
        logging.debug(
            '33 output server get connection with ip port buffer' + str(self.ip) + ' ' + str(self.port) + ' ' + str(self.buffersize))

        return self;
    def serve(self):
        logging.debug('37 output server serve with ip port buffer')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(1)
        self.socket =s
        while(1):
            logging.debug('44 output server serve first while loop')
            try:
                logging.debug('46 output server serve first while loop (TRY)')
                try:
                    logging.debug('48 output server serve first while loop (TRY/TRY)')
                    conn, addr = s.accept()
                except Exception as e:
                    print "@ accept",e
                    logging.debug('52 output server serve first while loop (TRY/EXCEPT)'+e.message)
                    s.shutdown()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind((self.ip, self.port))
                    s.listen(1)
                    self.socket = s
                print 'Connection address outputdeamon server:', addr
                logging.debug('59 output server serve first while loop (TRY) '+addr)
                #while(1):
                print "in main Loop"
                if (self.socket is not None):# ToDO Remove this if or refactor
                    currentstr = ""
                    # isbegin=False
                    #break
                    logging.debug('66 output server serve first while loop (TRY) Socket not None')
                    self.handler = outputHandler()
                    while (1):
                        logging.debug('69 output server serve first while loop (TRY) Socket not None While')
                        try:
                            logging.debug('71 output server serve first while loop (TRY) Socket not None While (TRY)')
                            msg = self.handler.readdatapipe()
                            conn.send(msg)
                            #time.sleep(1)
                            print "send Done"
                        except Exception as a:
                            print a, " error"
                            logging.debug('78 output server serve first while loop (TRY) Socket not None While (EXCEPT) '+a.message)
                            conn.close()
                            break
                else:
                    logging.debug('82 output server serve first while loop (TRY) Socket is None')
                    print "Sorry input deamon socket has an error"


            except Exception as e:
                #if(s.)
                print e
                exc_type, exc_obj, exc_tb = sys.exc_info()
                logging.debug('89 output server serve first while loop (EXCEPT) '+str(e.message)+' '+exc_tb.tb_lineno)
                time.sleep(5)
                break
