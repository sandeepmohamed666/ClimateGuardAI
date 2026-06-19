import React, { useState } from "react";
import "./HeatwavePrediction.css";


const HeatwavePrediction = () => {
  const [temp, setTemp] = useState("");
  const [result, setResult] = useState(null);


  // Dummy logic (replace with backend ML API later)
  const handlePredict = () => {
    const temperature = parseFloat(temp);


    if (isNaN(temperature)) {
      setResult({
        status: "Invalid Input ❌",
        message: "Please enter a valid temperature value.",
      });
      return;
    }


    let status = "";
    let message = "";


    if (temperature >= 40) {
      status = "Severe Heatwave 🔴";
      message = "Extreme heat conditions detected. High risk alert!";
    } else if (temperature >= 35) {
      status = "Heatwave Warning 🟠";
      message = "High temperature detected. Stay hydrated and avoid exposure.";
    } else {
      status = "Normal Conditions 🟢";
      message = "Temperature is within safe range.";
    }


    setResult({ status, message });
  };


  return (
    <div className="hw-container">
      <div className="hw-card">
        <h1>Heatwave Prediction 🔥</h1>


        <p>
          This module predicts potential heatwave conditions based on
          temperature input and environmental trends using AI logic.
        </p>


        <div className="input-box">
          <input
            type="number"
            placeholder="Enter temperature (°C)"
            value={temp}
            onChange={(e) => setTemp(e.target.value)}
          />


          <button onClick={handlePredict}>Predict</button>
        </div>


        {result && (
          <div className="result-box">
            <h2>{result.status}</h2>
            <p>{result.message}</p>
          </div>
        )}


        <h2>🌡️ Heatwave Risk Levels</h2>
        <ul>
          <li>Below 35°C → Normal conditions</li>
          <li>35°C - 39°C → Heatwave warning</li>
          <li>40°C and above → Severe heatwave alert</li>
        </ul>


        <h2>🧠 Future Upgrade</h2>
        <p>
          This will be upgraded to a machine learning model using historical
          temperature trends, humidity, and pressure data.
        </p>
      </div>
    </div>
  );
};


export default HeatwavePrediction;
 