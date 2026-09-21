from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='views')
    app.secret_key = 'chave_secreta_para_sessoes_mude_em_producao'

    # Registro dos Blueprints
    from app.controllers import auth_bp, main_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)

    return app