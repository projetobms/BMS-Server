# Usar uma imagem base do Python
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para o contêiner
COPY server.py /app/
COPY requirements.txt /app/

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que o servidor irá escutar
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
