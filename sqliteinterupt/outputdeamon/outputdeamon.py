#ToDo add ping thread
from outputDeamonFactory import outputDeamonFactory

import time
import sys
import os
sys.path.append(os.path.abspath('../'))


from initdb import initdbclass


currentDb=initdbclass()
factory=outputDeamonFactory()  #ToDo
currentDb.updateoutputpid(os.getgid())
def outputmainlink():#ToDo
    while(1):
        isclient=True
        datarow=currentDb.getnodedata("oudeamon")#ToDo
        outpip=datarow[2]#ToDo
        outpport=datarow[3]#ToDo
        type=datarow[4]
        print outpip," ",outpport," ",type#ToDo
        if(type=="client"):
            outputdeamon = factory.getoutputDeamon("client").getconnection(outpip,outpport)#ToDo

            while(not outputdeamon.connect()):#ToDo
                time.sleep(2)
                print "output Link Connection error occured"
            try:
                outputdeamon.senddata()#ToDo
                print "outclient"
            except Exception,e:
                print "output Server Link gone ",e
                outputdeamon.disconnect()#ToDo

        elif(type=="server"):
            try:
                outputdeamon=factory.getoutputDeamon("server").getconnection(outpip,outpport)#ToDo
                outputdeamon.serve()#ToDo
            except Exception as e:
                print e


outputmainlink()