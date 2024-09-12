from sqlalchemy import Column, Float, DateTime, Integer
from database import Base
from datetime import datetime

class BatteryVoltage(Base):
    __tablename__ = 'battery_voltage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatteryCurrent(Base):
    __tablename__ = 'battery_current'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatteryTemperature(Base):
    __tablename__ = 'battery_temperature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatterySoC(Base):
    __tablename__ = 'battery_soc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChargerVoltage(Base):
    __tablename__ = 'charger_voltage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChargerEnable(Base):
    __tablename__ = 'charger_enable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DischargeCurrent(Base):
    __tablename__ = 'discharge_current'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DischargerEnable(Base):
    __tablename__ = 'discharger_enable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatteryVoltageESP(Base):
    __tablename__ = 'battery_voltage_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatteryCurrentESP(Base):
    __tablename__ = 'battery_current_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatteryTemperatureESP(Base):
    __tablename__ = 'battery_temperature_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class BatterySoCESP(Base):
    __tablename__ = 'battery_soc_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChargerVoltageESP(Base):
    __tablename__ = 'charger_voltage_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChargerEnableESP(Base):
    __tablename__ = 'charger_enable_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DischargeCurrentESP(Base):
    __tablename__ = 'discharge_current_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DischargerEnableESP(Base):
    __tablename__ = 'discharger_enable_esp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChamberSetpoint(Base):
    __tablename__ = 'chamber_setpoint'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChamberTemperature(Base):
    __tablename__ = 'chamber_temperature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    simulation_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
