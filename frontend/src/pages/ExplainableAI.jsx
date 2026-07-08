import React, { useState } from "react";
import { predictFromLocationAPI } from "../services/api";

const ExplainableAI = () => {
  const [latitude, setLatitude] = useState("28.6139");
  const [longitude, setLongitude] = useState("77.2090");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  const explainPrediction = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await predictFromLocationAPI(
        Number(latitude),
        Number(longitude),
        "anomaly"
      );

      const weather = response.weather;
      const contributions = [
        {
          feature: "Temperature",
          value: weather.temperature_celsius,
          impact: Math.abs(weather.temperature_celsius - 24) * 1.8,
        },
        {
          feature: "Humidity",
          value: weather.humidity,
          impact: Math.abs(weather.humidity - 55) * 0.8,
        },
        {
          feature: "Precipitation",
          value: weather.precip_mm,
          impact: weather.precip_mm * 1.2,
        },
        {
          feature: "Pressure",
          value: weather.pressure_mb,
          impact: Math.max(0, 1000 - weather.pressure_mb) * 0.4,
        },
        {
          feature: "Wind",
          value: weather.wind_kph,
          impact: Math.max(0, weather.wind_kph - 20) * 0.9,
        },
      ].sort((a, b) => b.impact - a.impact);

      setResult({
        label: response.prediction.anomaly,
        score: response.prediction.anomaly_score,
        confidence: response.prediction.confidence,
        contributions,
      });
    } catch (err) {
      setError(err.message || "Failed to generate explanation");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h1>Explainable AI</h1>
      <p>Understand which weather features drove the anomaly model decision.</p>

      <div className="grid" style={{ marginTop: 12 }}>
        <input value={latitude} onChange={(e) => setLatitude(e.target.value)} placeholder="Latitude" />
        <input value={longitude} onChange={(e) => setLongitude(e.target.value)} placeholder="Longitude" />
      </div>

      <button style={{ marginTop: 12 }} onClick={explainPrediction} disabled={loading}>
        {loading ? "Explaining..." : "Generate Explanation"}
      </button>

      {error && <p className="danger" style={{ marginTop: 12 }}>{error}</p>}

      {result && (
        <div className="card" style={{ marginTop: 16 }}>
          <h3>Prediction: {result.label}</h3>
          <p>Anomaly Score: {result.score}</p>
          <p>Confidence: {result.confidence}%</p>
          <hr style={{ margin: "12px 0", opacity: 0.2 }} />
          <h3>Top Feature Contributions</h3>
          {result.contributions.map((item) => (
            <p key={item.feature}>
              {item.feature}: value={Number(item.value).toFixed(2)}, impact={item.impact.toFixed(2)}
            </p>
          ))}
        </div>
      )}
    </section>
  );
};

export default ExplainableAI;
