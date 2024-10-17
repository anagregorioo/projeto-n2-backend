#arquivo para manipular o armazenamento local
#aqui eu faco algumas operacoes para ler o filme e cadastrar o filme
#eu tenho um arquivo chamado filmes_vistos.json que armazena os filmes que eu ja vi

import json
import os

FILE_PATH = 'filmes_vistos.json'

def carregar_filmes_vistos():
    """Carrega a lista de filmes vistos do arquivo JSON."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def salvar_filme_visto(filme):
    """Salva um novo filme como visto no arquivo JSON."""
    filmes_vistos = carregar_filmes_vistos()
    filmes_vistos.append(filme)

    with open(FILE_PATH, 'w') as file:
        json.dump(filmes_vistos, file, indent=4)

def listar_filmes_vistos():
    """Retorna a lista de todos os filmes vistos."""
    return carregar_filmes_vistos()
