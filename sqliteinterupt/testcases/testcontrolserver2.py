import os
import socket
import json
import threading
import time
import hashlib

import sys


def handleserver(conn,addr):
    id = str(conn.recv(1024));
    print addr, "   id ", id
    print 'Connection address:', addr
    print >> sys.stderr, addr
    md5val=0;
    while(True):
        fo = open("configchange.json", "r")
        msg=fo.read()
        if(len(msg)<5):
            continue
        m = hashlib.md5()
        m.update(msg)
        mval=m.digest()
        if(md5val!=mval):
            jsonread=json.loads(msg)
            if(id=="togen"):
                msgtosend=jsonread["togen"]
                conn.send(json.dumps(msgtosend))  # echo
            if (id == "tosecond"):
                msgtosend = jsonread["tosecond"]
                conn.send(json.dumps(msgtosend))  # echo
            if (id == "tothird"):
                msgtosend = jsonread["tothird"]
                conn.send(json.dumps(msgtosend))  # echo

        if(md5val==0):
            md5val=mval
        time.sleep(5)
    conn.close()



    #print 'Connection address:', addr
    # #while 1:
    #     #data = conn.recv(BUFFER_SIZE)
    #     #if not data: break
    #     #print "received data:", data
    #
    # data={}
    # data['inpdeamon']={"ip":"127.0.0.1","port":8050,"name":'inpdeamon',"type":"client","protocol":"tcp"}
    # data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
    # data["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
    #
    # data["timestamp"]="2016-10-07"
    # data["fromip"]="127.0.0.1"
    # data["sysid"]=1500
    # data["sysname"]="control1"
    # data["sysname"]="control1"
    # data["programproperties"]="-p 100 -q 1000"
    # data["deviceproperties"]="-p 1500 -q 150"
    # print json.dumps(data)
    # time.sleep(30)
    # conn.send(json.dumps(data))  # echo
    #
    # data["cntrldeamon"]["port"]=8080

    #conn.send(json.dumps(data))  # echo
    #conn.close()


TCP_IP = ''
TCP_PORT = 8080
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

threadlist={}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while(1):
    conn, addr = s.accept()


    newpid = os.fork()
    if newpid == 0:
        handleserver(conn,addr)
        exit(0)
    else:
        pass
    #t = threading.Thread(target=handleserver,args=(conn,addr,id,))
    #threadlist[id]=t


