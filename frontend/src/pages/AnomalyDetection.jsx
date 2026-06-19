import React, { useState } from "react";
import "./AnomalyDetection.css";


const AnomalyDetection = () => {
  const [result, setResult] = useState(null);


  // Dummy prediction function (replace with backend API call)
  const handleDetect = () => {
    const isAnomaly = Math.random() > 0.5;


    setResult({
      status: isAnomaly ? "Anomaly Detected ⚠️" : "Normal Condition ✅",
      description: isAnomaly
        ? "Extreme climate pattern detected. This may indicate unusual environmental behavior."
        : "Environmental conditions are stable and within normal range.",
    });
  };


  return (
    <div className="ad-container">
      <div className="ad-card">
        <h1>Anomaly Detection 🔍</h1>


        <p>
          This module uses machine learning (One-Class SVM) to detect unusual
          climate conditions based on environmental inputs.
        </p>


        <button className="detect-btn" onClick={handleDetect}>
          Run Detection
        </button>


        {result && (
          <div
            className={
              result.status.includes("Anomaly")
                ? "result-box anomaly"
                : "result-box normal"
            }
          >
            <h2>{result.status}</h2>
            <p>{result.description}</p>
          </div>
        )}


        <h2>📌 How it works</h2>
        <ul>
          <li>Input environmental parameters (temperature, AQI, humidity)</li>
          <li>Data is scaled using StandardScaler</li>
          <li>One-Class SVM detects deviations from normal patterns</li>
          <li>System classifies result as Normal or Anomaly</li>
        </ul>


        <h2>🌡️ Example Anomalies</h2>
        <ul>
          <li>Extreme heatwaves</li>
          <li>Sudden air quality drop</li>
          <li>Unusual rainfall spikes</li>
          <li>Rare atmospheric pressure shifts</li>
        </ul>
      </div>
    </div>
  );
};


export default AnomalyDetection;
 

