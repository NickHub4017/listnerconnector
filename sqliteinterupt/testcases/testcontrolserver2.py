
import socket
import json
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 8070
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
    data['inpdeamon']={"ip":"127.0.0.1","port":8090,"name":'inpdeamon',"type":"client","protocol":"tcp"}
    data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
    data["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}

    data["timestamp"]="2016-10-07"
    data["fromip"]="127.0.0.1"
    data["sysid"]=1500
    data["sysname"]="control1"
    data["sysname"]="control1"
    data["programproperties"]="-p 100 -q 1000"
    data["deviceproperties"]="-p 1500 -q 150"
    print data['inpdeamon']
    conn.send(json.dumps(data))  # echo
    time.sleep(10)
    data["cntrldeamon"]["port"]=8080
    conn.send(json.dumps(data))  # echo
    #conn.close()
