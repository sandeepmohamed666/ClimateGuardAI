import React from "react";

const ClimateCard = ({
  title = "Climate Metric",
  value = null,
  unit = "",
  icon = "🌍",
  description = "",
  trend = null, // "up", "down", or null
}) => {
  const getTrendColor = () => {
    if (trend === "up") return "#ef4444";
    if (trend === "down") return "#22c55e";
    return "#9ca3af";
  };

  return (
    <div className="climate-card">
      <div className="climate-header">
        <span className="climate-icon">{icon}</span>
        <h3>{title}</h3>
      </div>

      <div className="climate-body">
        {value !== null && (
          <p className="climate-value">
            <strong>
              {value} {unit}
            </strong>
          </p>
        )}

        {trend && (
          <p
            className="climate-trend"
            style={{ color: getTrendColor() }}
          >
            Trend: {trend === "up" ? "↑ Increasing" : "↓ Decreasing"}
          </p>
        )}

        {description && (
          <p className="climate-desc">{description}</p>
        )}
      </div>
    </div>
  );
};

export default ClimateCard;
 