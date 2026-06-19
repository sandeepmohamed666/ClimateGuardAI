import { useState, useEffect, useCallback } from "react";
import { getClimateData } from "../services/api"; // adjust path if needed


const useClimateData = (initialParams = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [params, setParams] = useState(initialParams);


  const fetchClimateData = useCallback(async (overrideParams = {}) => {
    setLoading(true);
    setError(null);


    try {
      const queryParams = { ...params, ...overrideParams };


      const response = await getClimateData(queryParams);


      // expecting backend returns { data: [...] } or similar
      setData(response?.data?.data || response?.data || null);
    } catch (err) {
      setError(
        err?.response?.data?.message ||
          err.message ||
          "Failed to fetch climate data"
      );
      setData(null);
    } finally {
      setLoading(false);
    }
  }, [params]);


  // Auto-fetch on mount or when params change (optional behavior)
  useEffect(() => {
    fetchClimateData();
  }, [fetchClimateData]);


  const updateParams = (newParams) => {
    setParams((prev) => ({
      ...prev,
      ...newParams,
    }));
  };


  const refresh = () => {
    fetchClimateData();
  };


  const reset = () => {
    setData(null);
    setError(null);
  };


  return {
    data,
    loading,
    error,
    params,
    setParams: updateParams,
    fetchClimateData,
    refresh,
    reset,
  };
};


export default useClimateData;
 