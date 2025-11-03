import React, { useState } from 'react';
import './css/Signup.css';
import { useNavigate } from 'react-router-dom';

export default function Signup() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: '',
    surname: '',
    birthday: '',
    email: '',
    password: '',
    confirmPassword: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const calculateAge = (birthday) => {
    const birthDate = new Date(birthday);
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  if (formData.password !== formData.confirmPassword) {
    alert("Passwords do not match!");
    return;
  }

  const age = calculateAge(formData.birthday);
  if (age < 18) {
    alert("You must be at least 18 years old to sign up.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/signup", {  // 👈 your FastAPI endpoint
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: formData.name,
        surname: formData.surname,
        birthday: formData.birthday,
        email: formData.email,
        password: formData.password,
      }),
    });

if (!response.ok) {
  const errorData = await response.json().catch(() => ({})); // safely parse JSON
  const errorMessage = errorData.detail || "Unknown error occurred.";
  alert("Signup failed: " + errorMessage);
  return;
    }

    const data = await response.json();
    console.log("✅ Signup successful:", data);
    // <-- store session info in localStorage
    localStorage.setItem("user", JSON.stringify({
      user_id: data.user_id,
      name: data.name,
      email: data.email,
      token: data.token,
    }));
    // alert("Signup successful!");
    navigate("/home");
  } catch (error) {
    console.error("❌ Error during signup:", error);
    alert("Error connecting to server.");
  }
};

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto", textAlign: "left" }}>
      <h2>Sign Up</h2>

      {/* Login redirect text */}
      <p 
        className="login-redirect"
        onClick={() => navigate('/login')}
        style={{ cursor: 'pointer', color: '#007bff', textDecoration: 'underline', marginBottom: '20px' }}
      >
        Already have an account? Login here
      </p>

      <form onSubmit={handleSubmit} className="signup-form">
        <label>
          First Name:
          <input type="text" name="name" value={formData.name} onChange={handleChange} required />
        </label>

        <label>
          Last Name:
          <input type="text" name="surname" value={formData.surname} onChange={handleChange} required />
        </label>

        <label>
          Birthday:
          <input type="date" name="birthday" value={formData.birthday} onChange={handleChange} required />
        </label>

        <label>
          Email:
          <input type="email" name="email" value={formData.email} onChange={handleChange} required />
        </label>

        <label>
          Password:
          <input type="password" name="password" value={formData.password} onChange={handleChange} required />
        </label>

        <label>
          Confirm Password:
          <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
        </label>

        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}