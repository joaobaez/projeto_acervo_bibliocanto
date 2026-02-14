from .extensions import db, login_manager
from flask import Flask
from os import path
from config import Config, Development


def create_app():
    #instancia o servidor
    app = Flask(__name__, template_folder='templates')

    #1 Configuração do BD
    app.config.from_object(Development)

    #2 Extensões
    db.init_app(app)
    login_manager.init_app(app)

    #3 Blueprints
    from .auth import bp as auth_bp
    from .books import bp as books_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)

    #4 importa Models
    from .auth import models as auth_models
    #from .books import models as books_models

    #5 Configuração de Login
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return auth_models.User.query.get(int(user_id))

    #6 Criação do banco
    create_database(app)

    #7 Encerra a função
    return app


def create_database(app):
    with app.app_context():
        db.create_all()

