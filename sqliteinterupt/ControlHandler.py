#This class will handle the control message and make decisions upon the handler.

import json

import time

from initdb import initdbclass

class ControlHandler:
    def __init__(self):
        print "Handler initiated"

    def insertcontrolmessage(self,controlmsg):
        print "@json:- ",controlmsg
        controlmsgjson = json.loads(controlmsg)
        print controlmsgjson
        inputdeamonprop=controlmsgjson["inpdeamon"]
        outputdeamonprop = controlmsgjson["oupdeamon"]
        cntrldeamonprop = controlmsgjson["cntrldeamon"]

        controlmessagetimestamp=controlmsgjson["timestamp"]
        controlmessagefromip = controlmsgjson["fromip"]
        controlmessagesysid = controlmsgjson["sysid"]
        controlmessagesysname = controlmsgjson["sysname"]
        controlmessageprogramproperties = controlmsgjson["programproperties"]
        controlmessagedeviceproperties = controlmsgjson["deviceproperties"]
        self.submitdatatodatabase(controlmessagetimestamp,controlmessagefromip,controlmessagesysid,controlmessagesysname,controlmessageprogramproperties,controlmessagedeviceproperties,inputdeamonprop,outputdeamonprop,cntrldeamonprop)


    def submitdatatodatabase(self,controlmessagetimestamp,controlmessagefromip,controlmessagesysid,controlmessagesysname,controlmessageprogramproperties,controlmessagedeviceproperties,inputdeamonprop,outputdeamonprop,cntrldeamonprop):
        print "todo implement the db submit code"
        self.db=initdbclass()
        #print "---------------------1------------------"
        self.db.updatedevicemetadata("subdate",controlmessagetimestamp,time.time())
        self.db.updatedevicemetadata("updatefrom", controlmessagefromip, time.time())
        self.db.updatedevicemetadata("sysid", controlmessagesysid, time.time())#ToDo add this to the table
        self.db.updatedevicemetadata("sysname", controlmessagesysname, time.time())
        self.db.updatedevicemetadata("progparams", controlmessageprogramproperties, time.time())
        self.db.updatedevicemetadata("deviceparams", controlmessagedeviceproperties, time.time())
        #print "---------------------2------------------"
        self.db.updatefulldeamondata(inputdeamonprop,time.time())
        #print "---------------------3------------------"
        self.db.updatefulldeamondata(outputdeamonprop, time.time())
        print "---------------------4------------------",cntrldeamonprop["port"]
        self.db.updatefulldeamondata(cntrldeamonprop, time.time())
        #print "---------------------5------------------"



