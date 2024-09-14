import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Graphs from './pages/Graphs';
import './styles/global.css'

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/graphs" element={<Graphs />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
