#This class will handle the control message and make decisions upon the handler.

import json

import time

from initdb import initdbclass

class ControlHandler:
    def __init__(self):
        print "Handler initiated"

    def insertcontrolmessage(self,controlmsg):
        #print "@json:- ",controlmsg
        controlmsgjson = json.loads(controlmsg)
        #print controlmsgjson
        inputdeamonprop=controlmsgjson["inpdeamon"]
        print inputdeamonprop,"  ++ ---   "
        outputdeamonprop = controlmsgjson["oupdeamon"]
        print outputdeamonprop, "  ++ ---   "
        cntrldeamonprop = controlmsgjson["cntrldeamon"]
        print cntrldeamonprop, "  ++ ---   "

        controlmessagetimestamp=controlmsgjson["timestamp"]
        controlmessagefromip = controlmsgjson["fromip"]
        controlmessagesysid = controlmsgjson["sysid"]
        controlmessagesysname = controlmsgjson["sysname"]
        controlmessageprogramproperties = controlmsgjson["programproperties"]
        controlmessagedeviceproperties = controlmsgjson["deviceproperties"]
        resdata=self.submitdatatodatabase(controlmessagetimestamp,controlmessagefromip,controlmessagesysid,controlmessagesysname,controlmessageprogramproperties,controlmessagedeviceproperties,inputdeamonprop,outputdeamonprop,cntrldeamonprop)
        return resdata


    def submitdatatodatabase(self,controlmessagetimestamp,controlmessagefromip,controlmessagesysid,controlmessagesysname,controlmessageprogramproperties,controlmessagedeviceproperties,inputdeamonprop,outputdeamonprop,cntrldeamonprop):
        #print "todo implement the db submit code"
        self.db=initdbclass()
        #print "---------------------1------------------"

        self.db.updatedevicemetadata("subdate",controlmessagetimestamp,time.time())
        self.db.updatedevicemetadata("updatefrom", controlmessagefromip, time.time())
        self.db.updatedevicemetadata("sysid", controlmessagesysid, time.time())#ToDo add this to the table
        self.db.updatedevicemetadata("sysname", controlmessagesysname, time.time())
        self.db.updatedevicemetadata("progparams", controlmessageprogramproperties, time.time())
        self.db.updatedevicemetadata("deviceparams", controlmessagedeviceproperties, time.time())
        #print "---------------------2------------------"
        updatelist=[False,False,False,False]  #input output control program
        inprow = self.db.getnodedata("inpdeamon")
        if (inprow[2]!=inputdeamonprop["ip"] or inprow[3]!=inputdeamonprop["port"] or inprow[4]!=inputdeamonprop["type"] or inprow[5]!=inputdeamonprop["protocol"]):
            self.db.updatefulldeamondata(inputdeamonprop,time.time())
            updatelist[0]=True
        #print "---------------------3------------------"
        outprow = self.db.getnodedata("oudeamon")
        if (outprow[2] != outputdeamonprop["ip"] or outprow[3] != outputdeamonprop["port"] or outprow[4] != outputdeamonprop["type"] or outprow[5] != outputdeamonprop["protocol"]):
            self.db.updatefulldeamondata(outputdeamonprop, time.time())
            updatelist[1] = True
        #print "---------------------4------------------",cntrldeamonprop["port"]
        controlprow = self.db.getnodedata("cntrldeamon")
        if (controlprow[2] != cntrldeamonprop["ip"] or controlprow[3] != cntrldeamonprop["port"] or controlprow[4] !=cntrldeamonprop["type"] or controlprow[5] != cntrldeamonprop["protocol"]):
            self.db.updatefulldeamondata(cntrldeamonprop, time.time())
            updatelist[2] = True
        #print "---------------------5------------------"
        return updatelist


