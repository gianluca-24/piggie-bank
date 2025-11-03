import React, { useState } from 'react';
import './css/Contact.css';

export default function Contact() {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Thank you for contacting us! We will get back to you soon.');
    setFormData({ name: '', email: '', message: '' });
  };

  return (
    <div className="contact-page">

      {/* Title wrapper */}
      <div className="contact-title-wrapper">
        <h1 className="contact-title">Contact Gocc and Suzy 💌</h1>
      </div>

      {/* Left and right content */}
      <div className="contact-content">
        <div className="contact-left">
          <p>
            We’d love to hear from you! Whether you have questions, feedback, or just want to say hi, don’t hesitate to reach out.
          </p>
          <img 
            src="../goccsuzy.jpg" 
            alt="Gocc and Suzy" 
            className="contact-image" 
          />
        </div>

        <div className="contact-right">
          <form className="contact-form" onSubmit={handleSubmit}>
            <label htmlFor="name">Name</label>
            <input 
              id="name"
              type="text" 
              name="name" 
              value={formData.name} 
              onChange={handleChange} 
              required 
            />

            <label htmlFor="email">Email</label>
            <input 
              id="email"
              type="email" 
              name="email" 
              value={formData.email} 
              onChange={handleChange} 
              required 
            />

            <label htmlFor="message">Message</label>
            <textarea 
              id="message"
              name="message" 
              rows="4" 
              value={formData.message} 
              onChange={handleChange} 
              required 
            ></textarea>

            <button type="submit">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  );
}