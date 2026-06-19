import React from "react";

const AnomalyCard = ({
  status = "Normal",
  score = null,
  description = "",
  timestamp = null,
}) => {
  const isAnomaly = status?.toLowerCase() === "anomaly";

  return (
    <div className={`anomaly-card ${isAnomaly ? "anomaly" : "normal"}`}>
      <div className="anomaly-header">
        <h3>{isAnomaly ? "⚠️ Anomaly Detected" : "✅ Normal Condition"}</h3>
      </div>

      <div className="anomaly-body">
        <p className="anomaly-status">
          Status: <strong>{status}</strong>
        </p>

        {score !== null && (
          <p className="anomaly-score">
            Score: <strong>{score}</strong>
          </p>
        )}

        {description && (
          <p className="anomaly-desc">{description}</p>
        )}

        {timestamp && (
          <p className="anomaly-time">
            Time: {new Date(timestamp).toLocaleString()}
          </p>
        )}
      </div>
    </div>
  );
};

export default AnomalyCard; 
