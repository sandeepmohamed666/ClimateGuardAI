import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";


// Pages
import Dashboard from "../pages/Dashboard";
import ClimateProfile from "../pages/ClimateProfile";
import RiskPrediction from "../pages/RiskPrediction";
import AnomalyDetection from "../pages/AnomalyDetection";
import Reports from "../pages/Reports";
import About from "../pages/About";
import NotFound from "../pages/NotFound";


const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Main Pages */}
        <Route path="/" element={<Dashboard />} />
        <Route path="/climate-profile" element={<ClimateProfile />} />
        <Route path="/risk-prediction" element={<RiskPrediction />} />
        <Route path="/anomaly-detection" element={<AnomalyDetection />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/about" element={<About />} />


        {/* 404 Page */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};


export default Router;


