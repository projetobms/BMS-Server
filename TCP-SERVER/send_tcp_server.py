import asyncio
from opcua import Client

# Definição dos nodes OPC UA e portas correspondentes
NODES = [
    "ns=1;s=switch.HPPC",
    "ns=1;s=switch.capacity",
    "ns=1;s=switch.discharge",
    "ns=1;s=switch.charge",
    "ns=1;s=battery.setpoint"
]

PORTS = [8082, 8083, 8084, 8085, 8086]

class OPCUAClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = None

    def connect(self):
        """Conecta ao servidor OPC UA."""
        try:
            self.client = Client(self.server_url)
            self.client.connect()
            print(f"Conectado ao servidor OPC UA: {self.server_url}")
        except Exception as e:
            print(f"Erro ao conectar ao servidor OPC UA: {e}")

    def disconnect(self):
        """Desconecta do servidor OPC UA."""
        if self.client:
            self.client.disconnect()
            print("Desconectado do servidor OPC UA.")

    def get_node_value(self, node_address):
        """Obtém o valor do nó OPC UA."""
        try:
            node = self.client.get_node(node_address)
            value = node.get_value()
            return value
        except Exception as e:
            print(f"Erro ao obter o valor do nó {node_address}: {e}")
            return None

async def send_data(ip, port, data):
    """Envia dados para o servidor TCP."""
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        message = "<%f>\n" % data
        writer.write(message.encode('utf-8'))
        await writer.drain()
        print(f"Mensagem enviada para a porta {port}: {message.strip()}")
        writer.close()
        await writer.wait_closed()
    except (ConnectionRefusedError, OSError) as e:
        print(f"Erro ao enviar dados para a porta {port}: {e}")

async def manage_connections(ip, ports):
    """Gerencia conexões TCP persistentes para todas as portas."""
    connections = {}
    for port in ports:
        try:
            reader, writer = await asyncio.open_connection(ip, port)
            connections[port] = writer
        except (ConnectionRefusedError, OSError) as e:
            print(f"Erro ao conectar na porta {port}: {e}")
    
    return connections

async def main():
    server_url = "opc.tcp://192.168.0.231:4840"
    opcua_client = OPCUAClient(server_url)
    opcua_client.connect()

    try:
        connections = await manage_connections("192.168.0.230", PORTS)

        while True:
            for i, node_address in enumerate(NODES):
                value = opcua_client.get_node_value(node_address)
                if value is not None:
                    port = PORTS[i % len(PORTS)]
                    writer = connections.get(port)
                    if writer:
                        message = "<%f>\n" % value
                        writer.write(message.encode('utf-8'))
                        await writer.drain()
                        print(f"Mensagem enviada para a porta {port}: {message.strip()}")
                else:
                    print(f"Não foi possível obter o valor do nó {node_address}")

            await asyncio.sleep(1)

    finally:
        opcua_client.disconnect()
        for writer in connections.values():
            writer.close()
            await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
