from utils import load_data, load_template, add_sql, delete_sql, edit_sql

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

def edit_page(note_id):
    note_template = load_template('components/edit_note.html')
    notes_li = [
        note_template.format(title=dados[0], details=dados[1], id=note_id)
        for dados in load_data('static\data\db_web.db')# if dados[2] == note_id
    ]
    notes = '\n'.join(notes_li)

    return load_template('components/edit.html').format(edit_notes=notes)

def edit_note(note_id, titulo, detalhes):
    dados = {
        "titulo": titulo,
        "detalhes": detalhes
    }
    return edit_sql(dados, note_id)