from opcua import Client
import asyncio
from sqlalchemy.orm import Session
from datetime import datetime
import time
from models import (BatteryVoltage, BatteryCurrent, BatteryTemperature, BatterySoC, 
                    ChargerVoltage, ChargerEnable, DischargeCurrent, DischargerEnable,
                    BatteryVoltageESP, BatteryCurrentESP, BatteryTemperatureESP, BatterySoCESP,
                    ChargerVoltageESP, ChargerEnableESP, DischargeCurrentESP, DischargerEnableESP,
                    ChamberSetpoint, ChamberTemperature,BatteryCapacity)
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Defina o URL do servidor OPC UA
server_url = "opc.tcp://192.168.0.231:4840"  # Substitua pelo URL do seu servidor OPC-UA

# Dicionário contendo os IDs dos nós OPC UA
node_ids = {
    "batteryVoltage": "ns=1;s=battery.voltage",
    "batteryTemperature": "ns=1;s=battery.temperature",
    "batteryCurrent": "ns=1;s=battery.current",
    "batterySOC": "ns=1;s=battery.SOC",
    "batteryCapacity": "ns=1;s=battery.capacity",
    "batteryDischargeCurrent": "ns=1;s=battery.dischargecurrent",
    "batteryChargerVoltage": "ns=1;s=battery.chargervoltage",
    "batteryChargerEnable": "ns=1;s=battery.chargerenable",
    "batteryDischargerEnable": "ns=1;s=battery.dischargerenable",
    "chamberSetpoint": "ns=1;s=chamber.setpoint",
    "chamberTemperature": "ns=1;s=chamber.temperature",
    "espBatteryVoltage": "ns=1;s=esp.battery.voltage",
    "espBatteryTemperature": "ns=1;s=esp.battery.temperature",
    "espBatteryCurrent": "ns=1;s=esp.battery.current",
    "espBatterySOC": "ns=1;s=esp.battery.SOC",
    "espBatteryDischargeCurrent": "ns=1;s=esp.battery.dischargecurrent",
    "espBatteryChargerVoltage": "ns=1;s=esp.battery.chargervoltage",
    "espBatteryChargerEnable": "ns=1;s=esp.battery.chargerenable",
    "espBatteryDischargerEnable": "ns=1;s=esp.battery.dischargerenable",
    "simulationTime": "ns=1;s=simulation.time"
}

# Função assíncrona para ler dados OPC UA mantendo a conexão
async def read_opcua_data(client):
    try:
        data = {}
        for name, node_id in node_ids.items():
            node = client.get_node(node_id)
            value = node.get_value()
            data[name] = value
        return data
    except Exception as e:
        print(f"Erro ao ler dados: {e}")
        return None

# Função para salvar os dados no banco de dados
async def save_to_db(data, db: Session):
    timestamp = datetime.utcnow()
    simulation_time = data["simulationTime"]
    
    # Inserção de cada valor nos respectivos modelos
    if "batteryVoltage" in data:
        db.add(BatteryVoltage(value=data["batteryVoltage"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryCurrent" in data:
        db.add(BatteryCurrent(value=data["batteryCurrent"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryTemperature" in data:
        db.add(BatteryTemperature(value=data["batteryTemperature"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batterySOC" in data:
        db.add(BatterySoC(value=data["batterySOC"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryCapacity" in data:
        db.add(BatteryCapacity(value=data["batteryCapacity"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryDischargeCurrent" in data:
        db.add(DischargeCurrent(value=data["batteryDischargeCurrent"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryChargerVoltage" in data:
        db.add(ChargerVoltage(value=data["batteryChargerVoltage"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryChargerEnable" in data:
        db.add(ChargerEnable(value=data["batteryChargerEnable"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "batteryDischargerEnable" in data:
        db.add(DischargerEnable(value=data["batteryDischargerEnable"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "chamberSetpoint" in data:
        db.add(ChamberSetpoint(value=data["chamberSetpoint"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "chamberTemperature" in data:
        db.add(ChamberTemperature(value=data["chamberTemperature"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryVoltage" in data:
        db.add(BatteryVoltageESP(value=data["espBatteryVoltage"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryCurrent" in data:
        db.add(BatteryCurrentESP(value=data["espBatteryCurrent"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryTemperature" in data:
        db.add(BatteryTemperatureESP(value=data["espBatteryTemperature"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatterySOC" in data:
        db.add(BatterySoCESP(value=data["espBatterySOC"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryDischargeCurrent" in data:
        db.add(DischargeCurrentESP(value=data["espBatteryDischargeCurrent"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryChargerVoltage" in data:
        db.add(ChargerVoltageESP(value=data["espBatteryChargerVoltage"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryChargerEnable" in data:
        db.add(ChargerEnableESP(value=data["espBatteryChargerEnable"], simulation_time=simulation_time, timestamp=timestamp))
    
    if "espBatteryDischargerEnable" in data:
        db.add(DischargerEnableESP(value=data["espBatteryDischargerEnable"], simulation_time=simulation_time, timestamp=timestamp))

    db.commit()

# Função para ler e salvar os dados
async def read_and_save_data():
    client = Client(server_url)
    try:
        client.connect()  # Manter a conexão aberta
        time.sleep(20)  # Aguardar antes de iniciar a leitura
        
        while True:
            db = next(get_db())  # Obter sessão do banco de dados
            data = await read_opcua_data(client)  # Reutilizar a conexão
            if data:
                await save_to_db(data, db)
            time.sleep(0.05)  # Intervalo entre as leituras

    except Exception as e:
        print(f"Erro no cliente OPC UA: {e}")
    finally:
        client.disconnect()  # Desconectar após encerrar o loop

# Inicializar o loop de eventos assíncronos
if __name__ == "__main__":
    asyncio.run(read_and_save_data())
