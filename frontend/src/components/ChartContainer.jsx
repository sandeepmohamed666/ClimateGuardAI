import React from "react";

const ChartContainer = ({
  title,
  children,
  loading = false,
  error = null,
  height = "300px",
  actions = null,
}) => {
  return (
    <div className="chart-container">
      {/* Header */}
      <div className="chart-header">
        <h3 className="chart-title">{title}</h3>
        {actions && <div className="chart-actions">{actions}</div>}
      </div>

      {/* Body */}
      <div className="chart-body" style={{ height }}>
        {loading ? (
          <div className="chart-state">Loading chart data...</div>
        ) : error ? (
          <div className="chart-state error">
            {error || "Failed to load chart"}
          </div>
        ) : (
          children
        )}
      </div>
    </div>
  );
};

export default ChartContainer;
 