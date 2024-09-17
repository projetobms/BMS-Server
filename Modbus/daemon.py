import serial
import struct
import asyncio
from opcua import Client

# Função para calcular o CRC16 para Modbus
def calculate_crc(data):
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if (crc & 1):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc.to_bytes(2, byteorder='little')

# Função para ler um registrador específico e interpretar o valor como um número com sinal
def read_modbus_register(register_address):
    ser = serial.Serial(
        port='COM4',        # Porta serial
        baudrate=9600,      # Taxa de transmissão
        bytesize=8,         # Tamanho do byte (geralmente 8 bits)
        parity='N',         # Paridade (N = sem paridade)
        stopbits=1,         # Bits de parada (geralmente 1)
        timeout=1           # Timeout para leitura/escrita
    )
    
    # Monta a mensagem Modbus (endereço do escravo é 0x01)
    message = bytes([0x01, 0x03]) + struct.pack('>H', register_address) + bytes([0x00, 0x01])
    
    # Calcula o CRC para a mensagem
    crc = calculate_crc(message)
    
    # Junta a mensagem completa com o CRC
    message_with_crc = message + crc
    
    # Envia a mensagem para o escravo Modbus
    ser.write(message_with_crc)
    response = ser.read(7)  # Espera-se uma resposta de 7 bytes
    
    ser.close()
    
    # Verifica se recebeu uma resposta
    if response:
        data = response[3:5]
        # Converte os bytes para um inteiro com sinal (big-endian)
        data_value = int.from_bytes(data, byteorder='big', signed=True)
        return data_value
    else:
        print(f"Nenhuma resposta do registrador {register_address}.")
        return None
def write_modbus_register(register_address, value):
    # Configuração da porta serial
    ser = serial.Serial(
        port='COM4',        # Porta serial
        baudrate=9600,      # Taxa de transmissão
        bytesize=8,         # Tamanho do byte (geralmente 8 bits)
        parity='N',         # Paridade (N = sem paridade)
        stopbits=1,         # Bits de parada (geralmente 1)
        timeout=1           # Timeout para leitura/escrita
    )
    
    # Monta a mensagem Modbus (endereço do escravo é 0x01)
    # Função 0x06 (escrever em um único registrador)
    message = bytes([0x01, 0x06]) + struct.pack('>H', register_address) + struct.pack('>h', value)
    
    # Calcula o CRC para a mensagem
    crc = calculate_crc(message)
    
    # Junta a mensagem completa com o CRC
    message_with_crc = message + crc
    
    # Envia a mensagem para o escravo Modbus
    ser.write(message_with_crc)
    print(f"Mensagem enviada: {message_with_crc.hex()}")

    # Lê a resposta (espera-se uma resposta de confirmação do escravo)
    response = ser.read(8)
    
    # Verifica se recebeu uma resposta
    if response:
        print(f"Resposta recebida: {response.hex()}")
    else:
        print("Nenhuma resposta recebida dentro do tempo limite.")
    
    # Fecha a conexão
    ser.close()


# Função assíncrona para ler e salvar os dados no OPC UA
async def read_and_save_modbus_to_opcua():
    while True:
        opcua_client = Client("opc.tcp://localhost:4840")  # URL do servidor OPC UA
        opcua_client.connect()  # Conectar ao servidor OPC UA

        lastSetpoint=-100000

        try:
            while True:
                # Lê o registrador 1 (PV - Temperatura da câmara)
                chamber_temperature = read_modbus_register(0)/10
                
                # Lê o registrador 2 (SP - Setpoint da câmara)
                chamber_setpoint = read_modbus_register(1)/10
                if(lastSetpoint!=-100000):
                    lastSetpoint=chamber_setpoint
                
                if chamber_temperature is not None and chamber_setpoint is not None:
                    # Atribuir valores lidos aos nós OPC UA
                    temperature_node = opcua_client.get_node("ns=1;s=chamber.temperature")
                    setpoint_node = opcua_client.get_node("ns=1;s=chamber.setpoint")
                    
                    if(lastSetpoint==chamber_setpoint and setpoint_node.get_value()!=chamber_setpoint):      
                        write_modbus_register(1, int(setpoint_node.get_value()*10))
                        chamber_setpoint=setpoint_node.get_value()*10
                    # Enviar os valores para os respectivos nodes
                    temperature_node.set_value(chamber_temperature)
                    setpoint_node.set_value(chamber_setpoint)
                    
                    print(f"Chamber Temperature: {chamber_temperature}")
                    print(f"Chamber Setpoint: {chamber_setpoint}")
                    lastSetpoint=chamber_setpoint
                
                # Aguarda 1 segundo antes de fazer a próxima leitura
                await asyncio.sleep(1)

        except Exception as e:
            print(f"Erro durante a comunicação: {e}")
        
        finally:
            opcua_client.disconnect()  # Desconectar do servidor OPC UA

# Inicializa o loop assíncrono para ler Modbus e enviar os dados ao OPC UA
if __name__ == "__main__":
    asyncio.run(read_and_save_modbus_to_opcua())
