import sqlite3
import datetime;
class initdbclass():
    def __init__(self):
        print "iniialise database"

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
            #cursor.execute("insert into devicemetadata (key,value) values ('controlip','127.0.0.1');")
            #cursor.execute("insert into devicemetadata (key,value) values ('controlport',8080);")


        except Exception as e:
            print("Insert error "+e.message.capitalize())

        self.closedb(conn)

    def connecttodb(self):
        conn = sqlite3.connect('pnp.db')
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





#cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


