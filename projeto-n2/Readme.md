# Projeto n2 Backend
Aluna: Ana Carolina Gregório Gonçalves

## Sobre
O projeto consiste em um pesquisador de filmes, tendo uma serie de filmes utilizando a api themoviedb
Fiz com que o codigo consiga retornar o filme, dados do mesmo e tambem salvar como visto o filme

## Como rodar:
Digite o seguinte comando na raiz do projeto

```bash 
docker-compose up --build
```

Utilizando insomnia ou postman, coloque a url ``` http://127.0.0.1:8080/filmes ```
ela sera a rota principal, dentro dela existem (/sobre,/consultar,/vistos)
veja abaixo como usa-los

## Descrição de rotas
/filmes/sobre

/filmes/consultar?titulo=titulo desejado

/filmes/vistos (com os metodos get e post)

Corpo do metodo post:

                "URL": "http://localhost:8080/filmes/vistos",
                "Headers": {
                    "Content-Type": "application/json"
                },
                "Body": '{"titulo": "Inception"}'

