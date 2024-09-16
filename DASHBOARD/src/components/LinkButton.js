import React from 'react';

const LinkButton = ({ href, children }) => {
  return (
    <a
      href={href}
      style={{
        display: 'inline-block',
        backgroundColor: '#D3D3D3',
        color: '#333',
        border: 'none',
        borderRadius: '15px',
        padding: '20px 30px',
        fontSize: '24px',
        margin: '10px',
        textDecoration: 'none',
        boxShadow: '0 2px 5px rgba(0, 0, 0, 0.2)',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease',
      }}
      onMouseEnter={(e) => (e.target.style.backgroundColor = '#F5F5F5')}
      onMouseLeave={(e) => (e.target.style.backgroundColor = '#D3D3D3')}
    >
      {children}
    </a>
  );
};

export default LinkButton;
