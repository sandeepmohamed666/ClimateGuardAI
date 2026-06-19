// services/rainfallService.js


/**
 * Climate Guard AI - Rainfall Prediction Service
 * Handles ML-based rainfall probability estimation
 */


const API_URL = "http://localhost:5000"; // update in production


/**
 * Predict rainfall probability
 * @param {Object} inputData
 * Example:
 * {
 *   humidity: 85,
 *   pressure: 1005,
 *   temperature: 28,
 *   windSpeed: 12
 * }
 */
export const predictRainfall = async (inputData) => {
  try {
    const response = await fetch(`${API_URL}/predict/rainfall`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });


    if (!response.ok) {
      throw new Error("Failed to fetch rainfall prediction");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Rainfall Service Error:", error);


    // fallback mock logic
    return mockRainfallPrediction(inputData);
  }
};


/**
 * Mock rainfall prediction (frontend fallback)
 */
const mockRainfallPrediction = (input) => {
  const {
    humidity = 0,
    pressure = 1010,
    temperature = 30,
    windSpeed = 5,
  } = input;


  // Simple heuristic probability model
  let probability =
    humidity * 0.5 +
    (1010 - pressure) * 0.4 +
    (30 - temperature) * 0.2 +
    windSpeed * 0.3;


  if (probability < 0) probability = 0;


  let level = "";
  let status = "";


  if (probability >= 70) {
    level = "High";
    status = "Heavy Rainfall 🌧️";
  } else if (probability >= 40) {
    level = "Medium";
    status = "Moderate Rainfall 🌦️";
  } else {
    level = "Low";
    status = "Low Rainfall 🌤️";
  }


  return {
    status,
    probability: probability.toFixed(2),
    riskLevel: level,
    confidence: (0.75 + Math.random() * 0.2).toFixed(2),
    message:
      level === "High"
        ? "High chance of rainfall detected. Carry protection!"
        : level === "Medium"
        ? "Moderate rainfall expected."
        : "Low chance of rainfall.",
    factors: [
      {
        feature: "Humidity",
        value: humidity,
        impact: 0.5,
      },
      {
        feature: "Pressure",
        value: pressure,
        impact: 0.4,
      },
      {
        feature: "Temperature",
        value: temperature,
        impact: 0.2,
      },
      {
        feature: "Wind Speed",
        value: windSpeed,
        impact: 0.3,
      },
    ],
  };
};
