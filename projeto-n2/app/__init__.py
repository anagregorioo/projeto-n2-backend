from flask import Flask
from app.controller import filme_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(filme_bp)  # Registra o blueprint do controlador

    return app
