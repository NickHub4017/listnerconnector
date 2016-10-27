

from inputDeamonFactory import inputDeamonFactory

import time
import sys
import os
sys.path.append(os.path.abspath('../'))


from initdb import initdbclass


currentDb=initdbclass()
factory=inputDeamonFactory()


while(1):
    isclient=True
    datarow=currentDb.getnodedata("inpdeamon")
    inpip=datarow[2]
    inpport=datarow[3]
    type=datarow[4]
    print inpip," ",inpport," ",type
    if(type=="client"):
        inputdeamon = factory.getinputDeamon("client").getconnection(inpip,inpport)

        while(not inputdeamon.connect()):
            time.sleep(2)
            print "Input Link Connection error occured"
        try:
            inputdeamon.getdata()
        except Exception,e:
            #print "Control Server Link gone ",e
            inputdeamon.disconnect()

