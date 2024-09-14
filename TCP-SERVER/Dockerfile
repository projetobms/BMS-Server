# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o script para o diretório de trabalho
COPY tcp_server.py .

# Instale as dependências necessárias
RUN pip install opcua

# Exponha a porta que o servidor irá usar
EXPOSE 8081

# Execute o script quando o container for iniciado
CMD ["python", "tcp_server.py"]
