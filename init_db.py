import sqlite3
import os
from werkzeug.security import generate_password_hash

# Define o nome do arquivo do banco
db_path = 'conteudos_bd.db'

# Conecta ao arquivo (cria o arquivo se não existir)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. SQL Puro para criar a tabela de usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
''')

# 2. Inserindo o primeiro usuário manualmente
username = 'igor'
password_hash = generate_password_hash('senha123')

try:
    # SQL Puro para inserir os dados
    cursor.execute(
        'INSERT INTO users (username, password_hash) VALUES (?, ?)',
        (username, password_hash)
    )
    print(f"Usuário '{username}' inserido com sucesso!")
except sqlite3.IntegrityError:
    print(f"O usuário '{username}' já existe no banco.")

# Confirma as alterações e fecha a conexão
conn.commit()
conn.close()