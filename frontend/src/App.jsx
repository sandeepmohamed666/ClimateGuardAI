import React from "react";
import { Routes, Route } from "react-router-dom";


import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";


import Dashboard from "./pages/Dashboard";
import ClimateProfiles from "./pages/ClimateProfiles";
import RainfallPrediction from "./pages/RainfallPrediction";
import HeatwavePrediction from "./pages/HeatwavePrediction";
import AnomalyDetection from "./pages/AnomalyDetection";
import ClimateRiskScore from "./pages/ClimateRiskScore";
import ExplainableAI from "./pages/ExplainableAI";
import NotFound from "./pages/NotFound";


import "./assets/styles/App.css";


function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <Navbar />
        <div className="page-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/rainfall" element={<RainfallPrediction />} />
            <Route path="/heatwave" element={<HeatwavePrediction />} />
            <Route path="/anomaly" element={<AnomalyDetection />} />
            <Route path="/climate-profiles" element={<ClimateProfiles />} />
            <Route path="/risk-score" element={<ClimateRiskScore />} />
            <Route path="/explainable-ai" element={<ExplainableAI />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </div>
  );
}


export default App; 
