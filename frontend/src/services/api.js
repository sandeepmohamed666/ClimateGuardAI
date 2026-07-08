const API_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5000";

const readJson = async (response) => {
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const detail = payload?.detail || "Request failed";
    throw new Error(detail);
  }
  return payload;
};

const postRequest = async (endpoint, body) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  return readJson(response);
};

const getRequest = async (endpoint) => {
  const response = await fetch(`${API_URL}${endpoint}`);
  return readJson(response);
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
