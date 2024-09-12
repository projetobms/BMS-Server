# Use a imagem base oficial do Python 3.10
FROM python:3.10

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos para o container
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o container
COPY . .

# Garantir que o diretório de scripts do Python esteja no PATH
ENV PATH="/root/.local/bin:$PATH"

# Definir permissões de execução no arquivo start.sh
RUN chmod +x /app/start.sh

# Expor a porta na qual o FastAPI será executado
EXPOSE 8000

# Manter o container rodando para debug
CMD ["sh", "/app/start.sh"]