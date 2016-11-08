#!/usr/bin/python
import unittest

from sqliteinterupt.initdb import initdbclass


class TestInitdb(unittest.TestCase):

    def test_connecttodb(self):
        db = initdbclass();
        cursor,conn=db.connecttodb()
        self.assertIsNotNone(cursor)
        self.assertIsNotNone(conn)


    def test_updatedeamon(self):
        a = self.getcontrolmsg()
        db =initdbclass();

        db.updatefulldeamondata(a["inpdeamon"],"2016-10-10")
        db.updatefulldeamondata(a["oupdeamon"], "2016-10-10")
        db.updatefulldeamondata(a["cntrldeamon"], "2016-10-10")

    def test_updatedevicemetadata(self):
        a=self.getcontrolmsg()

        db = initdbclass();
        db.updatedevicemetadata("subdate",a["timestamp"],"2016-10-10")
        db.updatedevicemetadata("updatefrom", a["fromip"],"2016-10-10")
        db.updatedevicemetadata("sysid", a["sysid"],"2016-10-10")
        db.updatedevicemetadata("sysname", a["sysname"],"2016-10-10")
        db.updatedevicemetadata("progparams", a["programproperties"],"2016-10-10")
        db.updatedevicemetadata("deviceparams", a["deviceproperties"],"2016-10-10")

    def getcontrolmsg(self):
        a = {"inpdeamon": {"name": "inpdeamon",
                           "ip": "127.0.0.1",
                           "port": 8080,
                           "type": "server",
                           "protocol": "http",},
             "oupdeamon": {"name": "oudeamon",
                           "ip": "127.0.0.1",
                           "port": 8080,
                           "type": "server",
                           "protocol": "http",},
             "cntrldeamon": {"name": "cntrldeamon",
                             "ip": "127.0.0.1",
                             "port": 8080,
                             "type": "server",
                             "protocol": "http",},
             "timestamp": "2016-10-02 10:00:00",
             "fromip": "127.0.0.1",
             "sysid": 128,
             "sysname": "main01",
             "programproperties": "-p -q",
             "deviceproperties": "-p -q"
             }
        return a;


if __name__ == '__main__':
    unittest.main()