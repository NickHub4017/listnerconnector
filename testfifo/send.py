import json
import os

data={}
data['inpdeamon']={"ip":"127.0.0.1","port":8050,"name":'inpdeamon',"type":"client","protocol":"tcp"}
data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
data["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}

data["timestamp"]="2016-10-07"
data["fromip"]="127.0.0.1"
data["sysid"]=1500
data["sysname"]="control1"
data["sysname"]="control1"
data["programproperties"]="-p 100 -q 1000"
data["deviceproperties"]="-p 1500 -q 150"
print json.dumps(data)


path = "program2.fifo"
try:
    os.mkfifo(path)
except:
    print "file is exsist"

fifo = open(path, 'w')
for i in range(0,1500000):
    print "send",str(i)
    fifo.write("Message from the sender!\n")
#fifo.close()
