import socket
import asyncio
from opcua import Client

# Dicionário que mapeia a posição dos dados para os nodes OPC UA
NODE_ADDRESSES = {
    0: "ns=1;s=battery.voltage",
    1: "ns=1;s=battery.temperature",
    2: "ns=1;s=battery.current",
    3: "ns=1;s=battery.SOC",
    4: "ns=1;s=battery.dischargecurrent",
    5: "ns=1;s=battery.chargervoltage",
    6: "ns=1;s=battery.chargerenable",
    7: "ns=1;s=battery.dischargerenable",
    8: "ns=1;s=simulation.time"
}

# Função para enviar dados para o servidor OPC UA
async def send_to_opcua(data):
    opcua_client = Client("opc.tcp://192.168.0.231:4840")  # URL do servidor OPC UA
    opcua_client.connect()  # Conectar ao servidor OPC UA

    try:
        # Itera sobre os dados e atualiza os nós OPC UA correspondentes
        for i, value in enumerate(data):
            if i in NODE_ADDRESSES:
                node_address = NODE_ADDRESSES[i]
                node = opcua_client.get_node(node_address)
                node.set_value(value)
                print(f"Dados enviados para {node_address}: {value}")

    except Exception as e:
        print(f"Erro durante a comunicação OPC UA: {e}")
    
    finally:
        opcua_client.disconnect()  # Desconectar do servidor OPC UA

async def start_tcp_server(host='0.0.0.0', port=8081):
    # Cria um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Liga o socket ao endereço e porta especificados
        server_socket.bind((host, port))
        # Começa a escutar por conexões
        server_socket.listen()

        print(f"Servidor TCP/IP iniciado em {host}:{port}. Aguardando conexões...")

        while True:
            # Aceita uma nova conexão
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conectado por {addr}")

                buffer = b''  # Buffer para armazenar dados recebidos
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    # Adiciona os dados recebidos ao buffer
                    buffer += data

                    # Processa as mensagens delimitadas por '<' e '>'
                    while b'<' in buffer and b'>' in buffer:
                        start_idx = buffer.find(b'<')
                        end_idx = buffer.find(b'>', start_idx)

                        if start_idx != -1 and end_idx != -1:
                            # Extrai a mensagem entre '<' e '>'
                            message = buffer[start_idx + 1:end_idx].decode('utf-8')
                            
                            # Remove a mensagem do buffer
                            buffer = buffer[end_idx + 1:]

                            # Divide a mensagem usando ':' como delimitador
                            elements = message.split(':')
                            
                            # Converte cada elemento para float
                            try:
                                converted_elements = [float(element) for element in elements]
                                print(f"Recebido e convertido: {converted_elements}", flush=True)

                                # Envia os dados para o OPC UA
                                await send_to_opcua(converted_elements)

                            except ValueError as e:
                                print(f"Erro ao converter dados: {e}", flush=True)

if __name__ == "__main__":
    asyncio.run(start_tcp_server())
