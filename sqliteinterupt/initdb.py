import sqlite3
import datetime;
import time
class initdbclass():
    def __init__(self):
        #print "iniialise database"

        cursor,conn=self.connecttodb();
        cursor.execute('''CREATE TABLE IF NOT EXISTS deamonmetadata (device text primary key, msgdate TIMESTAMP , ip text, port int,type text, protocol text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS devicemetadata (msgdate TIMESTAMP, key text primary key, value text)''')

        try:
            cursor.execute("insert into deamonmetadata ('device') values ('inpdeamon');")
            cursor.execute("insert into deamonmetadata ('device') values ('oudeamon');")
            cursor.execute("insert into deamonmetadata ('device','ip','port','type','protocol') values ('cntrldeamon','127.0.0.1',8080,'client','tcp');")

            cursor.execute("insert into devicemetadata (key) values ('subdate');")
            cursor.execute("insert into devicemetadata (key) values ('updatefrom');")
            cursor.execute("insert into devicemetadata (key) values ('sysid');")
            cursor.execute("insert into devicemetadata (key) values ('sysname');")
            cursor.execute("insert into devicemetadata (key) values ('deviceparams');")
            cursor.execute("insert into devicemetadata (key) values ('progparams');")
            cursor.execute("insert into devicemetadata (key) values ('inputpid');")
            cursor.execute("insert into devicemetadata (key) values ('outputpid');")
            cursor.execute("insert into devicemetadata (key) values ('controlutpid');")
            cursor.execute("insert into devicemetadata (key) values ('processputpid');")
            #cursor.execute("insert into devicemetadata (key,value) values ('controlip','127.0.0.1');")
            #cursor.execute("insert into devicemetadata (key,value) values ('controlport',8080);")


        except Exception as e:
            print("Insert error "+e.message.capitalize())

        self.closedb(conn)

    def connecttodb(self):
        conn = sqlite3.connect('/home/nrv/PycharmProjects/listnerconnector/sqliteinterupt/pnp.db')
        cursor = conn.cursor()
        return  cursor,conn

    def closedb(self,conn):
        conn.commit()
        #conn.close()


    def updatefulldeamondata(self,jsondeamondata,msgdate):
        try:
            cursor, conn = self.connecttodb();

            cursor.execute(
                """UPDATE deamonmetadata SET msgdate = ? ,ip = ?,port = ?,type = ?,protocol = ? WHERE device= ? """,
                (msgdate, jsondeamondata["ip"], jsondeamondata["port"], jsondeamondata["type"], jsondeamondata["protocol"],jsondeamondata["name"],))

            self.closedb(conn);
        except Exception,e:
            print e.message

    def updatedevicemetadata(self,jsonkey,jsonvalue,msgdate):
        cursor, conn = self.connecttodb();
        cursor.execute(
            """UPDATE devicemetadata SET value = ? ,msgdate = ? WHERE key= ? """,(jsonvalue,msgdate,jsonkey))
        self.closedb(conn);


    def updateSubdate(self,value):

        self.updatedevicemetadata(value,"",value);

    def getdata(self,keyval):
        cursor ,conn=self.connecttodb()
        data = (keyval,)
        cursor.execute('SELECT * FROM devicemetadata WHERE key=?', data)
        fetcheddata=cursor.fetchone()
        #return fetcheddata
        return fetcheddata[2]

    def getnodedata(self,keyval):
        cursor, conn = self.connecttodb()
        data = (keyval,)
        cursor.execute('SELECT * FROM deamonmetadata WHERE device=?', data)
        fetcheddata = cursor.fetchone()
        # return fetcheddata
        return fetcheddata

    def updateinputpid(self,pid):
        self.updatedevicemetadata( "inputpid", pid,time.time() )


    def updateoutputpid(self, pid):
        self.updatedevicemetadata("outputpid", pid, time.time())


    def updatecontrolpid(self, pid):
        self.updatedevicemetadata( "controlutpid", pid, time.time())

    def updateprocesspid(self, pid):
        self.updatedevicemetadata( "processputpid", pid, time.time())

    def getinputpid(self):
        #self.updatedevicemetadata(self, "inputpid", pid, time.time())
        return self.getdata("inputpid")

    def getoutputpid(self):
        #self.updatedevicemetadata(self, "outputpid", pid, time.time())
        return self.getdata("outputpid")

    def getcontrolpid(self):
        #self.updatedevicemetadata(self, "controlutpid", pid, time.time())
        return self.getdata("controlutpid")

    def getprocesspid(self):
        #self.updatedevicemetadata(self, "processputpid", pid, time.time())
        return self.getdata("processputpid")
#cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


