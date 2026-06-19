import { useState, useCallback } from "react";
import axios from "axios";


/**
 * Generic fetch hook for GET/POST APIs
 * Works with any endpoint (climate data, risk score, etc.)
 */
const useFetch = (baseURL = "") => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const request = useCallback(
    async ({
      url,
      method = "GET",
      body = null,
      params = null,
      headers = {},
    }) => {
      setLoading(true);
      setError(null);


      try {
        const response = await axios({
          url: baseURL + url,
          method,
          data: body,
          params,
          headers,
        });


        setData(response?.data);
        return response?.data;
      } catch (err) {
        const message =
          err?.response?.data?.message ||
          err.message ||
          "Request failed";


        setError(message);
        setData(null);
        throw err;
      } finally {
        setLoading(false);
      }
    },
    [baseURL]
  );


  const reset = () => {
    setData(null);
    setError(null);
    setLoading(false);
  };


  return {
    data,
    loading,
    error,
    request,
    reset,
  };
};


export default useFetch;

 
