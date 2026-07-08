import React, { useState } from "react";
import { predictFromLocationAPI } from "../services/api";

const AnomalyDetection = () => {
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
        "anomaly"
      );
      setResult(response);
    } catch (err) {
      setError(err.message || "Failed to detect anomaly");
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h1>Anomaly Detection</h1>
      <p>Detect unusual climate conditions using current weather and backend anomaly scoring.</p>

      <div className="grid" style={{ marginTop: 12 }}>
        <input value={latitude} onChange={(e) => setLatitude(e.target.value)} placeholder="Latitude" />
        <input value={longitude} onChange={(e) => setLongitude(e.target.value)} placeholder="Longitude" />
      </div>

      <button style={{ marginTop: 12 }} onClick={handlePredict} disabled={loading}>
        {loading ? "Analyzing..." : "Run Detection"}
      </button>

      {error && <p className="danger" style={{ marginTop: 12 }}>{error}</p>}

      {result && (
        <div className="card" style={{ marginTop: 16 }}>
          <h3>Result</h3>
          <p>Label: {result.prediction.anomaly}</p>
          <p>Score: {result.prediction.anomaly_score}</p>
          <p>Pressure: {result.weather.pressure_mb} mb</p>
          <p>Observed At: {result.weather.observed_at}</p>
        </div>
      )}
    </section>
  );
};

export default AnomalyDetection;
