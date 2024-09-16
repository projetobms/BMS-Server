const API_URL = 'http://localhost:8000'; // URL da sua API

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