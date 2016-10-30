import random
import socket
import json
import time

import signal
import os
#
# def sigint_handler(signum, frame):
#     p = os.system('echo %s|sudo -S %s' % ('ua741', 'tcpkill ip host 127.0.0.1 port 8050'))
#     print 'Stop pressing the CTRL+C!'
#
# signal.signal(signal.SIGINT, sigint_handler)

TCP_IP = '127.0.0.1'
TCP_PORT = 8050
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while(1):
    conn, addr = s.accept()
    print 'Connection address:', addr
    #while 1:
        #data = conn.recv(BUFFER_SIZE)
        #if not data: break
        #print "received data:", data
    data={}

    while(1):
    #while()
        data["audio"] = random.random()
        time.sleep(1)
        conn.send(json.dumps(data))  # echo
    conn.close()
