import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

const Header = () => {
  return (
    <header className="header">
      <div className="header-logo">
        <img
          src="/logo.png"
          alt="Climate Guard AI Logo"
          className="logo"
        />
        <h1>Climate Guard AI</h1>
      </div>

      <nav>
        <ul className="header-links">
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/rainfall">Rainfall Risk</Link></li>
          <li><Link to="/heatwave">Heatwave Risk</Link></li>
          <li><Link to="/profiles">Climate Profiles</Link></li>
          <li><Link to="/anomaly">Anomaly Detection</Link></li>
          <li><Link to="/intelligence">Intelligence</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
 