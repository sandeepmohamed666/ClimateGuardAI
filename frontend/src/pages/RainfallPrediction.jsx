import React, { useState } from "react";
import "./RainfallPrediction.css";


const RainfallPrediction = () => {
  const [humidity, setHumidity] = useState("");
  const [pressure, setPressure] = useState("");
  const [temp, setTemp] = useState("");
  const [result, setResult] = useState(null);


  // Dummy logic (replace with ML backend API later)
  const handlePredict = () => {
    const h = parseFloat(humidity);
    const p = parseFloat(pressure);
    const t = parseFloat(temp);


    if (isNaN(h) || isNaN(p) || isNaN(t)) {
      setResult({
        status: "Invalid Input ❌",
        message: "Please enter valid numerical values.",
      });
      return;
    }


    let rainfallChance = 0;


    // Simple heuristic logic (for UI only)
    rainfallChance += h * 0.6;      // humidity impact
    rainfallChance += (1010 - p) * 0.3; // low pressure increases rain chance
    rainfallChance += (30 - t) * 0.2;   // cooler temps slightly increase chance


    if (rainfallChance < 30) {
      setResult({
        status: "Low Rainfall 🌤️",
        message: `Rain probability is low (${rainfallChance.toFixed(1)}%).`,
      });
    } else if (rainfallChance < 60) {
      setResult({
        status: "Moderate Rainfall 🌦️",
        message: `Rain probability is moderate (${rainfallChance.toFixed(1)}%).`,
      });
    } else {
      setResult({
        status: "Heavy Rainfall 🌧️",
        message: `High chance of rain (${rainfallChance.toFixed(1)}%).`,
      });
    }
  };


  return (
    <div className="rp-container">
      <div className="rp-card">
        <h1>Rainfall Prediction 🌧️</h1>


        <p>
          This module predicts rainfall probability using environmental
          parameters like humidity, pressure, and temperature.
        </p>


        <div className="input-grid">
          <input
            type="number"
            placeholder="Humidity (%)"
            value={humidity}
            onChange={(e) => setHumidity(e.target.value)}
          />


          <input
            type="number"
            placeholder="Pressure (hPa)"
            value={pressure}
            onChange={(e) => setPressure(e.target.value)}
          />


          <input
            type="number"
            placeholder="Temperature (°C)"
            value={temp}
            onChange={(e) => setTemp(e.target.value)}
          />
        </div>


        <button className="predict-btn" onClick={handlePredict}>
          Predict Rainfall
        </button>


        {result && (
          <div className="result-box">
            <h2>{result.status}</h2>
            <p>{result.message}</p>
          </div>
        )}


        <h2>🌦️ Rainfall Logic Factors</h2>
        <ul>
          <li>High humidity increases rainfall probability</li>
          <li>Low atmospheric pressure indicates storm conditions</li>
          <li>Lower temperature can support precipitation formation</li>
        </ul>


        <h2>🧠 Future Upgrade</h2>
        <p>
          This will be replaced with a trained ML regression model using
          historical weather datasets for accurate precipitation forecasting.
        </p>
      </div>
    </div>
  );
};


export default RainfallPrediction;


 