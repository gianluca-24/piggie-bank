import React from 'react';
import '../style.css';
import { useNavigate } from 'react-router-dom';


export default function Landing() {
  return (
    <div className="landing">
      <Navbar />
      <div className="landing-content">
        <h1>Welcome to PiggieBank</h1>
        <p>Track your expenses, visualize your net worth, and manage your investments.</p>
      </div>
    </div>
  );
}


export function Navbar() {
  const navigate = useNavigate();

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <h2>PiggieBank 🐷</h2>
      </div>
      <div className="navbar-right">
        <button className="btn login-btn" onClick={() => navigate('/login')}>
          Login
        </button>
        <button className="btn signup-btn" onClick={() => navigate('/signup')}>
          Sign Up
        </button>
      </div>
    </nav>
  );
}