import sqlite3
import os

def get_db_connection():
    """
    Descobre o caminho da raiz do projeto e abre uma conexão independente 
    com o SQLite toda vez que for chamada.
    """
    # __file__ é o caminho deste arquivo (app/db.py)
    # dirname pega a pasta 'app', o segundo dirname pega a pasta raiz do projeto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, 'conteudos_bd.db')
    
    # Abre a conexão
    conn = sqlite3.connect(db_path)
    
    # Configura para os resultados virem como dicionário (ex: row['password_hash'])
    conn.row_factory = sqlite3.Row 
    
    return conn