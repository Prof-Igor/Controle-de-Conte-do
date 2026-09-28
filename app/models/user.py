from ..db import get_db_connection
from werkzeug.security import check_password_hash

class User:
    @staticmethod
    def authenticate(username, password):
        """Abre a conexão, valida o usuário via SQL puro e fecha o banco."""
        # 1. Solicita uma nova conexão explícita
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            # 2. Executa a query com prevenção a SQL Injection (?)
            cursor.execute(
                'SELECT password_hash FROM users WHERE username = ?', (username,)
            )
            user = cursor.fetchone()
            
            # 3. Valida a senha se o usuário existir
            if user and check_password_hash(user['password_hash'], password):
                return True
                
            return False
            
        finally:
            # 4. Garante que a conexão seja fechada, mesmo se der erro no meio do caminho
            conn.close()