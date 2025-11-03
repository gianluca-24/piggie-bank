import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './css/Home.css';

export default function Home() {
  const location = useLocation();
  const navigate = useNavigate();
  const [name, setName] = useState("there");
  const [activeTab, setActiveTab] = useState(null); // null = no tab active

  useEffect(() => {
    const user = localStorage.getItem("user");
    if (user) {
      const parsedUser = JSON.parse(user);
      if (parsedUser.name) setName(parsedUser.name);
      else navigate('/');
    } else navigate('/');
  }, [location.state, navigate]);

  return (
    <div className="home-container">
      {/* Tabs right below navbar */}
      <div className="tabs">
        <button 
          className={`tab ${activeTab === 'networth' ? 'active' : ''}`}
          onClick={() => setActiveTab(activeTab === 'networth' ? null : 'networth')}
        >
          Net Worth
        </button>
        <button 
          className={`tab ${activeTab === 'transactions' ? 'active' : ''}`}
          onClick={() => setActiveTab(activeTab === 'transactions' ? null : 'transactions')}
        >
          Transactions
        </button>
      </div>

      {/* Default welcome content if no tab is active */}
      {!activeTab && (
        <div className="home-content">
          <h1>Welcome to PiggieBank, {name}!</h1>
          <p>Manage your savings and track your goals easily 🪙</p>
        </div>
      )}

      {/* Tab content */}
      {activeTab === 'networth' && (
        <div className="tab-content">
          <h2>Net Worth Overview</h2>
          <p>Here you will see your net worth by account.</p>
        </div>
      )}

      {activeTab === 'transactions' && (
        <div className="tab-content">
          <h2>Transactions</h2>
          <p>Here you will see and add your expenses.</p>
        </div>
      )}
    </div>
  );
}