from werkzeug.security import generate_password_hash, check_password_hash

# Simulando um banco de dados com as senhas protegidas por hash
USERS = {
    'igor': generate_password_hash('senha123'),
    'admin': generate_password_hash('admin123')
}

def authenticate_user(username, password):
    """Verifica se o usuário existe e compara a senha em texto plano com o hash salvo."""
    user_hash = USERS.get(username)
    
    # check_password_hash faz a validação criptográfica segura
    if user_hash and check_password_hash(user_hash, password):
        return True
        
    return False