from flask import jsonify
from database import get_db_connection

# Criar uma nova dieta
def criar_dieta(nome, descricao, idade_minima, idade_maxima):
    db = get_db_connection()
    cursor = db.cursor()

    query = "INSERT INTO dietas (nome, descricao, idade_minima, idade_maxima) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, descricao, idade_minima, idade_maxima))

    db.commit()
    db.close()

    return {"id": cursor.lastrowid, "nome": nome, "descricao": descricao, "idade_minima": idade_minima, "idade_maxima": idade_maxima}



# Buscar todas as dietas
def listar_dietas():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM dietas"
    cursor.execute(query)
    dietas = cursor.fetchall()

    db.close()
    return dietas

# Buscar dieta por ID
def buscar_dieta(id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dietas WHERE id = %s", (id,))
    dieta = cursor.fetchone()
    db.close()
    return dieta

# Atualizar dieta
def atualizar_dieta(id, nome, descricao):
    db = get_db_connection()
    cursor = db.cursor()
    query = "UPDATE dietas SET nome=%s, descricao=%s WHERE id=%s"
    cursor.execute(query, (nome, descricao, id))
    db.commit()
    db.close()
    return buscar_dieta(id)

# Deletar dieta
def deletar_dieta(id):
    db = get_db_connection()
    cursor = db.cursor()
    query = "DELETE FROM dietas WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    db.close()
    return True
