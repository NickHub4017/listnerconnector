from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass
import time
import os

import threading
import inputdeamon
from inputdeamon.inputDeamon import inputmainlink
from outputdeamon.outputdeamon import outputmainlink

# class DeamonThreads(threading.Thread):
#      def __init__(self,inptype):
#          super(DeamonThreads, self).__init__()
#          self.deamonthreadtype=inptype
#      def run(self):
#          if(self.deamonthreadtype==1):
#             inputmainlink()

currentDb=initdbclass()

def initiateprocess():
    controlpid=currentDb.getcontrolpid()
    inputpid=currentDb.getinputpid()
    outputpid=currentDb.getoutputpid()
    try:
        os.kill(int(controlpid),9)
    except Exception as e:
        print "Kill Failed @ control ",e
    try:
        os.kill(int(inputpid), 9)
    except Exception as e:
        print "Kill Failed @ input " , e
    try:
        os.kill(int(outputpid), 9)
    except Exception as e:
        print "Kill Failed @ output " , e


initiateprocess()

print "----*----"
#inputthread=None
currentDb.updatecontrolpid(os.getgid())
while(1):
    print "loop terminated"

    newinputpid = os.fork()
    if newinputpid == 0:
        inputmainlink()
    else:
        newoutputpid = os.fork()
        if newoutputpid == 0:
            outputmainlink()
        else:
            #print('Hello from parent', os.getpid(), newinputpid)
            while(1):##For get the data from control
                #inputthread=DeamonThreads(1)
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
                        #inputthread.start()
                        controllink.getdata()  #This will return only an error occurs in control stream OR UPDATE HAPPENS
                        print "get data returened"
                        time.sleep(1)
                        os.kill(newinputpid)
                        os.kill(newoutputpid)
                        break;
                    except Exception,e:
                        #print "Control Server Link gone ",e
                        controllink.disconnect()

def child():
    for i in range(0,50):
        time.sleep(1)
        print('Hello from child', os.getpid())

    #print os.execl("python","-al")
    os._exit(0) # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            for i in range(0, 50):
                time.sleep(1.2)
                #print('Hello from child', os.getpid())
                print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break


