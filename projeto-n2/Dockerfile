# Usar imagem base do Python 3.11
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos requirements.txt e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o diretório de trabalho
COPY . .

# Expor a porta 8080
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
