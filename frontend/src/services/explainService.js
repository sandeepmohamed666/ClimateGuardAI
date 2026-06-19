// services/explainService.js


/**
 * Explain Service - Climate Guard AI
 * Handles communication for model explainability (SHAP / feature importance)
 */


const API_URL = "http://localhost:5000"; // change when deploying backend


/**
 * Get explanation for a prediction
 * @param {Object} inputData - climate feature inputs
 * Example:
 * {
 *   temperature: 35,
 *   humidity: 80,
 *   rainfall: 10,
 *   pressure: 1005,
 *   aqi: 120
 * }
 */
export const getExplanation = async (inputData) => {
  try {
    const response = await fetch(`${API_URL}/explain`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });


    if (!response.ok) {
      throw new Error("Failed to fetch explanation");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Explain Service Error:", error);


    // Fallback mock explanation (for frontend testing)
    return mockExplanation(inputData);
  }
};


/**
 * Mock SHAP-like explanation (used if backend is unavailable)
 */
const mockExplanation = (input) => {
  const features = [
    { feature: "Temperature", value: input.temperature || 0, impact: 0.35 },
    { feature: "Humidity", value: input.humidity || 0, impact: 0.25 },
    { feature: "Rainfall", value: input.rainfall || 0, impact: 0.15 },
    { feature: "Pressure", value: input.pressure || 0, impact: 0.15 },
    { feature: "AQI", value: input.aqi || 0, impact: 0.10 },
  ];


  // Normalize impacts to simulate SHAP contributions
  const explanation = features.map((f) => ({
    feature: f.feature,
    value: f.value,
    contribution: (f.value * f.impact).toFixed(2),
  }));


  return {
    prediction: Math.random() > 0.5 ? "Anomaly" : "Normal",
    explanation,
    message: "Mock explanation (backend not connected)",
  };
};


 