from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.models import authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Bloqueio: Se o usuário já estiver logado, manda direto para a home
    if 'user' in session:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if authenticate_user(username, password):
            session['user'] = username
            return redirect(url_for('main.home'))
        else:
            flash('Usuário ou senha inválidos.')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))