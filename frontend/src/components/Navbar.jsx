import React from "react";
import { Link } from "react-router-dom";
import "../assets/styles/Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
        <h2>Climate Guard AI</h2>
      </div>

      <ul className="nav-links">
        <li>
          <Link to="/">Dashboard</Link>
        </li>
        <li>
          <Link to="/rainfall">Rainfall Risk</Link>
        </li>
        <li>
          <Link to="/heatwave">Heatwave Risk</Link>
        </li>
        <li>
          <Link to="/climate-profiles">Climate Profiles</Link>
        </li>
        <li>
          <Link to="/anomaly">Anomaly Detection</Link>
        </li>
        <li>
          <Link to="/risk-score">Risk Score</Link>
        </li>
        <li>
          <Link to="/explainable-ai">Explainable AI</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
