// src/utils/riskCalculator.js


/**
 * Calculate Climate Risk Score
 * Input values should generally be normalized between 0 and 1.
 */


export const calculateRiskScore = ({
  temperature,
  humidity,
  rainfall,
  airQuality,
  uvIndex,
  visibility,
}) => {
  // Assign weights to each factor
  const weights = {
    temperature: 0.25,
    humidity: 0.15,
    rainfall: 0.20,
    airQuality: 0.20,
    uvIndex: 0.10,
    visibility: 0.10,
  };


  const score =
    temperature * weights.temperature +
    humidity * weights.humidity +
    rainfall * weights.rainfall +
    airQuality * weights.airQuality +
    uvIndex * weights.uvIndex +
    (1 - visibility) * weights.visibility;


  // Convert to percentage
  return Math.round(score * 100);
};


/**
 * Get Risk Category
 */
export const getRiskLevel = (score) => {
  if (score >= 80) {
    return {
      level: "Extreme",
      color: "#dc2626",
      message: "Immediate climate risk detected.",
    };
  }


  if (score >= 60) {
    return {
      level: "High",
      color: "#f97316",
      message: "High climate risk. Precautions advised.",
    };
  }


  if (score >= 40) {
    return {
      level: "Moderate",
      color: "#eab308",
      message: "Moderate climate risk.",
    };
  }


  if (score >= 20) {
    return {
      level: "Low",
      color: "#22c55e",
      message: "Low climate risk.",
    };
  }


  return {
    level: "Safe",
    color: "#16a34a",
    message: "Environmental conditions are stable.",
  };
};


/**
 * Complete Risk Assessment
 */
export const assessClimateRisk = (data) => {
  const score = calculateRiskScore(data);
  const risk = getRiskLevel(score);


  return {
    score,
    ...risk,
  };
};
 