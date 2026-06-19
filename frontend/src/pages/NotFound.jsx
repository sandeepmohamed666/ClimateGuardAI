import React from "react";
import "./About.css";


const About = () => {
  return (
    <div className="about-container">
      <div className="about-card">
        <h1>About Climate Guard AI 🌍</h1>


        <p>
          Climate Guard AI is an intelligent climate monitoring and anomaly
          detection system designed to analyze environmental patterns and
          identify unusual or extreme weather conditions.
        </p>


        <h2>🚀 Our Mission</h2>
        <p>
          To leverage machine learning and data-driven insights to help
          detect climate risks early and support better environmental
          decision-making.
        </p>


        <h2>🧠 How It Works</h2>
        <ul>
          <li>Collects environmental data (temperature, humidity, etc.)</li>
          <li>Processes and scales features for analysis</li>
          <li>Uses ML models like One-Class SVM for anomaly detection</li>
          <li>Classifies normal vs extreme climate patterns</li>
        </ul>


        <h2>🌱 Key Features</h2>
        <ul>
          <li>Real-time anomaly detection</li>
          <li>Interactive dashboard</li>
          <li>Climate profiling using clustering</li>
          <li>Explainable AI insights (SHAP integration)</li>
        </ul>


        <p className="footer-text">
          Built with ❤️ for a safer and smarter planet.
        </p>
      </div>
    </div>
  );
};


export default About;

 
