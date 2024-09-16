import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { fetchData } from '../services/api';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import FlexVertical from '../components/FlexVertical';
import FlexHorizontal from '../components/FlexHorizontal';
import PageTitle from '../components/PageTitle';
import LinkButton from '../components/LinkButton';
import '../styles/graphs.css'

// Registrar os componentes necessários do Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

function Graphs() {
  const [graphData, setGraphData] = useState([]);
  const [startDate, setStartDate] = useState('2024-09-15T00:00:00');
  const [endDate, setEndDate] = useState('2024-09-15T23:59:59');
  const [limit, setLimit] = useState(9000);
  const [step, setStep] = useState(100);
  const [selectedData, setSelectedData] = useState({
    battery_voltage: false,
    battery_current: false,
    battery_temperature: false,
    battery_soc: false,
    charger_voltage: false,
    charger_enable: false,
    discharge_current: false,
    discharger_enable: false,
    battery_voltage_esp: false,
    battery_current_esp: false,
    battery_temperature_esp: false,
    battery_soc_esp: false,
    charger_voltage_esp: false,
    charger_enable_esp: false,
    discharge_current_esp: false,
    discharger_enable_esp: false,
    chamber_setpoint: false,
    chamber_temperature: false,
  });

  const dataOptions = {
    battery_voltage: { url: '/battery_voltage/', label: 'Battery Voltage', color: 'rgba(75, 192, 192, 1)' },
    battery_current: { url: '/battery_current/', label: 'Battery Current', color: 'rgba(255, 99, 132, 1)' },
    battery_temperature: { url: '/battery_temperature/', label: 'Battery Temperature', color: 'rgba(255, 159, 64, 1)' },
    battery_soc: { url: '/battery_soc/', label: 'Battery SOC', color: 'rgba(153, 102, 255, 1)' },
    charger_voltage: { url: '/charger_voltage/', label: 'Charger Voltage', color: 'rgba(54, 162, 235, 1)' },
    charger_enable: { url: '/charger_enable/', label: 'Charger Enable', color: 'rgba(255, 206, 86, 1)' },
    discharge_current: { url: '/discharge_current/', label: 'Discharge Current', color: 'rgba(75, 192, 192, 1)' },
    discharger_enable: { url: '/discharger_enable/', label: 'Discharger Enable', color: 'rgba(153, 102, 255, 1)' },
    battery_voltage_esp: { url: '/battery_voltage_esp/', label: 'Battery Voltage ESP', color: 'rgba(255, 205, 86, 1)' },
    battery_current_esp: { url: '/battery_current_esp/', label: 'Battery Current ESP', color: 'rgba(54, 235, 162, 1)' },
    battery_temperature_esp: { url: '/battery_temperature_esp/', label: 'Battery Temperature ESP', color: 'rgba(99, 255, 132, 1)' },
    battery_soc_esp: { url: '/battery_soc_esp/', label: 'Battery SOC ESP', color: 'rgba(162, 54, 235, 1)' },
    charger_voltage_esp: { url: '/charger_voltage_esp/', label: 'Charger Voltage ESP', color: 'rgba(235, 54, 162, 1)' },
    charger_enable_esp: { url: '/charger_enable_esp/', label: 'Charger Enable ESP', color: 'rgba(64, 159, 255, 1)' },
    discharge_current_esp: { url: '/discharge_current_esp/', label: 'Discharge Current ESP', color: 'rgba(255, 99, 86, 1)' },
    discharger_enable_esp: { url: '/discharger_enable_esp/', label: 'Discharger Enable ESP', color: 'rgba(192, 192, 75, 1)' },
    chamber_setpoint: { url: '/chamber_setpoint/', label: 'Chamber Setpoint', color: 'rgba(255, 86, 159, 1)' },
    chamber_temperature: { url: '/chamber_temperature/', label: 'Chamber Temperature', color: 'rgba(86, 255, 206, 1)' },
  };
  

  const fetchGraphData = async () => {
    try {
      const dataPromises = Object.keys(selectedData).filter(key => selectedData[key]).map(key => {
        const { url } = dataOptions[key];
        return fetchData(url, {
          start_date: startDate,
          end_date: endDate,
          limit: limit,
          step: step,
        }).then(data => ({ key, data: data.reverse() }));
      });

      const results = await Promise.all(dataPromises);

      const combinedData = results.reduce((acc, { key, data }) => {
        acc[key] = data;
        return acc;
      }, {});

      setGraphData(combinedData);
    } catch (error) {
      console.error('Erro ao buscar dados do gráfico:', error);
    }
  };

  useEffect(() => {
    fetchGraphData(); // Fetch initial data

    const intervalId = setInterval(() => {
      fetchGraphData();
    }, 1000); // Atualiza a cada 10 segundos, ajuste conforme necessário

    return () => clearInterval(intervalId); // Limpa o intervalo ao desmontar o componente
  }, [startDate, endDate, limit, step, selectedData]);

  const chartData = {
    labels: graphData[Object.keys(graphData)[0]]?.map(item => item.simulation_time) || [], // Usa o tempo de simulação como rótulo
    datasets: Object.keys(graphData).map(key => {
      const { label, color } = dataOptions[key];
      return {
        label: label,
        data: graphData[key].map(item => item.value),
        borderColor: color,
        backgroundColor: color.replace('1)', '0.2)'),
        pointRadius: 0, // Remove os círculos dos pontos
        hitRadius: 10, // Aumenta a área sensível ao mouse para o tooltip
        hoverRadius: 5, // Tamanho do círculo quando o ponto é hover
        fill: true,
      };
    }),
  };

  const chartOptions = {
    responsive: true,
    animation: {
      duration: 0 
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: function(tooltipItem) {
            return `${tooltipItem.dataset.label}: ${tooltipItem.raw}`;
          }
        }
      },
      legend: {
        labels: {
          color: '#FFFFFF', 
        },
      },
    },
    scales: {
      x: {
        type: 'category',
        title: {
          display: true,
          text: 'Tempo de simulação',
          color: "white"
        },
        ticks: {
          color: '#FFFFFF', // Cor dos rótulos do eixo X
        },
      },
      y: {
        title: {
          display: true,
          text: 'Valor',
          color: "white"
        },
        ticks: {
          color: '#FFFFFF', // Cor dos rótulos do eixo X
        },
        beginAtZero: true,
      },
    },
  };

  return (
        <FlexVertical>
          
        <FlexHorizontal>
          <div style={{marginLeft:"0px",marginRight:"auto"}}>
            <PageTitle>Projeto BMS</PageTitle>
          </div>
          <div style={{marginRight:"110px",marginLeft:"auto"}}>
            <LinkButton href={"/"}>Voltar</LinkButton>
          </div>
        </FlexHorizontal>
       
          <FlexHorizontal>
            <FlexVertical>
              {Object.keys(dataOptions).map(key => (
                <label key={key} style={{ fontFamily: 'Roboto, Arial, sans-serif', display: 'flex', alignItems: 'center', marginBottom: '10px' }}>
                  <input
                    type="checkbox"
                    checked={selectedData[key]}
                    onChange={() => setSelectedData(prevState => ({
                      ...prevState,
                      [key]: !prevState[key]
                    }))}
                    style={{
                      appearance: 'none',
                      width: '18px',
                      height: '18px',
                      border: '2px solid #ccc',
                      borderRadius: '4px',
                      marginRight: '10px',
                      position: 'relative',
                      cursor: 'pointer',
                      outline: 'none',
                      backgroundColor: selectedData[key] ? '#4caf50' : '#fff',
                    }}
                  />
                  <div
                    style={{
                      width: '15px',
                      height: '15px',
                      backgroundColor: dataOptions[key].color,
                      marginRight: '10px',
                      borderRadius: '2px'
                    }}
                  ></div>
                  {dataOptions[key].label}
                </label>
              ))}
           </FlexVertical>
           <FlexVertical>
            <FlexHorizontal>
              <label className="styled-label">
                Data de Início:
                <input
                  className="styled-input"
                  type="datetime-local"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                />
              </label>
              <label className="styled-label">
                Data de Fim:
                <input
                  className="styled-input"
                  type="datetime-local"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                />
              </label>
              <label className="styled-label">
                Limite:
                <input
                  className="styled-input"
                  type="number"
                  value={limit}
                  onChange={(e) => setLimit(Number(e.target.value))}
                />
              </label>
              <label className="styled-label">
                Passo:
                <input
                  className="styled-input"
                  type="number"
                  value={step}
                  onChange={(e) => setStep(Number(e.target.value))}
                />
              </label>
            </FlexHorizontal>
              <div style={{ width: '1000px', maxHeight: '70vh', overflow: 'auto' }}>
                <Line data={chartData} options={chartOptions} />
              </div>
           </FlexVertical>
          </FlexHorizontal>
        </FlexVertical>
  );
}

export default Graphs;
