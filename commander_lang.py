
import socket
import sys
import time
import xml.etree.ElementTree as ET
import hashlib



def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def makeconn(addr,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (addr, port)
    print >> sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    return sock;

#prevmd5=md5("Language/src/server.xml");
prevmd5=0

while True:
    
    try:
        newmd5 = md5("Language/src/server.xml");
        if (prevmd5 != newmd5):
            prevmd5 = newmd5;
            tree = ET.parse('Language/src/server.xml')
            root = tree.getroot()
            cmd=root[1][1].text+"z"
            print cmd
            sock = makeconn('localhost', 8502)
            #cmd=raw_input("Enter server,ipz :- ")
            sock.sendall(cmd)
            sock.close()
    except:
        #print "-"
	prevmd5=prevmd5
	
