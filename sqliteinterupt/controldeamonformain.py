#!/usr/bin/python
import sys

from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass
import time
import os

currentDb=initdbclass()


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
                print "Control Link Connection error occured" + " ip "+ str(controlip) + " port " + str(controlport)
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
                print "Control Server Link gone ",e
                controllink.disconnect()

controldeamon("/tmp/controlpipe")