from flask import Blueprint, request, jsonify
from app.service import consultar_filme_por_titulo, marcar_filme_como_visto, obter_filmes_vistos

# criando um blueprint para as rotas referentes a /filmes
filme_bp = Blueprint('filmes', __name__, url_prefix='/filmes')

# consultar filmes
@filme_bp.route('/consultar', methods=['GET'])
def consultar_filme():
    titulo = request.args.get('titulo')
    if not titulo:
        return jsonify({'erro': 'Título não informado'}), 400

    filme = consultar_filme_por_titulo(titulo)
    if filme:
        return jsonify(filme), 200
    return jsonify({'erro': 'Filme não encontrado'}), 404

# marcar um filme como visto
@filme_bp.route('/vistos', methods=['POST'])
def marcar_filme_visto():
    dados = request.get_json()
    titulo = dados.get('titulo')  # O usuario só precisa enviar o título do filme

    if not titulo:
        return jsonify({'erro': 'Título não informado'}), 400

    resposta = marcar_filme_como_visto(titulo)
    if 'marcado como visto' in resposta:
        return jsonify({'mensagem': resposta}), 200
    return jsonify({'erro': resposta}), 404

# listar todos os filmes marcados como vistos
@filme_bp.route('/vistos', methods=['GET'])
def listar_filmes_vistos():
    filmes = obter_filmes_vistos()
    return jsonify(filmes), 200

# Rota /sobre 
@filme_bp.route('/sobre', methods=['GET'])
def sobre():
    return jsonify({
        "Aluno": "Ana Carolina Gregório Gonçalves",
        "Projeto": "Servico de Consulta de Filmes com TMDb",
        "Instruções": [
            "Consultar um filme: GET /filmes/consultar?titulo=O titulo desejado",
            "Marcar um filme como visto: POST /filmes/vistos",
            "Exemplo de requisição POST:",
            {
                "URL": "http://localhost:8080/filmes/vistos",
                "Headers": {
                    "Content-Type": "application/json"
                },
                "Body": '{"titulo": "Inception"}'
            },
            "Ver todos os filmes já vistos: GET /filmes/vistos"
        ]
    }), 200
