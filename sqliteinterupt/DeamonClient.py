import socket

import time

from ControlHandler import ControlHandler
class DeamonClient:
    def __init__(self,inpport=1000,inpip="127.0.0.1"):
        print inpport," ",inpip
        self.port=int(inpport)
        self.ip=inpip
        self.socket=None
        self.buffersize=1024

    def connect(self):
        try:
            self.socket = socket.socket()
            self.socket.connect((self.ip, self.port))
            return True
        except:
            return False


    def getdata(self):
        try:
            self.socket.send("togen")
        except Exception as e:
            print "ID Sending error ",e
        if(self.socket is not None):
            currentstr=""
            #isbegin=False
            while(1):#ToDo remove onetime buffer read and add dynamic reading.
                #self.controlmessage = str(self.socket.recv(self.buffersize))
                print self.controlmessage, " <--->  "
                self.controlmessage=str(self.socket.recv(self.buffersize))
                print self.controlmessage," ---  "
                #time.sleep(5)
                self.handler=ControlHandler()
                try:
                    changedcomponents=self.handler.insertcontrolmessage(self.controlmessage)
                except Exception as e:
                    print e," At get data"
                #ToDo send the changed components to shutdown thread and create new
                #print "Control deamon data updated"
                print changedcomponents
                return changedcomponents
                #break;
        else:
            print "Sory Control deamon socket has an error"

    def disconnect(self):
        if (self.socket is not None):
            self.socket.close()
            self.socket=None



