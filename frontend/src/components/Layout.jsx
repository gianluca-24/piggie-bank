// src/components/Layout.jsx
import React from 'react';
import { Link, Outlet, useNavigate } from 'react-router-dom';
import './css/Navbar.css'; // reuse your navbar styles

export default function Layout() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Here you can clear user session or tokens if needed
    navigate('/');
  };

  return (
    <div className="app-layout">
      <nav className="navbar">
        <div className="navbar-left">
          <h2>PiggieBank 🐷</h2>
        </div>

        <div className="navbar-right">
          <Link to="/home" className="nav-link">Home</Link>
          <Link to="/about" className="nav-link">About</Link>
          <Link to="/contact" className="nav-link">Contact</Link>
          <button className="btn logout-btn" onClick={handleLogout}>Logout</button>
        </div>
      </nav>

      {/* This is where the active page (Home, About, Contact) will be rendered */}
      <div className="page-content">
        <Outlet />
      </div>
    </div>
  );
}