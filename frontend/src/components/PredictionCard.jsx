import React from "react";

const PredictionCard = ({
  title = "Prediction",
  value = null,
  label = "",
  confidence = null,
  unit = "",
  description = "",
  timestamp = null,
}) => {
  return (
    <div className="prediction-card">
      <div className="prediction-header">
        <h3>{title}</h3>
        {label && <span className="prediction-label">{label}</span>}
      </div>

      <div className="prediction-body">
        {value !== null && (
          <p className="prediction-value">
            <strong>
              {value} {unit}
            </strong>
          </p>
        )}

        {confidence !== null && (
          <p className="prediction-confidence">
            Confidence: <strong>{confidence}%</strong>
          </p>
        )}

        {description && (
          <p className="prediction-desc">{description}</p>
        )}

        {timestamp && (
          <p className="prediction-time">
            Time: {new Date(timestamp).toLocaleString()}
          </p>
        )}
      </div>
    </div>
  );
};

export default PredictionCard; 
