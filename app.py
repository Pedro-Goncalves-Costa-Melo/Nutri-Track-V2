from flask import Flask
from routes.paciente_routes import paciente_bp
from routes.dieta_routes import dieta_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de diferentes origens

# 🔹 Configurar conexão com MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Substitua pelo seu usuário MySQL
app.config['MYSQL_PASSWORD'] = 'senhaSQL'  # Substitua pela sua senha do MySQL
app.config['MYSQL_DATABASE'] = 'nutricionista_db'

# 🔹 Registrar as rotas corretamente
app.register_blueprint(paciente_bp, url_prefix='/api')
app.register_blueprint(dieta_bp, url_prefix='/api')

@app.route('/')
def home():
    return {"mensagem": "Servidor Flask rodando com MySQL!"}

if __name__ == '__main__':
    app.run(debug=True)
