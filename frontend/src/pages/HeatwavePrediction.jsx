import React, { useState } from "react";
import { predictFromLocationAPI } from "../services/api";

const HeatwavePrediction = () => {
  const [latitude, setLatitude] = useState("28.6139");
  const [longitude, setLongitude] = useState("77.2090");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await predictFromLocationAPI(
        Number(latitude),
        Number(longitude),
        "heatwave"
      );
      setResult(response);
    } catch (err) {
      setError(err.message || "Failed to predict heatwave risk");
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h1>Heatwave Prediction</h1>
      <p>Location-driven heatwave risk prediction powered by Open-Meteo and backend scoring.</p>

      <div className="grid" style={{ marginTop: 12 }}>
        <input value={latitude} onChange={(e) => setLatitude(e.target.value)} placeholder="Latitude" />
        <input value={longitude} onChange={(e) => setLongitude(e.target.value)} placeholder="Longitude" />
      </div>

      <button style={{ marginTop: 12 }} onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict Heatwave"}
      </button>

      {error && <p className="danger" style={{ marginTop: 12 }}>{error}</p>}

      {result && (
        <div className="card" style={{ marginTop: 16 }}>
          <h3>Prediction</h3>
          <p>Risk: {result.prediction.heatwave_risk}</p>
          <p>Risk Score: {result.prediction.risk_score}</p>
          <p>Temperature: {result.weather.temperature_celsius} C</p>
          <p>Wind: {result.weather.wind_kph} km/h</p>
          <p>Observed At: {result.weather.observed_at}</p>
        </div>
      )}
    </section>
  );
};

export default HeatwavePrediction;
