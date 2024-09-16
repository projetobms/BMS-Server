// PageTitle.js
import React from 'react';

const PageTitle = ({ children }) => {
  return (
    <h1 style={{ fontWeight: '300', fontSize: '40px',fontFamily: 'Roboto, Arial, sans-serif', marginLeft:"110px" }}>
      {children}
    </h1>
  );
};

export default PageTitle;
