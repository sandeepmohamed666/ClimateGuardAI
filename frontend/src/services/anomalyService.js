// services/anomalyService.js


/**
 * Climate Guard AI - Anomaly Detection Service
 * Handles communication with backend ML model (One-Class SVM)
 */


const API_URL = "http://localhost:5000"; // update in production


/**
 * Send climate data for anomaly prediction
 * @param {Object} inputData
 * Example:
 * {
 *   temperature: 35,
 *   humidity: 80,
 *   rainfall: 10,
 *   pressure: 1005,
 *   aqi: 120,
 *   visibility: 8,
 *   uv_index: 6
 * }
 */
export const detectAnomaly = async (inputData) => {
  try {
    const response = await fetch(`${API_URL}/predict/anomaly`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });


    if (!response.ok) {
      throw new Error("Failed to fetch anomaly prediction");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Anomaly Service Error:", error);


    // fallback mock prediction for UI testing
    return mockAnomalyPrediction(inputData);
  }
};


/**
 * Mock anomaly detection logic (frontend fallback)
 */
const mockAnomalyPrediction = (input) => {
  const score =
    (input.temperature || 0) * 0.3 +
    (input.humidity || 0) * 0.2 +
    (input.aqi || 0) * 0.25 +
    ((1000 - (input.pressure || 1000)) * 0.15) +
    (input.rainfall || 0) * 0.1;


  const isAnomaly = score > 60;


  return {
    prediction: isAnomaly ? "Anomaly" : "Normal",
    score: score.toFixed(2),
    confidence: isAnomaly ? 0.82 : 0.91,
    message: isAnomaly
      ? "Unusual climate pattern detected ⚠️"
      : "Climate conditions are stable ✅",
    factors: [
      {
        feature: "Temperature",
        value: input.temperature || 0,
        impact: 0.3,
      },
      {
        feature: "Humidity",
        value: input.humidity || 0,
        impact: 0.2,
      },
      {
        feature: "AQI",
        value: input.aqi || 0,
        impact: 0.25,
      },
      {
        feature: "Pressure",
        value: input.pressure || 1000,
        impact: 0.15,
      },
      {
        feature: "Rainfall",
        value: input.rainfall || 0,
        impact: 0.1,
      },
    ],
  };
}; 
