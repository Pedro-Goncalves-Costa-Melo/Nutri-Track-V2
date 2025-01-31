import mysql.connector
from flask import current_app

def get_db_connection():
    """Cria e retorna uma nova conexão com o banco de dados."""
    db = mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DATABASE']
    )
    return db
