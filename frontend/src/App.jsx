import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import DestinationList from './components/DestinationList';
import DestinationForm from './components/DestinationForm';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <nav className="navbar">
          <h1>✈️ Travel Destinations</h1>
          <div className="links">
            <Link to="/">Home</Link>
            <Link to="/create">Add Destination</Link>
          </div>
        </nav>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<DestinationList />} />
            <Route path="/create" element={<DestinationForm />} />
            <Route path="/edit/:id" element={<DestinationForm />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
