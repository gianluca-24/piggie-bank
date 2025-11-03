import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export default function Home() {
  const location = useLocation();
  const navigate = useNavigate();
  const [name, setName] = useState("there");

  useEffect(() => {
    // Try to get user from localStorage
    const user = localStorage.getItem("user");

    if (user) {
      const parsedUser = JSON.parse(user);
      if (parsedUser.name) {
        setName(parsedUser.name);
      } else {
        // No name found, redirect
        navigate('/');
      }
    } else {
      // No user found at all, redirect
      navigate('/');
    }
  }, [location.state, navigate]);

  return (
    <div className="home-content">
      <h1>Welcome to PiggieBank, {name}!</h1>
      <p>Manage your savings and track your goals easily 🪙</p>
    </div>
  );
}