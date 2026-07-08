import React, { useState } from "react";
import { predictFromLocationAPI } from "../services/api";

const ClimateProfiles = () => {
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
        "profile"
      );
      setResult(response);
    } catch (err) {
      setError(err.message || "Failed to classify climate profile");
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h1>Climate Profiles</h1>
      <p>Classify current location into a climate profile using backend clustering logic.</p>

      <div className="grid" style={{ marginTop: 12 }}>
        <input value={latitude} onChange={(e) => setLatitude(e.target.value)} placeholder="Latitude" />
        <input value={longitude} onChange={(e) => setLongitude(e.target.value)} placeholder="Longitude" />
      </div>

      <button style={{ marginTop: 12 }} onClick={handlePredict} disabled={loading}>
        {loading ? "Classifying..." : "Classify Profile"}
      </button>

      {error && <p className="danger" style={{ marginTop: 12 }}>{error}</p>}

      {result && (
        <div className="card" style={{ marginTop: 16 }}>
          <h3>Profile</h3>
          <p>{result.prediction.climate_cluster}</p>
          <p>Temperature: {result.weather.temperature_celsius} C</p>
          <p>Humidity: {result.weather.humidity}%</p>
          <p>Precipitation: {result.weather.precip_mm} mm</p>
        </div>
      )}
    </section>
  );
};

export default ClimateProfiles;
