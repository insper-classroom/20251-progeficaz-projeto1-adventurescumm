from flask import Flask, render_template_string, request, redirect
import views

id = 0

caminho = "static/data/notes.json"

app = Flask(__name__)


# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<note_id>', methods=['GET'])
def delete_form(note_id):
    views.delete(note_id)
    return redirect('/')

@app.route('/edit/<note_id>', methods=['GET'])
def edit_form(note_id):
    return render_template_string(views.edit_page(note_id))

@app.route('/edit/<note_id>', methods=['POST'])
def edit_note(note_id):
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.edit_note(note_id, titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)