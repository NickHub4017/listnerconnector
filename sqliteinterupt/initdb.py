import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE netmetadata(date text, ip text, port int,  real, price real)''')

cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
