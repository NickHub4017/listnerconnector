import yaml
import sys
import os
import time
sys.path.append(os.path.abspath('../'))
from initdb import initdbclass

db=initdbclass()
def compareinputconfig(newconfig):
    datarow = db.getnodedata("inpdeamon")
    #print datarow
    inpip = datarow[2]
    inpport = datarow[3]
    inptype = datarow[4]
    inpprotoc = datarow[5]
    if(inpip!=newconfig["ip"] or inpport!=newconfig["port"] or inptype!=newconfig["type"] or inpprotoc!=newconfig["protocol"]):
        return True
    return False

def comparecntrlconfig(newconfig):
    datarow = db.getnodedata("cntrldeamon")
    cntrlip = datarow[2]
    #print datarow
    cntrlport = datarow[3]
    cntrltype = datarow[4]
    cntrlprotoc = datarow[5]
    if(cntrlip!=newconfig["ip"] or cntrlport!=newconfig["port"] or cntrltype!=newconfig["type"] or cntrlprotoc!=newconfig["protocol"]):
        return True
    return False

def compareoutputconfig(newconfig):
    datarow = db.getnodedata("oudeamon")
    #print datarow
    outpip = datarow[2]
    outport = datarow[3]
    outtype = datarow[4]
    outprotoc = datarow[5]
    if(outpip!=newconfig["ip"] or outport!=newconfig["port"] or outtype!=newconfig["type"] or outprotoc!=newconfig["protocol"]):
        return True
    return False


def readconfig(file):
    with open(file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    #print cfg
    return cfg

def doFileConfig(file):
    print "Begin File execute"
    configs=readconfig(file)
    iscontrolchange=comparecntrlconfig(configs["controldeamon"])
    isinputchange =compareinputconfig(configs["inputdeamon"])
    isoutputchange =compareoutputconfig(configs["outputdeamon"])
    if(iscontrolchange):
        db.updatefulldeamondata(configs["controldeamon"],time.time())
    if (isinputchange):
        db.updatefulldeamondata(configs["inputdeamon"], time.time())
    if (isoutputchange):
        db.updatefulldeamondata(configs["outputdeamon"], time.time())
    print iscontrolchange,isinputchange,isoutputchange


