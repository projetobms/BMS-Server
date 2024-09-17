import React, { useEffect, useState } from 'react';
import CircuitComponent from '../components/CircuitComponent';
import { fetchOpcUaData } from '../services/api';
import FlexVertical from '../components/FlexVertical';
import FlexHorizontal from '../components/FlexHorizontal';
import PageTitle from '../components/PageTitle';
import ToggleButton from '../components/ToggleButton';
import LinkButton from '../components/LinkButton';

function Dashboard() {
  const [opcUaData, setOpcUaData] = useState(null);

  useEffect(() => {
    const intervalId = setInterval(async () => {
      const data = await fetchOpcUaData();
      if (data) {
        setOpcUaData(data);
      }
    }, 1000); // Atualiza a cada 100ms (0.1 segundos)

    // Limpa o intervalo quando o componente é desmontado
    return () => clearInterval(intervalId);
  }, []);

  if (!opcUaData) {
    return <div>Carregando...</div>;
  }

  return (
    <FlexVertical>
      <FlexHorizontal>
        <div style={{marginLeft:"0px",marginRight:"auto"}}>
          <PageTitle>Projeto BMS</PageTitle>
        </div>
        <div style={{marginRight:"110px",marginLeft:"auto"}}>
          <LinkButton href={"/camera"}>Camera</LinkButton>
          <LinkButton href={"/graphs"}>Gráficos</LinkButton>
        </div>
      </FlexHorizontal>
      <FlexHorizontal>
        <FlexVertical style={{marginRight:"100px"}}>
          <ToggleButton>Descarregar</ToggleButton>
          <ToggleButton>Carregar</ToggleButton>
          <ToggleButton>HPPC</ToggleButton>
          <ToggleButton>Capacidade</ToggleButton>
        </FlexVertical>
        <CircuitComponent 
          SoC={opcUaData.batterySOC.value}
          BatteryVoltage={opcUaData.batteryVoltage.value}
          DischargerCurrent={opcUaData.batteryDischargeCurrent.value}
          BatteryTemperature={opcUaData.batteryTemperature.value}
          BatteryCurrent={opcUaData.batteryCurrent.value}
          BatteryCapacity={opcUaData.batteryCapacity.value}
          ChargerVoltage={opcUaData.batteryChargerVoltage.value}
          ChamberTemperature={opcUaData.chamberTemperature.value}
          ChamberSetpoint={opcUaData.chamberSetpoint.value}
          DischargerEnable={opcUaData.batteryDischargerEnable.value}
          ChargerEnable={opcUaData.batteryChargerEnable.value}
          SimulationTime={opcUaData.simulationTime.value}
        />
      </FlexHorizontal>
    </FlexVertical>
  );
}

export default Dashboard;
