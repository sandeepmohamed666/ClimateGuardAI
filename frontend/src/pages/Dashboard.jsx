import React, { useEffect, useState } from "react";
import { healthCheckAPI, predictFromLocationAPI } from "../services/api";

const DEFAULT_LOCATION = {
  latitude: 28.6139,
  longitude: 77.209,
};

const Dashboard = () => {
  const [health, setHealth] = useState("checking");
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        await healthCheckAPI();
        setHealth("online");
        const response = await predictFromLocationAPI(
          DEFAULT_LOCATION.latitude,
          DEFAULT_LOCATION.longitude,
          "rainfall"
        );
        setSummary(response);
      } catch (err) {
        setHealth("offline");
        setError(err.message || "Unable to load backend data");
      }
    };
    load();
  }, []);

  return (
    <section className="card">
      <h1>Dashboard</h1>
      <p>Backend status: {health}</p>
      {error && <p className="danger">{error}</p>}

      {summary && (
        <div className="grid" style={{ marginTop: 16 }}>
          <div className="card">
            <h3>Location</h3>
            <p>
              {summary.location.latitude}, {summary.location.longitude}
            </p>
          </div>
          <div className="card">
            <h3>Temperature</h3>
            <p>{summary.weather.temperature_celsius} C</p>
          </div>
          <div className="card">
            <h3>Humidity</h3>
            <p>{summary.weather.humidity}%</p>
          </div>
          <div className="card">
            <h3>Rainfall Risk</h3>
            <p>{summary.prediction.rainfall_risk}</p>
          </div>
        </div>
      )}
    </section>
  );
};

export default Dashboard;
