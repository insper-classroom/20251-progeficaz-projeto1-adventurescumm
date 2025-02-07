import json

def load_data(dados):
    dados = f"static\data\{dados}"
    d = open(dados)
    notas = json.load(d)
    return notas

def load_template(template):
    template = f"static/templates/{template}"
    t = open(template)
    return t.read()

def add_json(dados, filename='static/data/notes.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(dados)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)