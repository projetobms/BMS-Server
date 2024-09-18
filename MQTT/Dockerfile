# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos requirements.txt e o script Python para o container
COPY requirements.txt requirements.txt
COPY server.py server.py

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta MQTT (se for necessário para debugging)
EXPOSE 1883

# Comando para iniciar o script Python
CMD ["python", "server.py"]
