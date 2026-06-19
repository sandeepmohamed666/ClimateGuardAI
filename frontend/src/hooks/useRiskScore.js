import { useState, useCallback } from "react";
import { getRiskScore } from "../services/api"; // adjust if your path differs


const useRiskScore = () => {
  const [riskScore, setRiskScore] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const calculateRisk = useCallback(async (inputData) => {
    setLoading(true);
    setError(null);


    try {
      // Call backend API
      const response = await getRiskScore(inputData);


      const score = response?.data?.risk_score;


      setRiskScore(score);


      // Simple risk categorization (customize as needed)
      if (score >= 80) setRiskLevel("Critical");
      else if (score >= 60) setRiskLevel("High");
      else if (score >= 40) setRiskLevel("Moderate");
      else setRiskLevel("Low");


    } catch (err) {
      setError(err?.response?.data?.message || "Failed to calculate risk score");
      setRiskScore(null);
      setRiskLevel(null);
    } finally {
      setLoading(false);
    }
  }, []);


  const resetRisk = () => {
    setRiskScore(null);
    setRiskLevel(null);
    setError(null);
  };


  return {
    riskScore,
    riskLevel,
    loading,
    error,
    calculateRisk,
    resetRisk,
  };
};


export default useRiskScore;
 