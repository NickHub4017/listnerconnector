from unittest import TestCase

from sqliteinterupt.initdb import initdbclass


class TestInitdb(TestCase):
    global db;
    db=initdbclass();
    global conn;
    conn=None
    def init(self):
        #super(a,b)
        global conn,db;
        #self.db = initdbclass()
        conn=None;
    def test_connecttodb(self):
        global conn, db;
        self.init();
        cursor, conn=db.connecttodb()
        self.assertIsNotNone(cursor)
        self.assertIsNotNone(conn)

        #self.fail()

    def test_closedb(self):
        #self.fail()
        global conn, db;
        db.closedb(conn)
        self.assertIsNotNone(conn)

    def test_updatefulldeamondata(self):
        print "Done"
        #self.fail()

    def runTest(self, result=None):
        TestInit = TestInitdb();
        TestInit.test_connecttodb()
        TestInit.test_closedb()


