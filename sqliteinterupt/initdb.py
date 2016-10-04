import sqlite3

class initdbclass():
    def __init__(self):
        print "iniialise database"

        cursor,conn=self.connecttodb();
        cursor.execute('''CREATE TABLE IF NOT EXISTS deamonmetadata (device text primary key, msgdate TIMESTAMP , ip text, port int,type text, protocol text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS devicemetadata (msgdate TIMESTAMP, key text primary key, value text)''')

        try:
            cursor.execute("insert into deamonmetadata ('device') values ('inpdeamon');")
            cursor.execute("insert into deamonmetadata (device) values ('oudeamon');")
            cursor.execute("insert into deamonmetadata (device) values ('cntrldeamon');")

            cursor.execute("insert into devicemetadata (key) values ('subdate');")
            cursor.execute("insert into devicemetadata (key) values ('updatefrom');")
            cursor.execute("insert into devicemetadata (key) values ('sysid');")
            cursor.execute("insert into devicemetadata (key) values ('sysname');")
            cursor.execute("insert into devicemetadata (key) values ('deviceparams');")
            cursor.execute("insert into devicemetadata (key) values ('progparams');")


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
        cursor, conn = self.connecttodb();

        cursor.execute(
            """UPDATE deamonmetadata SET msgdate = ? ,ip = ?,port = ?,type = ?,protocol = ? WHERE device= ? """,
            (msgdate, jsondeamondata["ip"], jsondeamondata["port"], jsondeamondata["type"], jsondeamondata["protocol"],jsondeamondata["name"]))

        self.closedb(conn);

    def updatedevicemetadata(self,jsonkey,jsonvalue,msgdate):
        cursor, conn = self.connecttodb();
        cursor.execute(
            """UPDATE devicemetadata SET value = ? ,msgdate = ? WHERE key= ? """,(jsonvalue,msgdate,jsonkey))
        self.closedb(conn);







#cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


