import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      {/* Logo Section */}
      <div className="navbar-logo">
        <img
          src="/logo.png"
          alt="Climate Guard AI Logo"
          className="logo"
        />
        <h2>Climate Guard AI</h2>
      </div>

      {/* Navigation Links */}
      <ul className="navbar-links">
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
          <Link to="/profiles">Climate Profiles</Link>
        </li>

        <li>
          <Link to="/anomaly">Anomaly Detection</Link>
        </li>

        <li>
          <Link to="/intelligence">Intelligence</Link>.logo {
  width: 45px;
  height: 45px;
}

.navbar-logo h2 {
  color: #38bdf8;
  font-size: 24px;
}

.navbar-links {
  display: flex;
  gap: 25px;
  list-style: none;
}

.navbar-links a {
  text-decoration: none;
  color: white;
  font-weight: 500;
  transition: 0.3s;
}

.navbar-links a:hover {
  color: #38bdf8;
}
 
