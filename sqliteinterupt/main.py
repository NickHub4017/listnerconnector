#!/usr/bin/python
import sys

import subprocess

import signal
from termcolor import colored, cprint

from initdb import initdbclass
import time
import os

# class DeamonThreads(threading.Thread):
#      def __init__(self,inptype):
#          super(DeamonThreads, self).__init__()
#          self.deamonthreadtype=inptype
#      def run(self):
#          if(self.deamonthreadtype==1):
#             inputmainlink()
def processCleanUp():
    tmp = os.popen("ps aux").read()
    pslist=[]
    #print tmp
    for line in tmp.split("\n"):
        x=1
        line=line.strip()
        procdata=line.split(" ")
        for c in range(0,procdata.count('')):
            procdata.remove('')
        #print procdata
        try:
            if("controldeamon.py" in procdata[11]):
                try:
                    pslist.append(int(procdata[1]))
                except Exception as e:
                    pass
                    #print "Error occured in init process cleanup:- "+e.message
        except Exception as e:
            pass
            #print "Error occured in init process cleanup Main try :- "+e.message
    #print pslist
    for p in pslist:
        try:
            if(os.getpid()!=p):
                print p,os.getpid()
                os.kill(p,9)
        except Exception as e:
            print "Error occured in init process cleanup (Killing):- " + e.message

        #time.sleep(1)
#print "Please wait for Process cleanup"
cprint("Please wait for Process cleanup", 'green')
processCleanUp()
#print "Process cleanUp done"
cprint("Process cleanUp done", 'green')

currentDb=initdbclass()




control_pipe_name="/tmp/controlpipe"
if not os.path.exists(control_pipe_name):
    os.mkfifo(control_pipe_name)

mainpath=os.path.dirname(os.path.abspath(__file__))
inputpath=mainpath+"/inputdeamon/inputDeamon.py"
controlpath=mainpath+"/controldeamonformain.py"
outputpath=mainpath+"/outputdeamon/outputdeamon.py"
procpath=os.getenv("HOME")+"/a.py"

print mainpath
print inputpath
print controlpath
print outputpath
print procpath



inpproc=subprocess.Popen(['python', inputpath])
controlproc=subprocess.Popen(['python', controlpath])
outpproc=subprocess.Popen(['python', outputpath])
processproc=subprocess.Popen(['python', procpath])

currentDb.updateinputpid(inpproc.pid)
currentDb.updatecontrolpid(controlproc.pid)
currentDb.updateprocesspid(outpproc.pid)
currentDb.updateoutputpid(outpproc.pid)


def signal_handler(signal, frame):
    print "Process are Shutting down"
    inpproc.kill()
    outpproc.kill()
    controlproc.kill()
    processproc.kill()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
#print('Press Ctrl+C')
#signal.pause()

while(1):
    pipein = open(control_pipe_name, 'r')
    line = pipein.read()
    print line,"----+++++++++----------"
    if line!="":
        #print line,"-- is received from the control"
        cprint(line+" -- is received from the control", 'yellow')
    if(line[0]=="T"):
        os.kill(inpproc.pid,9)
        inpproc = subprocess.Popen(['python', inputpath])
        currentDb.updateinputpid(inpproc.pid)
    if (line[1] == "T"):
        os.kill(outpproc.pid, 9)
        outpproc = subprocess.Popen(['python', outputpath])
        currentDb.updateoutputpid(outpproc.pid)
    if (line[2] == "T"):
        os.kill(controlproc.pid, 9)
        controlproc = subprocess.Popen(['python', controlpath])
        currentDb.updatecontrolpid(controlproc.pid)

    #ToDo implement the process shutdown mechanism

    pipein.close()
    time.sleep(5)

