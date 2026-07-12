import { API_BASE_URL } from "../utils/constants";

const API_URLS = Array.from(
  new Set([
    API_BASE_URL,
    "/api",
    "http://localhost:5000",
    "http://127.0.0.1:5000",
  ])
).filter(Boolean);

const readJson = async (response) => {
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const detail = payload?.detail || "Request failed";
    throw new Error(detail);
  }
  return payload;
};

const buildUrl = (baseUrl, endpoint) => `${baseUrl.replace(/\/$/, "")}${endpoint}`;

const requestWithFallback = async (method, endpoint, body) => {
  let lastError = null;

  for (const baseUrl of API_URLS) {
    try {
      const response = await fetch(buildUrl(baseUrl, endpoint), {
        method,
        headers: body ? { "Content-Type": "application/json" } : {},
        body: body ? JSON.stringify(body) : undefined,
      });
      return await readJson(response);
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError || new Error("Request failed");
};

const postRequest = async (endpoint, body) => {
  return requestWithFallback("POST", endpoint, body);
};

const getRequest = async (endpoint) => {
  return requestWithFallback("GET", endpoint);
};

export const healthCheckAPI = () => getRequest("/health");

export const getCurrentWeatherAPI = (latitude, longitude) =>
  getRequest(`/weather/current?latitude=${latitude}&longitude=${longitude}`);

export const predictRainfallAPI = (data) => postRequest("/predict/rainfall", data);
export const predictHeatwaveAPI = (data) => postRequest("/predict/heatwave", data);
export const predictAnomalyAPI = (data) => postRequest("/predict/anomaly", data);
export const predictProfileAPI = (data) => postRequest("/predict/cluster", data);

export const predictFromLocationAPI = (latitude, longitude, mode) =>
  postRequest("/predict/from-location", { latitude, longitude, mode });

export default {
  healthCheckAPI,
  getCurrentWeatherAPI,
  predictRainfallAPI,
  predictHeatwaveAPI,
  predictAnomalyAPI,
  predictProfileAPI,
  predictFromLocationAPI,
};
