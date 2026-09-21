from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Se não houver usuário na sessão, barra o acesso e redireciona
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        
        # Se estiver logado, continua para a função original da rota
        return f(*args, **kwargs)
    
    return decorated_function