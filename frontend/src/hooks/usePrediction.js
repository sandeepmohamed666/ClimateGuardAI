// hooks/usePrediction.js


import { useState } from "react";


/**
 * Generic reusable prediction hook
 * Works with any ML service (anomaly, heatwave, rainfall, etc.)
 */


export const usePrediction = (apiFunction) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const predict = async (inputData) => {
    setLoading(true);
    setError(null);


    try {
      const result = await apiFunction(inputData);
      setData(result);
      return result;
    } catch (err) {
      console.error("Prediction Hook Error:", err);
      setError(err.message || "Prediction failed");
    } finally {
      setLoading(false);
    }
  };


  const reset = () => {
    setData(null);
    setError(null);
    setLoading(false);
  };


  return {
    data,
    loading,
    error,
    predict,
    reset,
  };
};


 