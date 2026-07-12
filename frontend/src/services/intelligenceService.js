import { API_BASE_URL } from "../utils/constants";
// services/intelligenceService.js


/**
 * Climate Intelligence Service
 * Provides AI-driven climate insights, trends, and risk summaries
 */


/**
 * Fetch climate intelligence insights from backend
 * @param {Object} queryParams - optional filters (date range, region, etc.)
 */
export const getClimateInsights = async (queryParams = {}) => {
  try {
    const response = await fetch(`${API_BASE_URL}/climate-intelligence`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(queryParams),
    });


    if (!response.ok) {
      throw new Error("Failed to fetch climate insights");
    }


    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Intelligence Service Error:", error);


    // fallback mock data if backend is not connected
    return mockInsights();
  }
};


/**
 * Mock climate intelligence data (frontend fallback)
 */
const mockInsights = () => {
  return {
    summary:
      "Climate patterns show moderate instability with occasional extreme events.",
    
    riskLevel: "Medium",


    stats: {
      normalPatterns: 72,
      anomalies: 18,
      highRiskEvents: 10,
    },


    trends: [
      {
        label: "Temperature Trend",
        value: "Increasing",
        impact: "High",
      },
      {
        label: "Rainfall Pattern",
        value: "Irregular",
        impact: "Medium",
      },
      {
        label: "Air Quality",
        value: "Moderate",
        impact: "Medium",
      },
      {
        label: "Humidity Stability",
        value: "Stable",
        impact: "Low",
      },
    ],


    alerts: [
      "Possible heatwave conditions in upcoming cycle",
      "AQI fluctuations detected in urban regions",
      "Rainfall variability increasing",
    ],
  };
};


/**
 * Optional: Fetch only risk score (lightweight API)
 */
export const getRiskScore = async (payload = {}) => {
  try {
    const response = await fetch(`${API_BASE_URL}/risk-score`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error("Failed to fetch risk score");


    return await response.json();
  } catch (error) {
    console.error("Risk Score Error:", error);


    return {
      riskScore: Math.floor(Math.random() * 100),
      level: "Medium",
    };
  }
};


 