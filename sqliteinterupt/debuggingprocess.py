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


def controldeamon(pipename):
    print "Control deamon Created"
    currentDb.updatecontrolpid(os.getgid())
    # print('Hello from parent', os.getpid(), newinputpid)
    while (1):  ##For get the data from control
        # inputthread=DeamonThreads(1)
        isclient = True
        datarow = currentDb.getnodedata("cntrldeamon")
        controlip = datarow[2]
        controlport = datarow[3]
        type = datarow[4]
        if (type == "client"):
            controllink = DeamonLinkFactory("client").getConnection(controlip, controlport)
            while (not controllink.connect()):
                time.sleep(2)
                print "Control Link Connection error occured"
            try:
                # inputthread.start()
                msgls=controllink.getdata()  # This will return only an error occurs in control stream OR UPDATE HAPPENS
                print  "get data returened ",os.getpid()
                time.sleep(1)
                msg=""
                for q in msgls:
                    if q:
                        msg=msg+"T"
                    else:
                        msg = msg + "F"
                pipeout = open(pipename, 'w')
                pipeout.write(msg)
                pipeout.close()
                #os.kill(newinputpid)
                #os.kill(newoutputpid)
                break;
            except Exception as e:
                print "Control Server Link gone ",e.message
                controllink.disconnect()


#initiateprocess()

def createinputDeamon():
    newinputpid = os.fork()
    if newinputpid == 0:
        inputmainlink()
        return False
    else:
        return True  #To Check is this the parent
print "----*----"
#inputthread=None
control_pipe_name="controlnamepipe"
if not os.path.exists(control_pipe_name):
    os.mkfifo(control_pipe_name)


while(1):
    print "loop terminated"

    newinputpid = os.fork()
    currentDb.updateinputpid(newinputpid)
    if newinputpid == 0:
        inputmainlink()

    else:
        newoutputpid = os.fork()
        currentDb.updateoutputpid(newoutputpid)
        if newoutputpid == 0:
            #outputmainlink()
            print "output"
            while(True):
                x=1
        else:
            newcontrolpid = os.fork()
            currentDb.updatecontrolpid(newcontrolpid)
            if newcontrolpid == 0:
                #controldeamon(control_pipe_name)
                print "control"
                while (True):
                    x = 1
            else:
                while(True):
                    continue;
                    #print "in Main loop"
                    pipein = open(control_pipe_name, 'r')
                    line = pipein.read()
                    if line!="":
                        print line,"-- is received from the control"
                        if(line[0]=="T"):
                            os.kill(newinputpid,9)
                            newinputpid = os.fork()
                            currentDb.updateinputpid(newinputpid)
                            if newinputpid == 0:
                                inputmainlink()
                        if (line[1] == "T"):
                            os.kill(newoutputpid, 9)
                            newoutputpid = os.fork()
                            currentDb.updateoutputpid(newoutputpid)
                            if newoutputpid == 0:
                                outputmainlink()
                        if (line[2] == "T"):
                            print "Control daemon PID ",newcontrolpid
                            os.kill(newcontrolpid, 9)
                            newcontrolpid = os.fork()
                            currentDb.updatecontrolpid(newcontrolpid)
                            if newcontrolpid == 0:
                                controldeamon(control_pipe_name)
                    pipein.close()
                    time.sleep(1)








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


