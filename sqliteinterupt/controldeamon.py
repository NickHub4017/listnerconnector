from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass
import time


currentDb=initdbclass()
while(1):
    isclient=True
    datarow=currentDb.getnodedata("cntrldeamon")
    controlip=datarow[2]
    controlport=datarow[3]
    type=datarow[4]
    if(type=="client"):
        controllink=DeamonLinkFactory("client").getConnection(controlip,controlport)
        while(not controllink.connect()):
            time.sleep(2)
            print "Control Link Connection error occured"
        try:
            controllink.getdata()
        except Exception,e:
            #print "Control Server Link gone ",e
            controllink.disconnect()

