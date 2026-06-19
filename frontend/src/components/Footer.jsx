import React from "react";

const Footer = () => {
  return (
    <footer className="app-footer">
      <div className="footer-content">
        <div className="footer-left">
          <h4>Climate Guard AI</h4>
          <p>AI-powered climate intelligence & anomaly detection system</p>
        </div>

        <div className="footer-center">
          <p>© {new Date().getFullYear()} Climate Guard AI</p>
          <p>Built with React • ML Models • Flask/FastAPI</p>
        </div>

        <div className="footer-right">
          <a href="#dashboard">Dashboard</a>
          <a href="#profiles">Profiles</a>
          <a href="#predictions">Predictions</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
 