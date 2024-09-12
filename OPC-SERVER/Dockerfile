# Usando uma imagem base do Ubuntu
FROM ubuntu:20.04



RUN apt-get update && apt-get install -y \
    software-properties-common \
    tzdata 


RUN echo "America/Sao_Paulo" > /etc/timezone && \
    ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata


# Instalando dependências
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clonar e compilar open62541 com amalgamation
RUN add-apt-repository ppa:open62541-team/ppa
RUN apt-get update
RUN apt-get install -y libopen62541-1-dev
# Copiar o código fonte do servidor para o contêiner
COPY opc_server.c /usr/src/app/opc_server.c

# Compilar o servidor OPC-UA
WORKDIR /usr/src/app
RUN gcc opc_server.c -o opc_server -I /open62541/build/ -L /open62541/build/ -lopen62541

# Expor a porta 4840
EXPOSE 4840

# Comando para iniciar o servidor OPC-UA
CMD ["./opc_server"]