from pydantic import BaseModel
from datetime import datetime

class BatteryVoltageSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatteryCurrentSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatteryTemperatureSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatterySoCSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChargerVoltageSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChargerEnableSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class DischargeCurrentSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class DischargerEnableSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatteryVoltageESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatteryCurrentESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatteryTemperatureESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class BatterySoCESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChargerVoltageESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChargerEnableESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class DischargeCurrentESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class DischargerEnableESPSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChamberSetpointSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True

class ChamberTemperatureSchema(BaseModel):
    value: float
    simulation_time: float
    timestamp: datetime

    class Config:
        orm_mode = True
