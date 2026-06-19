import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";


import Dashboard from "./pages/Dashboard";
import ClimateProfiles from "./pages/ClimateProfiles";
import RiskPrediction from "./pages/RiskPrediction";
import AnomalyDetection from "./pages/AnomalyDetection";
import Reports from "./pages/Reports";
import NotFound from "./pages/NotFound";


import "./App.css";


function App() {
  return (
    <Router>
      <div className="app">
        <Sidebar />


        <div className="main-content">
          <Navbar />


          <div className="page-content">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route
                path="/climate-profiles"
                element={<ClimateProfiles />}
              />
              <Route
                path="/risk-prediction"
                element={<RiskPrediction />}
              />
              <Route
                path="/anomaly-detection"
                element={<AnomalyDetection />}
              />
              <Route path="/reports" element={<Reports />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </div>


          <Footer />
        </div>
      </div>
    </Router>
  );
}


export default App; 
