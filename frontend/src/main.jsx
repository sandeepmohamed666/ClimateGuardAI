// src/main.jsx


import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";


// Global Styles
import "./index.css";


// Render Application
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


If you're using React Router, you can use this version:
// src/main.jsx


import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./index.css";


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);


