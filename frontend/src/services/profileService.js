import { API_BASE_URL } from "../utils/constants";
// services/profileService.js


/**
 * Climate Guard AI - Climate Profile Service
 * Handles K-Means clustering based climate profile prediction
 */


/**
 * Get climate profile prediction from backend
 * @param {Object} inputData
 * Example:
 * {
 *   temperature: 30,
 *   humidity: 70,
 *   rainfall: 12,
 *   pressure: 1008,
 *   aqi: 90
 * }
 */
export const getClimateProfile = async (inputData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict/profile`, {
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
      throw new Error("Failed to fetch climate profile");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Profile Service Error:", error);


    // fallback mock clustering result
    return mockProfilePrediction(inputData);
  }
};


/**
 * Mock K-Means-like clustering fallback
 */
const mockProfilePrediction = (input) => {
  const { temperature = 0, humidity = 0, rainfall = 0 } = input;


  let profile = "";


  // Simple rule-based clustering simulation
  if (temperature >= 32 && humidity >= 70) {
    profile = "Tropical Profile 🌴";
  } else if (temperature >= 30 && humidity < 50) {
    profile = "Dry / Arid Profile 🏜️";
  } else if (temperature <= 15) {
    profile = "Cold Climate Profile ❄️";
  } else {
    profile = "Temperate Profile 🌤️";
  }


  return {
    profile,
    clusterId: Math.floor(Math.random() * 4),
    confidence: (0.75 + Math.random() * 0.2).toFixed(2),
    description: "Mock prediction (backend not connected)",
    features: {
      temperature,
      humidity,
      rainfall,
    },
  };
};
 