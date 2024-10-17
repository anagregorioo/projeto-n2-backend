import requests
from app.storage import salvar_filme_visto, listar_filmes_vistos

API_KEY = '0d1811bca235fa9c0509f46bac04e6c6'  # Chave da API TMDb

def consultar_filme_por_titulo(titulo):
    """Consulta o filme na API do TMDb pelo título."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={titulo}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados['results']:
            filme = dados['results'][0]  # Pegando o primeiro resultado
            return {
                'Titulo': filme.get('title'),
                'Ano': filme.get('release_date'),
                'Sinopse': filme.get('overview'),
                'Nota': filme.get('vote_average'),
                'Popularidade': filme.get('popularity')
            }
    return None

def marcar_filme_como_visto(titulo):
    """Marca um filme como visto, buscando os detalhes do filme pelo título."""
    filme = consultar_filme_por_titulo(titulo)
    if filme:
        salvar_filme_visto(filme)  # Salva os detalhes completos do filme
        return f"Filme '{filme['Titulo']}' foi marcado como visto."
    return 'Filme não encontrado.'

def obter_filmes_vistos():
    """Retorna a lista de filmes marcados como vistos."""
    return listar_filmes_vistos()
