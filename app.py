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

# 🔹 Editar Dieta (Interface Web)
@app.route('/dietas/editar/<int:id>', methods=['GET', 'POST'])
def editar_dieta(id):
    dieta = requests.get(f'http://127.0.0.1:5000/api/dietas/{id}').json()

    if request.method == 'POST':
        data = {
            "nome": request.form['nome'],
            "descricao": request.form['descricao']
        }
        requests.put(f'http://127.0.0.1:5000/api/dietas/{id}', json=data)
        return redirect(url_for('listar_dietas'))

    return render_template('editar_dieta.html', dieta=dieta)

# 🔹 Deletar Dieta (Interface Web)
@app.route('/dietas/deletar/<int:id>')
def deletar_dieta(id):
    requests.delete(f'http://127.0.0.1:5000/api/dietas/{id}')
    return redirect(url_for('listar_dietas'))


# 🔹 Dashboard com Estatísticas
@app.route('/dashboard')
def dashboard():
    # Buscar dados da API
    pacientes = requests.get('http://127.0.0.1:5000/api/pacientes').json()
    dietas = requests.get('http://127.0.0.1:5000/api/dietas').json()

    # Total de pacientes e dietas
    total_pacientes = len(pacientes)
    total_dietas = len(dietas)

    # Cálculo de médias (convertendo para números para evitar erros)
    if total_pacientes > 0:
        media_idade = sum(int(p['idade']) for p in pacientes) / total_pacientes
        media_altura = sum(float(p['altura']) for p in pacientes) / total_pacientes
        media_peso = sum(float(p['peso']) for p in pacientes) / total_pacientes
    else:
        media_idade = media_altura = media_peso = 0

    # 🔹 Contagem de pacientes por dieta
    pacientes_por_dieta = {}
    for paciente in pacientes:
        nome_dieta = paciente['nome_dieta'] if paciente['nome_dieta'] else 'Sem dieta'
        pacientes_por_dieta[nome_dieta] = pacientes_por_dieta.get(nome_dieta, 0) + 1

    # 🔹 Encontrar pacientes com dietas incompatíveis com sua idade
    pacientes_incompativeis = []
    for paciente in pacientes:
        if paciente['nome_dieta']:  # Se o paciente tem uma dieta associada
            dieta = next((d for d in dietas if d['nome'] == paciente['nome_dieta']), None)
            if dieta and (paciente['idade'] < dieta['idade_minima'] or paciente['idade'] > dieta['idade_maxima']):
                pacientes_incompativeis.append({
                    "nome": paciente['nome'],
                    "idade": paciente['idade'],
                    "dieta": paciente['nome_dieta'],
                    "idade_min": dieta['idade_minima'],
                    "idade_max": dieta['idade_maxima']
                })

    return render_template('dashboard.html', 
                           total_pacientes=total_pacientes, 
                           total_dietas=total_dietas, 
                           media_idade=round(media_idade, 1),
                           media_altura=round(media_altura, 2),
                           media_peso=round(media_peso, 1),
                           pacientes_por_dieta=pacientes_por_dieta,
                           pacientes_incompativeis=pacientes_incompativeis,
                           pacientes=pacientes[:5])  # Exibir últimos 5 pacientes cadastrados



if __name__ == '__main__':
    app.run(debug=True)
