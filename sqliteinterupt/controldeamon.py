from DeamonLinkFactory import DeamonLinkFactory
from initdb import initdbclass

currentDb=initdbclass()
controlip=currentDb.getdata("controlip")
controlport=currentDb.getdata("controlport")
controllink=DeamonLinkFactory("client").getConnection(controlip,controlport)
controllink.connect()
controllink.getdata()