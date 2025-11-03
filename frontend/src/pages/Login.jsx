import React from 'react';
import { useNavigate } from 'react-router-dom';
import './css/Login.css';

export default function Login() {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your real authentication logic here
    navigate('/home');
  };

  return (
    <div className="login-page">
      <h1>Login to PiggieBank</h1>
      <form className="login-form" onSubmit={handleSubmit}>
        <label>Email:</label>
        <input type="email" name="email" required />

        <label>Password:</label>
        <input type="password" name="password" required />

        <button type="submit" className="btn login-submit-btn">
          Login
        </button>
        <p 
          className="signup-text"
          onClick={() => navigate('/signup')}
        >
          Sign up here
        </p>
      </form>
    </div>
  );
}