import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # Certifique-se de que o MySQL está rodando no localhost
        user='theus',       # Substitua pelo seu usuário do MySQL
        password='140605',  # Substitua pela senha correta do usuário
        database='auth_db'    # Certifique-se de que o banco de dados 'auth_db' existe
    )
    return connection