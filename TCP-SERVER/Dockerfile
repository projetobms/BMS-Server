# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o script para o diretório de trabalho
COPY . .

# Instale as dependências necessárias
RUN pip install opcua

# Exponha a porta que o servidor irá usar
EXPOSE 8081 8082 8083 8084 8085

# Execute o script quando o container for iniciado
CMD ["python", "receive_tcp_server.py"]
