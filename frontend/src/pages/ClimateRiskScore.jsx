import React, { useState } from "react";
import { predictFromLocationAPI } from "../services/api";

const ClimateRiskScore = () => {
  const [latitude, setLatitude] = useState("28.6139");
  const [longitude, setLongitude] = useState("77.2090");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  const calculateRisk = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const [rainfall, heatwave, anomaly] = await Promise.all([
        predictFromLocationAPI(Number(latitude), Number(longitude), "rainfall"),
        predictFromLocationAPI(Number(latitude), Number(longitude), "heatwave"),
        predictFromLocationAPI(Number(latitude), Number(longitude), "anomaly"),
      ]);

      const rainfallScore = Number(rainfall?.prediction?.probability || 0);
      const heatwaveScore = Number(heatwave?.prediction?.risk_score || 0);
      const anomalyScore = Number(anomaly?.prediction?.anomaly_score || 0);

      const overall = Math.round(
        rainfallScore * 0.35 + heatwaveScore * 0.4 + anomalyScore * 0.25
      );

      const category =
        overall >= 75
          ? "Extreme"
          : overall >= 55
          ? "High"
          : overall >= 35
          ? "Moderate"
          : "Low";

      setResult({
        location: { latitude, longitude },
        overall,
        category,
        factors: {
          rainfall: rainfallScore,
          heatwave: heatwaveScore,
          anomaly: anomalyScore,
        },
      });
    } catch (err) {
      setError(err.message || "Failed to calculate climate risk score");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h1>Climate Risk Score</h1>
      <p>Combined risk index derived from rainfall, heatwave, and anomaly signals.</p>

      <div className="grid" style={{ marginTop: 12 }}>
        <input value={latitude} onChange={(e) => setLatitude(e.target.value)} placeholder="Latitude" />
        <input value={longitude} onChange={(e) => setLongitude(e.target.value)} placeholder="Longitude" />
      </div>

      <button style={{ marginTop: 12 }} onClick={calculateRisk} disabled={loading}>
        {loading ? "Calculating..." : "Calculate Risk Score"}
      </button>

      {error && <p className="danger" style={{ marginTop: 12 }}>{error}</p>}

      {result && (
        <div className="card" style={{ marginTop: 16 }}>
          <h3>Overall Climate Risk: {result.overall}/100</h3>
          <p>Category: {result.category}</p>
          <p>Location: {result.location.latitude}, {result.location.longitude}</p>
          <hr style={{ margin: "12px 0", opacity: 0.2 }} />
          <p>Rainfall Contribution: {result.factors.rainfall}</p>
          <p>Heatwave Contribution: {result.factors.heatwave}</p>
          <p>Anomaly Contribution: {result.factors.anomaly}</p>
        </div>
      )}
    </section>
  );
};

export default ClimateRiskScore;
