// src/constants/constants.js


// =========================
// Application Information
// =========================
export const APP_NAME = "Climate Guard AI";
export const APP_TAGLINE =
  "AI-Powered Climate Monitoring and Environmental Intelligence Platform";


export const APP_VERSION = "1.0.0";


// =========================
// API Configuration
// =========================
export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "/api";


// =========================
// Navigation Links
// =========================
export const NAV_LINKS = [
  { id: 1, name: "Dashboard", path: "/" },
  { id: 2, name: "Climate Profiles", path: "/profiles" },
  { id: 3, name: "Predictions", path: "/predictions" },
  { id: 4, name: "Anomalies", path: "/anomalies" },
  { id: 5, name: "Reports", path: "/reports" },
  { id: 6, name: "About", path: "/about" },
];


// =========================
// Sidebar Menu
// =========================
export const SIDEBAR_MENU = [
  {
    title: "Dashboard",
    path: "/",
    icon: "LayoutDashboard",
  },
  {
    title: "Climate Profiles",
    path: "/profiles",
    icon: "BarChart3",
  },
  {
    title: "Predictions",
    path: "/predictions",
    icon: "LineChart",
  },
  {
    title: "Anomaly Detection",
    path: "/anomalies",
    icon: "AlertTriangle",
  },
  {
    title: "Reports",
    path: "/reports",
    icon: "FileText",
  },
  {
    title: "Settings",
    path: "/settings",
    icon: "Settings",
  },
];


// =========================
// Climate Profile Labels
// =========================
export const CLIMATE_PROFILES = {
  0: "Hot and Dry",
  1: "Humid and Rainy",
  2: "Moderate Climate",
  3: "Extreme Conditions",
};


// =========================
// Prediction Status
// =========================
export const PREDICTION_STATUS = {
  NORMAL: "Normal",
  WARNING: "Warning",
  CRITICAL: "Critical",
};


// =========================
// Theme Colors
// =========================
export const COLORS = {
  primary: "#16a34a",
  secondary: "#0f172a",
  success: "#22c55e",
  warning: "#f59e0b",
  danger: "#ef4444",
  info: "#3b82f6",
  light: "#f8fafc",
  dark: "#111827",
};


// =========================
// Dashboard Cards
// =========================
export const DASHBOARD_CARDS = [
  {
    title: "Total Climate Records",
    key: "totalRecords",
  },
  {
    title: "Detected Anomalies",
    key: "anomalies",
  },
  {
    title: "Climate Profiles",
    key: "profiles",
  },
  {
    title: "Prediction Accuracy",
    key: "accuracy",
  },
];


// =========================
// Footer Text
// =========================
export const FOOTER_TEXT =
  "© 2026 Climate Guard AI. All Rights Reserved.";