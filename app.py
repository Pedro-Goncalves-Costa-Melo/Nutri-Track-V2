from flask import Flask, render_template, request, redirect, url_for
from routes.paciente_routes import paciente_bp
from routes.dieta_routes import dieta_bp
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Permite requisições de diferentes origens

# 🔹 Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Substitua pelo seu usuário MySQL
app.config['MYSQL_PASSWORD'] = 'senhaSQL'  # Substitua pela sua senha do MySQL
app.config['MYSQL_DATABASE'] = 'nutricionista_db'

# 🔹 Registrar as APIs do backend
app.register_blueprint(paciente_bp, url_prefix='/api')
app.register_blueprint(dieta_bp, url_prefix='/api')

# 🔹 Página Inicial (Interface Web)
@app.route('/')
def home():
    return render_template('home.html')

# 🔹 Listar Pacientes (Interface Web)
@app.route('/pacientes')
def listar_pacientes():
    response = requests.get('http://127.0.0.1:5000/api/pacientes')
    pacientes = response.json()
    return render_template('pacientes.html', pacientes=pacientes)

# 🔹 Criar Novo Paciente (Interface Web)
@app.route('/pacientes/novo', methods=['GET', 'POST'])
def novo_paciente():
    dietas = requests.get('http://127.0.0.1:5000/api/dietas').json()

    if request.method == 'POST':
        data = {
            "nome": request.form['nome'],
            "idade": request.form['idade'],
            "altura": request.form['altura'],
            "peso": request.form['peso'],
            "dieta_id": request.form['dieta_id'] if request.form['dieta_id'] else None
        }
        requests.post('http://127.0.0.1:5000/api/pacientes', json=data)
        return redirect(url_for('listar_pacientes'))

    return render_template('novo_paciente.html', dietas=dietas)

# 🔹 Editar Paciente (Interface Web)
@app.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = requests.get(f'http://127.0.0.1:5000/api/pacientes/{id}').json()
    dietas = requests.get('http://127.0.0.1:5000/api/dietas').json()

    if request.method == 'POST':
        data = {
            "nome": request.form['nome'],
            "idade": request.form['idade'],
            "altura": request.form['altura'],
            "peso": request.form['peso'],
            "dieta_id": request.form['dieta_id'] if request.form['dieta_id'] else None
        }
        requests.put(f'http://127.0.0.1:5000/api/pacientes/{id}', json=data)
        return redirect(url_for('listar_pacientes'))

    return render_template('editar_paciente.html', paciente=paciente, dietas=dietas)

# 🔹 Deletar Paciente (Interface Web)
@app.route('/pacientes/deletar/<int:id>')
def deletar_paciente(id):
    requests.delete(f'http://127.0.0.1:5000/api/pacientes/{id}')
    return redirect(url_for('listar_pacientes'))

# 🔹 Listar Dietas (Interface Web)
@app.route('/dietas')
def listar_dietas():
    response = requests.get('http://127.0.0.1:5000/api/dietas')
    dietas = response.json()
    return render_template('dietas.html', dietas=dietas)

# 🔹 Criar Nova Dieta
@app.route('/dietas/nova', methods=['GET', 'POST'])
def nova_dieta():
    if request.method == 'POST':
        data = {
            "nome": request.form['nome'],
            "descricao": request.form['descricao']
        }
        requests.post('http://127.0.0.1:5000/api/dietas', json=data)
        return redirect(url_for('listar_dietas'))

    return render_template('nova_dieta.html')

# 🔹 Dashboard com Estatísticas
@app.route('/dashboard')
def dashboard():
    pacientes = requests.get('http://127.0.0.1:5000/api/pacientes').json()
    dietas = requests.get('http://127.0.0.1:5000/api/dietas').json()

    total_pacientes = len(pacientes)
    total_dietas = len(dietas)

    # Criar estatísticas de pacientes por dieta
    dietas_labels = []
    dietas_data = []
    dieta_dict = {dieta['id']: dieta['nome'] for dieta in dietas}

    contagem_dietas = {}

    for paciente in pacientes:
        dieta_id = paciente['dieta_id']
        if dieta_id:
            nome_dieta = dieta_dict.get(dieta_id, "Desconhecida")
            if nome_dieta in contagem_dietas:
                contagem_dietas[nome_dieta] += 1
            else:
                contagem_dietas[nome_dieta] = 1

    for nome, qtd in contagem_dietas.items():
        dietas_labels.append(nome)
        dietas_data.append(qtd)

    return render_template('dashboard.html', 
                           total_pacientes=total_pacientes, 
                           total_dietas=total_dietas,
                           dietas_labels=dietas_labels,
                           dietas_data=dietas_data)


if __name__ == '__main__':
    app.run(debug=True)
