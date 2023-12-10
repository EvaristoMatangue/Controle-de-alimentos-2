from flask import Flask
from .main.routes import main
from .extensions import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rastreador_de_alimentos/db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização das extensões
    db.init_app(app)
    migrate = Migrate(app, db)
    

    # Registro dos blueprints
    app.register_blueprint(main)

    return app
if __name__ == "__name__":
    create_app().run(debug=True)
