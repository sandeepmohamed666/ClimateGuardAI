import React from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";


const Dashboard = () => {
  const navigate = useNavigate();


  const cards = [
    {
      title: "Anomaly Detection",
      desc: "Detect unusual climate patterns using ML models.",
      path: "/anomaly",
      icon: "⚠️",
      color: "#ef4444",
    },
    {
      title: "Climate Profiles",
      desc: "Discover hidden climate groups using K-Means clustering.",
      path: "/climate-profiles",
      icon: "🌤️",
      color: "#22c55e",
    },
    {
      title: "Heatwave Prediction",
      desc: "Predict heatwave risk based on temperature trends.",
      path: "/heatwave",
      icon: "🔥",
      color: "#f97316",
    },
    {
      title: "Rainfall Prediction",
      desc: "Estimate rainfall probability using weather parameters.",
      path: "/rainfall",
      icon: "🌧️",
      color: "#38bdf8",
    },
    {
      title: "Climate Intelligence",
      desc: "AI-powered insights into climate trends and risks.",
      path: "/climate-intelligence",
      icon: "🧠",
      color: "#a78bfa",
    },
    {
      title: "Explainability",
      desc: "Understand AI decisions using SHAP explanations.",
      path: "/explainability",
      icon: "📊",
      color: "#34d399",
    },
  ];


  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h1>Climate Guard AI 🌍</h1>
        <p>AI-powered Climate Monitoring & Risk Detection System</p>
      </div>


      <div className="card-grid">
        {cards.map((card, index) => (
          <div
            key={index}
            className="dashboard-card"
            style={{ borderTop: `4px solid ${card.color}` }}
            onClick={() => navigate(card.path)}
          >
            <div className="icon">{card.icon}</div>
            <h2>{card.title}</h2>
            <p>{card.desc}</p>
            <button style={{ background: card.color }}>Open</button>
          </div>
        ))}
      </div>
    </div>
  );
};


export default Dashboard;
 

