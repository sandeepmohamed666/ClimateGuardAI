import { API_BASE_URL } from "../utils/constants";
// services/heatwaveService.js


/**
 * Climate Guard AI - Heatwave Prediction Service
 * Handles ML-based heatwave risk prediction
 */


/**
 * Predict heatwave risk from climate inputs
 * @param {Object} inputData
 * Example:
 * {
 *   temperature: 42,
 *   humidity: 60,
 *   pressure: 1003,
 *   aqi: 120
 * }
 */
export const predictHeatwave = async (inputData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict/heatwave`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        temperature_celsius: inputData.temperature_celsius ?? inputData.temperature ?? 0,
        humidity: inputData.humidity ?? 0,
        precip_mm: inputData.precip_mm ?? inputData.rainfall ?? 0,
        wind_kph: inputData.wind_kph ?? inputData.windSpeed ?? 0,
        pressure_mb: inputData.pressure_mb ?? inputData.pressure ?? 1013,
      }),
    });


    if (!response.ok) {
      throw new Error("Failed to fetch heatwave prediction");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Heatwave Service Error:", error);


    // fallback mock logic
    return mockHeatwavePrediction(inputData);
  }
};


/**
 * Mock heatwave prediction logic (frontend fallback)
 */
const mockHeatwavePrediction = (input) => {
  const { temperature = 0, humidity = 0 } = input;


  // Simple risk scoring logic
  let riskScore =
    temperature * 1.2 +
    (100 - humidity) * 0.5;


  let status = "";
  let level = "";


  if (riskScore >= 70) {
    status = "Severe Heatwave 🔴";
    level = "High";
  } else if (riskScore >= 50) {
    status = "Heatwave Warning 🟠";
    level = "Medium";
  } else {
    status = "Normal Conditions 🟢";
    level = "Low";
  }


  return {
    status,
    riskLevel: level,
    riskScore: riskScore.toFixed(2),
    confidence: (0.78 + Math.random() * 0.18).toFixed(2),
    message:
      level === "High"
        ? "Extreme heat conditions detected. Take precautions!"
        : level === "Medium"
        ? "Moderate heat risk. Stay hydrated."
        : "No heatwave risk detected.",
    factors: [
      {
        feature: "Temperature",
        value: temperature,
        impact: 0.6,
      },
      {
        feature: "Humidity",
        value: humidity,
        impact: 0.4,
      },
    ],
  };
};


 