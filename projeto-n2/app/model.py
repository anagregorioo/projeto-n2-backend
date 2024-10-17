class Filme:
    def __init__(self, titulo, ano, sinopse, nota, popularidade):
        self.titulo = titulo
        self.ano = ano
        self.sinopse = sinopse
        self.nota = nota
        self.popularidade = popularidade

    def to_dict(self):
        return {
            'Titulo': self.titulo,
            'Ano': self.ano,
            'Sinopse': self.sinopse,
            'Nota': self.nota,
            'Popularidade': self.popularidade
        }
