from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass
import time

currentDb=initdbclass()
while(1):
    controlip=currentDb.getdata("controlip")
    controlport=currentDb.getdata("controlport")
    controllink=DeamonLinkFactory("client").getConnection(controlip,controlport)
    while(not controllink.connect()):
        time.sleep(3)
        print "Control Link Connection error occured"
    try:
        controllink.getdata()
    except:
        print "Control Server Link gone"
    controllink.disconnect()

