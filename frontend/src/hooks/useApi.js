import { useState, useCallback } from "react";
import axios from "axios";


/**
 * useApi - Centralized API handler hook
 * Best for scalable apps like Climate Guard AI
 */
const useApi = (baseURL = "") => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const apiCall = useCallback(
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
          "Something went wrong";


        setError(message);
        setData(null);
        throw err;
      } finally {
        setLoading(false);
      }
    },
    [baseURL]
  );


  // Predefined helpers for cleaner usage
  const get = (url, params, headers) =>
    apiCall({ url, method: "GET", params, headers });


  const post = (url, body, headers) =>
    apiCall({ url, method: "POST", body, headers });


  const put = (url, body, headers) =>
    apiCall({ url, method: "PUT", body, headers });


  const remove = (url, body, headers) =>
    apiCall({ url, method: "DELETE", body, headers });


  const reset = () => {
    setData(null);
    setError(null);
    setLoading(false);
  };


  return {
    data,
    loading,
    error,
    apiCall,
    get,
    post,
    put,
    remove,
    reset,
  };
};


export default useApi;


 