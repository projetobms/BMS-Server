# Usar uma imagem base com gcc
FROM gcc:latest

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copiar o código do servidor para o container
COPY tcp_server.c .

# Compilar o código
RUN gcc -o tcp_server tcp_server.c

# Expor a porta 8080 para o host
EXPOSE 8081

# Comando para executar o servidor TCP
CMD ["./tcp_server"]
