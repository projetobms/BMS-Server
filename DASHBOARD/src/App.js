import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Graphs from './pages/Graphs';
import './styles/global.css'
import Webcam from './pages/Webcam';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/graphs" element={<Graphs />} />
          <Route path="/camera" element={<Webcam />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
