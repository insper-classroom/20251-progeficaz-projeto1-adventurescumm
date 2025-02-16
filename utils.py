import sqlite3 as sql

def load_data(dados):
    con = sql.connect(dados)
    cur = con.cursor()
    cur.execute("SELECT * FROM notes")
    data = cur.fetchall()
    return data

def load_template(template):
    template = f"static/templates/{template}"
    t = open(template)
    return t.read()

def add_sql(dados, filename='static/data/db_web.db'):
    con = sql.connect(filename)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO notes(TITULO, DETALHES) VALUES (?, ?)", (dados['titulo'], dados['detalhes'])
    )
    con.commit()

def delete_sql(note_id, filename='static/data/db_web.db'):
    con = sql.connect(filename)
    cur = con.cursor()
    cur.execute(
        "DELETE FROM notes WHERE ID=?", (note_id)
    )
    con.commit()