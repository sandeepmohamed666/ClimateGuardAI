// Base URL of the backend API
const BASE_URL = "http://localhost:5000/api";


// API Endpoints
const ENDPOINTS = {
  // Health Check
  HEALTH: `${BASE_URL}/health`,


  // Dashboard
  DASHBOARD: `${BASE_URL}/dashboard`,


  // Climate Profile Prediction
  CLIMATE_PROFILE: `${BASE_URL}/climate-profile/predict`,


  // Climate Risk Prediction
  CLIMATE_RISK: `${BASE_URL}/climate-risk/predict`,


  // Climate Anomaly Detection
  ANOMALY_DETECTION: `${BASE_URL}/anomaly/detect`,


  // SHAP Explainability
  SHAP_EXPLANATION: `${BASE_URL}/explain/shap`,


  // Historical Climate Data
  HISTORICAL_DATA: `${BASE_URL}/data/history`,


  // Real-Time Weather Data
  REALTIME_DATA: `${BASE_URL}/data/realtime`,


  // Upload Dataset
  UPLOAD_DATASET: `${BASE_URL}/upload`,
};


export default ENDPOINTS; 
 