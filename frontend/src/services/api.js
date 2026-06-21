// services/api.js

/**
 * Climate Guard AI - Central API Service
 * Unified handler for all backend ML requests
 */

// const API_URL = "http://localhost:5000"; // update in production
const API_URL = "https://climateguardai-2-4k51.onrender.com";
/**
 * Generic POST request handler
 */
const postRequest = async (endpoint, data) => {
  try {
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`Request failed: ${endpoint}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`API Error [${endpoint}]:`, error);
    throw error;
  }
};

/**
 * Generic GET request handler
 */
const getRequest = async (endpoint) => {
  try {
    const response = await fetch(`${API_URL}${endpoint}`);

    if (!response.ok) {
      throw new Error(`Request failed: ${endpoint}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`API Error [${endpoint}]:`, error);
    throw error;
  }
};

/* =========================
   ML MODEL ENDPOINTS
========================= */

// /** Anomaly Detection */
// export const predictAnomalyAPI = (data) =>
//   postRequest("/predict/anomaly", data);

// /** Heatwave Prediction */
// export const predictHeatwaveAPI = (data) =>
//   postRequest("/predict/heatwave", data);

// /** Rainfall Prediction */
// // export const predictRainfallAPI = (data) =>
// //   postRequest("/predict/rainfall", data);

// export const predictRainfallAPI = (data) =>
//   postRequest("/rainfall-risk", data);

// /** Climate Profile (K-Means) */
// export const predictProfileAPI = (data) =>
//   postRequest("/predict/profile", data);

/** Anomaly Detection */
export const predictAnomalyAPI = (data) =>
  postRequest("/anomaly-detection", data);

/** Heatwave Prediction */
export const predictHeatwaveAPI = (data) =>
  postRequest("/heatwave-risk", data);

/** Rainfall Prediction */
export const predictRainfallAPI = (data) =>
  postRequest("/rainfall-risk", data);

/** Climate Profile (K-Means) */
export const predictProfileAPI = (data) =>
  postRequest("/climate-profile", data);
/* =========================
   INTELLIGENCE ENDPOINTS
========================= */

/** Climate Intelligence Insights */
export const getClimateInsightsAPI = (data) =>
  postRequest("/climate-intelligence", data);

/** Risk Score */
export const getRiskScoreAPI = () =>
  getRequest("/risk-score");

/* =========================
   EXPLAINABILITY
========================= */

/** SHAP / Explainability */
export const getExplanationAPI = (data) =>
  postRequest("/explain", data);

/* =========================
   HEALTH CHECK
========================= */

/** Backend status check */
export const healthCheckAPI = () =>
  getRequest("/health");

 