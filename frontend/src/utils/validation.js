// Email Validation
export const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};


// Password Validation
export const validatePassword = (password) => {
  // Minimum 8 characters, at least one letter and one number
  const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/;
  return regex.test(password);
};


// Required Field Validation
export const validateRequired = (value) => {
  return value && value.trim() !== "";
};


// Number Validation
export const validateNumber = (value) => {
  return !isNaN(value) && value !== "";
};


// Climate Parameter Range Validation
export const validateClimateData = (data) => {
  const errors = {};


  // Temperature
  if (
    !validateNumber(data.temperature) ||
    data.temperature < -50 ||
    data.temperature > 60
  ) {
    errors.temperature =
      "Temperature must be between -50°C and 60°C.";
  }


  // Humidity
  if (
    !validateNumber(data.humidity) ||
    data.humidity < 0 ||
    data.humidity > 100
  ) {
    errors.humidity =
      "Humidity must be between 0% and 100%.";
  }


  // Rainfall
  if (
    !validateNumber(data.rainfall) ||
    data.rainfall < 0
  ) {
    errors.rainfall =
      "Rainfall cannot be negative.";
  }


  // Air Quality Index
  if (
    !validateNumber(data.airQualityIndex) ||
    data.airQualityIndex < 0
  ) {
    errors.airQualityIndex =
      "Invalid Air Quality Index.";
  }


  // UV Index
  if (
    !validateNumber(data.uvIndex) ||
    data.uvIndex < 0 ||
    data.uvIndex > 15
  ) {
    errors.uvIndex =
      "UV Index must be between 0 and 15.";
  }


  return errors;
};


  