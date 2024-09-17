const API_URL = 'https://labnvh.online/api'; // URL da sua API

export const fetchOpcUaData = async () => {
  try {
    const response = await fetch(`${API_URL}/opcua-data`);
    if (!response.ok) {
      throw new Error('Erro ao buscar dados da API');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Erro ao buscar dados da API:', error);
    return null;
  }
};


export const fetchData = async (endpoint, params = {}) => {
  try {
    const url = new URL(`${API_URL}${endpoint}`);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Erro ao buscar dados da API no endpoint ${endpoint}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error(`Erro ao buscar dados da API: ${error}`);
    return null;
  }
};

export const writeOpcUaData = async (nodeName, value) => {
  console.log(nodeName)
  try {
    const response = await fetch(`${API_URL}/opcua-write/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        node_name: nodeName,  // Certifique-se de que o nome do campo está correto
        value: value,
      }),
    });

    if (!response.ok) {
      throw new Error('Erro ao escrever dados no OPC UA');
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Erro ao escrever dados no OPC UA:', error);
    return null;
  }
};
