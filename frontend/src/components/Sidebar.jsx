import React from "react";
import { NavLink } from "react-router-dom";


const Sidebar = () => {
  const menuItems = [
    { name: "Dashboard", path: "/" },
    { name: "Climate Profiles", path: "/climate-profiles" },
    { name: "Rainfall Prediction", path: "/rainfall" },
    { name: "Heatwave Prediction", path: "/heatwave" },
    { name: "Anomaly Detection", path: "/anomaly" },
    { name: "Climate Risk Score", path: "/risk-score" },
    { name: "Explainable AI", path: "/explainable-ai" },
  ];


  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>🌍 Climate Guard AI</h2>
      </div>


      <nav className="sidebar-nav">
        {menuItems.map((item, index) => (
          <NavLink
            key={index}
            to={item.path}
            className={({ isActive }) =>
              isActive ? "nav-item active" : "nav-item"
            }
          >
            {item.name}
          </NavLink>
        ))}
      </nav>


      <div className="sidebar-footer">
        <p>AI Climate Monitoring System</p>
      </div>
    </div>
  );
};


export default Sidebar;
 