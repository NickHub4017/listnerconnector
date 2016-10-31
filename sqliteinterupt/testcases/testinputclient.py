import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 8050
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(s.connect((TCP_IP, TCP_PORT))):
    while (True):
        s.send(MESSAGE)
        time.sleep(0.25)
    #data = s.recv(BUFFER_SIZE)
    s.close()

#print "received data:", data