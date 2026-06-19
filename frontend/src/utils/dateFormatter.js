// src/utils/dateFormatter.js


/**
 * Format date as DD/MM/YYYY
 */
export const formatDate = (date) => {
  if (!date) return "N/A";


  const d = new Date(date);


  return d.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });
};


/**
 * Format date and time as DD/MM/YYYY, HH:MM AM/PM
 */
export const formatDateTime = (date) => {
  if (!date) return "N/A";


  const d = new Date(date);


  return d.toLocaleString("en-IN", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    hour12: true,
  });
};


/**
 * Format date as '17 Jun 2026'
 */
export const formatShortDate = (date) => {
  if (!date) return "N/A";


  const d = new Date(date);


  return d.toLocaleDateString("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}; 



