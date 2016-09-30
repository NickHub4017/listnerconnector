#This class will handle the control message and make decisions upon the handler.

import json


class ControlHandler:
    def __init__(self):
        print "Handler initiated"

    def insertcontrolmessage(self,controlmsg):
        controlmsgjson = json.loads(controlmsg)

        inputdeamonprop=controlmsg["inpdeamon"]
        outputdeamonprop = controlmsg["oupdeamon"]
        cntrldeamonprop = controlmsg["cntrldeamon"]

        controlmessagetimestamp=controlmsg["timestamp"]
        controlmessagefromip = controlmsg["fromip"]
        controlmessagesysid = controlmsg["sysid"]
        controlmessagesysname = controlmsg["sysname"]
        controlmessageprogramproperties = controlmsg["programproperties"]
        controlmessagedeviceproperties = controlmsg["deviceproperties"]

    def submitdatatodatabase(self):
        print "todo implement the db submit code"


