import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS notes")

#Create users table  in db_web database
sql ='''CREATE TABLE "notes" (
	"TITULO" TEXT,
    "DETALHES" TEXT,
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
