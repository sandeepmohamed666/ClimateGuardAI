import React from "react";

const RiskGauge = ({
  score = 0,
  size = 160,
  label = "Risk Level",
}) => {
  const normalizedScore = Math.max(0, Math.min(score, 100));

  const getRiskColor = (value) => {
    if (value >= 80) return "#ef4444"; // Critical
    if (value >= 60) return "#f97316"; // High
    if (value >= 40) return "#facc15"; // Moderate
    return "#22c55e"; // Low
  };

  const color = getRiskColor(normalizedScore);
  const strokeWidth = 12;
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;

  const progress = (normalizedScore / 100) * circumference;
  const offset = circumference - progress;

  return (
    <div className="risk-gauge-wrapper">
      <svg width={size} height={size} className="risk-gauge">
        {/* Background Circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="#374151"
          strokeWidth={strokeWidth}
          fill="none"
        />

        {/* Progress Circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={color}
          strokeWidth={strokeWidth}
          fill="none"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          transform={`rotate(-90 ${size / 2} ${size / 2})`}
        />

        {/* Text */}
        <text
          x="50%"
          y="50%"
          textAnchor="middle"
          dy="0.3em"
          fontSize="20"
          fill="#e5e7eb"
          fontWeight="bold"
        >
          {normalizedScore}%
        </text>
      </svg>

      <p className="risk-gauge-label">{label}</p>
    </div>
  );
};

export default RiskGauge;
 