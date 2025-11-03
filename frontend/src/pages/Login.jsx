import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get("email");
    const password = formData.get("password");

    try {
      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const err = await response.json();
        setError(err.detail || "Login failed");
        return;
      }

      const data = await response.json();
      console.log("✅ Login successful:", data);

      // Store session info in localStorage
      localStorage.setItem("user", JSON.stringify({
        user_id: data.user_id,
        name: data.name,
        email: data.email,
        token: data.token,
      }));

      navigate("/home");
    } catch (err) {
      console.error("❌ Error logging in:", err);
      setError("Login failed. Please try again.");
    }
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
        {error && <p style={{ color: "red" }}>{error}</p>}
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