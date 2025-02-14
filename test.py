import sqlite3 as sql
from utils import load_data

def insert_data():
    con = sql.connect('db_web.db')
    cur = con.cursor()
    cur.execute("INSERT INTO notes(NOTA) VALUES (?)", ({
        "TITULO": "TESTE1",
        "DETALHES": "TESTE2"
    }))
    con.commit()
    con.close()

print(load_data('db_web.db'))