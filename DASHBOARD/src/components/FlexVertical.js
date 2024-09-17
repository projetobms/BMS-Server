// FlexVertical.js
import React from 'react';

const FlexVertical = ({ children, style }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', ...style }}>
      {children}
    </div>
  );
};

export default FlexVertical;
