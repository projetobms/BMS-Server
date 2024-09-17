import React from 'react';

const ToggleButton = ({ children, isToggled, onToggle }) => {
  return (
    <button
      onClick={onToggle} // Função para alterar o estado quando o botão é clicado
      style={{
        backgroundColor: isToggled ? '#F5F5F5' : '#D3D3D3', 
        color: '#333',
        border: 'none',
        borderRadius: '15px',
        padding: '20px 30px',
        fontSize: '24px',
        margin: '10px',
        boxShadow: '0 2px 5px rgba(0, 0, 0, 0.2)',
        outline: isToggled ? '2px solid blue' : 'none', 
        cursor: 'pointer',
        transition: 'background-color 0.3s ease',
      }}
    >
      {children}
    </button>
  );
};

export default ToggleButton;
