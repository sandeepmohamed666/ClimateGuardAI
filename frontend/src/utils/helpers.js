// Format date and time
export const formatDate = (date) => {
  return new Date(date).toLocaleString("en-IN", {
    dateStyle: "medium",
    timeStyle: "short",
  });
};


// Capitalize first letter
export const capitalize = (text) => {
  if (!text) return "";
  return text.charAt(0).toUpperCase() + text.slice(1);
};


// Format large numbers
export const formatNumber = (num) => {
  return Number(num).toLocaleString("en-IN");
};


// Get climate risk color
export const getRiskColor = (riskLevel) => {
  switch (riskLevel?.toLowerCase()) {
    case "low":
      return "#4CAF50"; // Green
    case "moderate":
      return "#FFC107"; // Yellow
    case "high":
      return "#FF9800"; // Orange
    case "extreme":
      return "#F44336"; // Red
    default:
      return "#9E9E9E"; // Grey
  }
};


// Get anomaly badge color
export const getAnomalyColor = (isAnomaly) => {
  return isAnomaly ? "#F44336" : "#4CAF50";
};


// Convert risk score to label
export const getRiskLabel = (score) => {
  if (score >= 80) return "Extreme";
  if (score >= 60) return "High";
  if (score >= 40) return "Moderate";
  return "Low";
};


// Generate greeting based on time
export const getGreeting = () => {
  const hour = new Date().getHours();


  if (hour < 12) return "Good Morning";
  if (hour < 18) return "Good Afternoon";
  return "Good Evening";
};


// Calculate percentage safely
export const calculatePercentage = (value, total) => {
  if (!total) return 0;
  return ((value / total) * 100).toFixed(2);
};


