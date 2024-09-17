import React from 'react';

const FlexHorizontal = ({ children }) => {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center', // Centraliza os itens horizontalmente
        alignItems: 'center', // Centraliza os itens verticalmente
        margin: 'auto', // Centraliza o próprio FlexHorizontal na página
        width: '100%', // O container flex ocupa 100% da largura
        height: '100%', // O container flex ocupa 100% da altura
      }}
    >
      {children}
    </div>
  );
};

export default FlexHorizontal;
