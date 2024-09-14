import React, { useEffect, useState } from 'react';
import CircuitComponent from '../components/CircuitComponent';


function Dashboard() {
    

  return (
    <div>
        <CircuitComponent SoC={0.1} BatteryVoltage={3.65} DischargerCurrent={2.3} BatteryTemperature={20.2} BatteryCurrent={1.23} ChargerVoltage={4.25} ChamberTemperature={301} ChamberSetpoint={300} DischargerEnable={1} ChargerEnable={0}/>
    </div>
  );
}

export default Dashboard;
