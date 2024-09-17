from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel
from opcua import Client
from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas

from database import SessionLocal,engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endereço do servidor OPC-UA
server_url = "opc.tcp://192.168.0.231:4840"  # Substitua pelo URL do seu servidor OPC-UA

# Identificadores dos nós que você deseja consultar
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
    "simulationTime": "ns=1;s=simulation.time"  ,
    "switchHPPC": "ns=1;s=switch.HPPC"  ,
    "switchCapacity": "ns=1;s=switch.capacity"  ,
    "switchDischarge": "ns=1;s=switch.discharge"  ,
    "switchCharge": "ns=1;s=switch.charge"  
}

async def read_opcua_data():
    client = Client(server_url)
    try:
        client.connect()
        data = {}
        for name, node_id in node_ids.items():
            node = client.get_node(node_id)
            value = node.get_value()
            data[name] = {"value": value}
        return data
    except Exception as e:
        print(f"Erro ao conectar ou ler dados: {e}")
        return None
    finally:
        client.disconnect()

@app.get("/opcua-data")
async def get_opcua_data():
    try:
        data = await read_opcua_data()
        if data is None:
            raise HTTPException(status_code=500, detail="Erro ao ler dados do servidor OPC-UA")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def write_opcua_setpoint(node_id: str, value: float):
    client = Client(server_url)
    try:
        client.connect()
        node = client.get_node(node_id)
        node.set_value(value)  # Escreve o novo valor no node
        return {"message": "Valor alterado com sucesso", "new_value": value}
    except Exception as e:
        print(f"Erro ao conectar ou escrever valor: {e}")
        return None
    finally:
        client.disconnect()

# Rota POST para alterar o valor do chamberSetpoint
@app.post("/set-chamber-setpoint")
async def set_chamber_setpoint(request: schemas.SetpointRequest):
    try:
        node_id = node_ids["chamberSetpoint"]
        result = await write_opcua_setpoint(node_id, request.value)
        if result is None:
            raise HTTPException(status_code=500, detail="Erro ao alterar o setpoint no servidor OPC-UA")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@app.get("/battery_voltage/", response_model=List[schemas.BatteryVoltageSchema])
def get_battery_voltage(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryVoltage)
    if start_date:
        query = query.filter(models.BatteryVoltage.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryVoltage.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryVoltage.id % step == 0)
    return query.order_by(models.BatteryVoltage.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_current/", response_model=List[schemas.BatteryCurrentSchema])
def get_battery_current(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryCurrent)
    if start_date:
        query = query.filter(models.BatteryCurrent.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryCurrent.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryCurrent.id % step == 0)
    return query.order_by(models.BatteryCurrent.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_temperature/", response_model=List[schemas.BatteryTemperatureSchema])
def get_battery_temperature(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryTemperature)
    if start_date:
        query = query.filter(models.BatteryTemperature.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryTemperature.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryTemperature.id % step == 0)
    return query.order_by(models.BatteryTemperature.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_soc/", response_model=List[schemas.BatterySoCSchema])
def get_battery_soc(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatterySoC)
    if start_date:
        query = query.filter(models.BatterySoC.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatterySoC.timestamp <= end_date)
    if step:
        query = query.filter(models.BatterySoC.id % step == 0)
    return query.order_by(models.BatterySoC.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_capacity/", response_model=List[schemas.BatteryCapacitySchema])
def get_battery_capacity(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryCapacity)
    if start_date:
        query = query.filter(models.BatteryCapacity.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryCapacity.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryCapacity.id % step == 0)
    return query.order_by(models.BatteryCapacity.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/charger_voltage/", response_model=List[schemas.ChargerVoltageSchema])
def get_charger_voltage(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChargerVoltage)
    if start_date:
        query = query.filter(models.ChargerVoltage.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChargerVoltage.timestamp <= end_date)
    if step:
        query = query.filter(models.ChargerVoltage.id % step == 0)
    return query.order_by(models.ChargerVoltage.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/charger_enable/", response_model=List[schemas.ChargerEnableSchema])
def get_charger_enable(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChargerEnable)
    if start_date:
        query = query.filter(models.ChargerEnable.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChargerEnable.timestamp <= end_date)
    if step:
        query = query.filter(models.ChargerEnable.id % step == 0)
    return query.order_by(models.ChargerEnable.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/discharge_current/", response_model=List[schemas.DischargeCurrentSchema])
def get_discharge_current(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.DischargeCurrent)
    if start_date:
        query = query.filter(models.DischargeCurrent.timestamp >= start_date)
    if end_date:
        query = query.filter(models.DischargeCurrent.timestamp <= end_date)
    if step:
        query = query.filter(models.DischargeCurrent.id % step == 0)
    return query.order_by(models.DischargeCurrent.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/discharger_enable/", response_model=List[schemas.DischargerEnableSchema])
def get_discharger_enable(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.DischargerEnable)
    if start_date:
        query = query.filter(models.DischargerEnable.timestamp >= start_date)
    if end_date:
        query = query.filter(models.DischargerEnable.timestamp <= end_date)
    if step:
        query = query.filter(models.DischargerEnable.id % step == 0)
    return query.order_by(models.DischargerEnable.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_voltage_esp/", response_model=List[schemas.BatteryVoltageESPSchema])
def get_battery_voltage_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryVoltageESP)
    if start_date:
        query = query.filter(models.BatteryVoltageESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryVoltageESP.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryVoltageESP.id % step == 0)
    return query.order_by(models.BatteryVoltageESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_current_esp/", response_model=List[schemas.BatteryCurrentESPSchema])
def get_battery_current_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryCurrentESP)
    if start_date:
        query = query.filter(models.BatteryCurrentESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryCurrentESP.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryCurrentESP.id % step == 0)
    return query.order_by(models.BatteryCurrentESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_temperature_esp/", response_model=List[schemas.BatteryTemperatureESPSchema])
def get_battery_temperature_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatteryTemperatureESP)
    if start_date:
        query = query.filter(models.BatteryTemperatureESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatteryTemperatureESP.timestamp <= end_date)
    if step:
        query = query.filter(models.BatteryTemperatureESP.id % step == 0)
    return query.order_by(models.BatteryTemperatureESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/battery_soc_esp/", response_model=List[schemas.BatterySoCESPSchema])
def get_battery_soc_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.BatterySoCESP)
    if start_date:
        query = query.filter(models.BatterySoCESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.BatterySoCESP.timestamp <= end_date)
    if step:
        query = query.filter(models.BatterySoCESP.id % step == 0)
    return query.order_by(models.BatterySoCESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/charger_voltage_esp/", response_model=List[schemas.ChargerVoltageESPSchema])
def get_charger_voltage_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChargerVoltageESP)
    if start_date:
        query = query.filter(models.ChargerVoltageESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChargerVoltageESP.timestamp <= end_date)
    if step:
        query = query.filter(models.ChargerVoltageESP.id % step == 0)
    return query.order_by(models.ChargerVoltageESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/charger_enable_esp/", response_model=List[schemas.ChargerEnableESPSchema])
def get_charger_enable_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChargerEnableESP)
    if start_date:
        query = query.filter(models.ChargerEnableESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChargerEnableESP.timestamp <= end_date)
    if step:
        query = query.filter(models.ChargerEnableESP.id % step == 0)
    return query.order_by(models.ChargerEnableESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/discharge_current_esp/", response_model=List[schemas.DischargeCurrentESPSchema])
def get_discharge_current_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.DischargeCurrentESP)
    if start_date:
        query = query.filter(models.DischargeCurrentESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.DischargeCurrentESP.timestamp <= end_date)
    if step:
        query = query.filter(models.DischargeCurrentESP.id % step == 0)
    return query.order_by(models.DischargeCurrentESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/discharger_enable_esp/", response_model=List[schemas.DischargerEnableESPSchema])
def get_discharger_enable_esp(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.DischargerEnableESP)
    if start_date:
        query = query.filter(models.DischargerEnableESP.timestamp >= start_date)
    if end_date:
        query = query.filter(models.DischargerEnableESP.timestamp <= end_date)
    if step:
        query = query.filter(models.DischargerEnableESP.id % step == 0)
    return query.order_by(models.DischargerEnableESP.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/chamber_setpoint/", response_model=List[schemas.ChamberSetpointSchema])
def get_chamber_setpoint(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChamberSetpoint)
    if start_date:
        query = query.filter(models.ChamberSetpoint.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChamberSetpoint.timestamp <= end_date)
    if step:
        query = query.filter(models.ChamberSetpoint.id % step == 0)
    return query.order_by(models.ChamberSetpoint.timestamp.desc()).offset(skip).limit(limit).all()

@app.get("/chamber_temperature/", response_model=List[schemas.ChamberTemperatureSchema])
def get_chamber_temperature(skip: int = 0, limit: int = 100, step: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.ChamberTemperature)
    if start_date:
        query = query.filter(models.ChamberTemperature.timestamp >= start_date)
    if end_date:
        query = query.filter(models.ChamberTemperature.timestamp <= end_date)
    if step:
        query = query.filter(models.ChamberTemperature.id % step == 0)
    return query.order_by(models.ChamberTemperature.timestamp.desc()).offset(skip).limit(limit).all()