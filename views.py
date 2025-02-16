from utils import load_data, load_template, add_sql, delete_sql

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados[0], details=dados[1], id=dados[2])
        for dados in load_data('static\data\db_web.db')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    dados = {
        "titulo": titulo,
        "detalhes": detalhes
    }
    return  add_sql(dados)

def delete(note_id):
    return delete_sql(note_id)