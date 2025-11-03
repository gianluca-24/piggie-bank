import React from 'react';
import './css/About.css';

export default function About() {
  return (
    <div className="about-page">
      {/* Overall Introduction */}
      <section className="about-intro">
        <h1>About PiggieBank 🐷</h1>
        <p>
          PiggieBank is your friendly savings companion — built to help you manage your goals,
          stay motivated, and make saving simple and fun.  
          Meet the creators who made this project possible!
        </p>
      </section>

      {/* Split Section for Gocc and Suzy */}
      <section className="about-team">
        {/* Gocc Section */}
        <div className="team-member">
          <img src="/gocc.jpg" alt="Gocc" className="member-photo" />
          <h2>Gocc 🧌</h2>
          <p>
    Based in Munich 🇩🇪<br />
    MSc in Data Science <br />
    BSc in Engineering in Computer Science <br /><br />
          </p>
        </div>

        {/* Suzy Section */}
        <div className="team-member">
          <img src="/suzy.jpg" alt="Suzy" className="member-photo" />
          <h2>Suzy 🤠</h2>
          <p>
    Based in Rome 🇮🇹<br />
    MSc in Data Science <br />
    BSc in Management Statistics <br /><br />
          </p>
        </div>
      </section>
    </div>
  );
}