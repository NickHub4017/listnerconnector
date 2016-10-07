#This class will handle the control message and make decisions upon the handler.

import json


class ControlHandler:
    def __init__(self):
        print "Handler initiated"

    def insertcontrolmessage(self,controlmsg):
        print type(controlmsg)

        controlmsgjson = json.loads(controlmsg)
        print type(controlmsgjson)
        inputdeamonprop=controlmsgjson["inpdeamon"]
        outputdeamonprop = controlmsgjson["oupdeamon"]
        cntrldeamonprop = controlmsgjson["cntrldeamon"]

        controlmessagetimestamp=controlmsgjson["timestamp"]
        controlmessagefromip = controlmsgjson["fromip"]
        controlmessagesysid = controlmsgjson["sysid"]
        controlmessagesysname = controlmsgjson["sysname"]
        controlmessageprogramproperties = controlmsgjson["programproperties"]
        controlmessagedeviceproperties = controlmsgjson["deviceproperties"]

    def submitdatatodatabase(self):
        print "todo implement the db submit code"


