import json

fo = open("configchange.json", "w")

fulldata={}
data={}
data['inpdeamon']={"ip":"127.0.0.1","port":8050,"name":'inpdeamon',"type":"server","protocol":"tcp"}
data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"server","protocol":"tcp"}
data["cntrldeamon"]={"ip":"192.168.1.3","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
data["timestamp"]="2016-10-07"
data["fromip"]="127.0.0.1"
data["sysid"]=1500
data["sysname"]="control1"
data["sysname"]="control1"
data["programproperties"]="-p 100 -q 1000"
data["deviceproperties"]="-p 1500 -q 150"
fulldata["togen"]=data
inp=raw_input("Type:- ")
if(inp=="abc"):
    datab=data
    datab['inpdeamon'] = {"ip": "192.168.1.3", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "tcp"}
    datab["oupdeamon"] = {"ip": "192.168.1.3", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "tcp"}
    fulldata["tosecond"] = datab
    datac = data
    datac['inpdeamon'] = {"ip": "192.168.1.7", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "tcp"}
    datac["oupdeamon"] = {"ip": "192.168.1.6", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "tcp"}
    fulldata["tothird"] = datac

    fo.write(json.dumps({"tothird": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.6", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.7", "type": "client", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}, "tosecond": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.7", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.3", "type": "client", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}, "togen": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.3", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.3", "type": "server", "port": 8050, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}}))

if(inp=="acb"):
    datab = data
    datab['inpdeamon'] = {"ip": "192.168.1.6", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "tcp"}
    datab["oupdeamon"] = {"ip": "192.168.1.7", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "tcp"}
    fulldata["tosecond"] = datab
    datac = data
    datac['inpdeamon'] = {"ip": "192.168.1.3", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "tcp"}
    datac["oupdeamon"] = {"ip": "192.168.1.3", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "tcp"}
    fulldata["tothird"] = datac
    fo.write(json.dumps({"tothird": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.6", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.3", "type": "client", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}, "tosecond": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.7", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.6", "type": "client", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}, "togen": {"sysname": "control1", "cntrldeamon": {"ip": "192.168.1.3", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "oupdeamon": {"ip": "192.168.1.3", "type": "server", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "fromip": "127.0.0.1", "sysid": 1500, "inpdeamon": {"ip": "192.168.1.3", "type": "server", "port": 8050, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "deviceproperties": "-p 1500 -q 150"}}))

fo.close()