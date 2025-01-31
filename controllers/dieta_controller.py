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

# Atualizar dieta (corrigido para incluir idade_minima e idade_maxima)
def atualizar_dieta(id, nome, descricao, idade_minima, idade_maxima):
    db = get_db_connection()
    cursor = db.cursor()
    
    query = """
        UPDATE dietas 
        SET nome=%s, descricao=%s, idade_minima=%s, idade_maxima=%s 
        WHERE id=%s
    """
    cursor.execute(query, (nome, descricao, idade_minima, idade_maxima, id))
    
    db.commit()
    db.close()
    
    return buscar_dieta(id)  # Retorna a dieta atualizada


# Deletar dieta
def deletar_dieta(id):
    db = get_db_connection()
    cursor = db.cursor()
    query = "DELETE FROM dietas WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    db.close()
    return True
