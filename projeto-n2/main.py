from flask import Flask, jsonify
from app.controller import filme_bp

app = Flask(__name__)

# Registro do Blueprint
app.register_blueprint(filme_bp)

if __name__ == '__main__':
    app.run(port=8080)
