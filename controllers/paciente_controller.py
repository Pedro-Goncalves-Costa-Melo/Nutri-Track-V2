from flask import jsonify
from database import get_db_connection

# Criar um paciente
def criar_paciente(nome, idade, altura, peso, dieta_id):
    db = get_db_connection()
    cursor = db.cursor()
    query = "INSERT INTO pacientes (nome, idade, altura, peso, dieta_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, idade, altura, peso, dieta_id))
    db.commit()
    db.close()
    return {"id": cursor.lastrowid, "nome": nome, "idade": idade, "altura": altura, "peso": peso, "dieta_id": dieta_id}

# Listar todos os pacientes
def listar_pacientes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    db.close()
    return pacientes

# Buscar paciente por ID
def buscar_paciente(id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id,))
    paciente = cursor.fetchone()
    db.close()
    return paciente

# Atualizar paciente
def atualizar_paciente(id, nome, idade, altura, peso, dieta_id):
    db = get_db_connection()
    cursor = db.cursor()
    query = "UPDATE pacientes SET nome=%s, idade=%s, altura=%s, peso=%s, dieta_id=%s WHERE id=%s"
    cursor.execute(query, (nome, idade, altura, peso, dieta_id, id))
    db.commit()
    db.close()
    return buscar_paciente(id)

# Deletar paciente
def deletar_paciente(id):
    db = get_db_connection()
    cursor = db.cursor()
    query = "DELETE FROM pacientes WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    db.close()
    return True
