import paho.mqtt.client as mqtt
from opcua import Client as OPCUAClient

# Tópicos para envio e recebimento
RECEIVE_TOPIC = "esp/data"
SEND_TOPIC = "esp/setpoints"

# Endereço do servidor OPC UA
opcua_url = "opc.tcp://192.168.0.231:4840"

# Nodes OPC UA
OPCUA_NODES = {
    "voltage": "ns=1;s=esp.battery.voltage",
    "temperature": "ns=1;s=esp.battery.temperature",
    "current": "ns=1;s=esp.battery.current",
    "soc": "ns=1;s=esp.battery.SOC",
    "capacity": "ns=1;s=battery.capacity",
    "batterySOC": "ns=1;s=battery.SOC",
    "simulationTime": "ns=1;s=simulation.time"
}

# Função chamada quando o cliente se conecta ao broker MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Conectado com código de resultado: {rc}")
    client.subscribe(RECEIVE_TOPIC)

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
    process_received_data(msg.payload.decode())

# Processa os dados recebidos da ESP e salva nos nodes OPC UA
def process_received_data(data):
    try:
        data_split = data.split(',')
        voltage = float(data_split[0])
        current = float(data_split[1])
        soc = float(data_split[2])
        temperature = float(data_split[3])

        print(f"Tensão: {voltage} V, Corrente: {current} A, SoC: {soc} %, Temperatura: {temperature} C")

        # Conectar ao servidor OPC UA
        opc_client = OPCUAClient(opcua_url)
        opc_client.connect()

        # Salvar dados nos nodes OPC UA
        opc_client.get_node(OPCUA_NODES["voltage"]).set_value(voltage)
        opc_client.get_node(OPCUA_NODES["current"]).set_value(current)
        opc_client.get_node(OPCUA_NODES["soc"]).set_value(soc)
        opc_client.get_node(OPCUA_NODES["temperature"]).set_value(temperature)

        print("Dados salvos no servidor OPC UA.")
        opc_client.disconnect()

    except Exception as e:
        print(f"Erro ao processar dados: {e}")

# Função para obter os setpoints dos nodes OPC UA e enviar para a ESP
def send_setpoints(client):
    try:
        # Conectar ao servidor OPC UA
        opc_client = OPCUAClient(opcua_url)
        opc_client.connect()

        # Ler valores dos nodes OPC UA
        simulation_time = opc_client.get_node(OPCUA_NODES["simulationTime"]).get_value()
        capacity = opc_client.get_node(OPCUA_NODES["capacity"]).get_value()
        soc = opc_client.get_node(OPCUA_NODES["batterySOC"]).get_value()

        message = f"{simulation_time},{capacity},{soc}"
        client.publish(SEND_TOPIC, message)
        print(f"Setpoints enviados: {message}")

        opc_client.disconnect()

    except Exception as e:
        print(f"Erro ao enviar setpoints: {e}")

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conexão ao broker MQTT (substitua pelos valores corretos)
broker_address = "192.168.0.231"
broker_port = 1883
client.connect(broker_address, broker_port, 60)

# Envia os setpoints para a ESP
send_setpoints(client)

# Inicia o loop de comunicação MQTT
client.loop_forever()
