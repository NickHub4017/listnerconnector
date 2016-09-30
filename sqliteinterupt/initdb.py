import sqlite3

class initdb:
    def __init__(self):
        print "iniialise database"

        cursor,conn=self.connecttodb();
        cursor.execute('''CREATE TABLE IF NOT EXISTS deamonmetadata (device text, msgdate TIMESTAMP DEFAULT DATETIME('now'), ip text, port int,type text, protocol text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS devicemetadata (msgdate TIMESTAMP DEFAULT DATETIME('now'), key text, value text)''')
        cursor.execute("insert into deamonmetadata (device) values ('inputdeamon');")
        cursor.execute("insert into deamonmetadata (device) values ('outputdeamon');")
        cursor.execute("insert into deamonmetadata (device) values ('controldeamon');")
        self.closedb(conn)

    def connecttodb(self):
        conn = sqlite3.connect('pnp.db')
        cursor = conn.cursor()
        return  cursor,conn

    def closedb(self,conn):
        conn.commit()
        conn.close()






#cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


