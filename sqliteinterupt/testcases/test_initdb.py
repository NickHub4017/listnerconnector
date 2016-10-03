from unittest import TestCase

from sqliteinterupt.initdb import initdb


class TestInitdb(TestCase):
    def __init__(self):
        self.db = initdb()
        self.conn;
    def test_connecttodb(self):
        cursor, self.conn=self.db.connecttodb()
        self.assertIsNone(cursor)
        self.assertIsNone(self.conn)

        #self.fail()

    def test_closedb(self):
        #self.fail()
        self.db.closedb(self.conn)
        self.assertIsNone(self.conn)

    def test_updatefulldeamondata(self):
        print "Done"
        #self.fail()


TestInit=TestInitdb();
TestInit.test_connecttodb()
TestInit.test_closedb()