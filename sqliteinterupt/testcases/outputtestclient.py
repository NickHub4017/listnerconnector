#!/usr/bin/python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 8120
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
    while (True):
        try:
            print "Wait to receve"
            msg=s.recv(BUFFER_SIZE)
            print str(msg)

            #time.sleep(0.5)
        except Exception as E:
            print E
            break
    #data = s.recv(BUFFER_SIZE)
    s.close()
except Exception as E:
    print E.message

#print "received data:", data