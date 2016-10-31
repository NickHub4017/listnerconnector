from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass
import time
import os

import threading
import inputdeamon
from inputdeamon.inputDeamon import inputmainlink

# class DeamonThreads(threading.Thread):
#      def __init__(self,inptype):
#          super(DeamonThreads, self).__init__()
#          self.deamonthreadtype=inptype
#      def run(self):
#          if(self.deamonthreadtype==1):
#             inputmainlink()



currentDb=initdbclass()
print "----*----"
#inputthread=None
while(1):
    print "loop terminated"

    newinputpid = os.fork()
    if newinputpid == 0:
        inputmainlink()
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
                    controllink.getdata()
                    print "get data returened"
                    time.sleep(1)
                    os.kill(newinputpid)
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

