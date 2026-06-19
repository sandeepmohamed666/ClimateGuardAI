import React from "react";
import "./Explainability.css";


const Explainability = () => {
  return (
    <div className="exp-container">
      <div className="exp-card">
        <h1>Explainability & AI Insights 🧠</h1>


        <p>
          Climate Guard AI uses explainable machine learning techniques to
          help users understand why a prediction was made, not just the result.
        </p>


        <h2>📊 Model Transparency</h2>
        <p>
          We integrate SHAP (SHapley Additive Explanations) to break down
          each prediction into feature contributions.
        </p>


        <div className="info-box">
          <h3>What SHAP shows:</h3>
          <ul>
            <li>Which environmental factors influenced the prediction</li>
            <li>How much each feature contributed (positive or negative)</li>
            <li>Why a climate event is marked as normal or anomalous</li>
          </ul>
        </div>


        <h2>🌡️ Key Input Features</h2>
        <ul>
          <li>Temperature (°C)</li>
          <li>Humidity (%)</li>
          <li>Rainfall (mm)</li>
          <li>Air Pressure</li>
          <li>Air Quality Index (AQI)</li>
          <li>Visibility</li>
          <li>UV Index</li>
        </ul>


        <h2>⚙️ Why Explainability Matters</h2>
        <p>
          In climate risk detection, transparency is critical. It ensures that
          predictions can be trusted, validated, and acted upon in real-world
          environmental decision-making.
        </p>


        <div className="highlight">
          <p>
            “A model is only as powerful as its ability to be understood.”
          </p>
        </div>
      </div>
    </div>
  );
};


export default Explainability;

 
