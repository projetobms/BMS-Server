# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie todos os arquivos do diretório de build para o diretório de trabalho
COPY . .

# Instale as dependências necessárias
RUN pip install opcua

# Dê permissão de execução ao script de inicialização
RUN chmod +x start.sh

# Exponha as portas que os servidores irão usar
EXPOSE 8081 8082 8083 8084 8085

# Execute o script de inicialização quando o container for iniciado
CMD ["./start.sh"]
