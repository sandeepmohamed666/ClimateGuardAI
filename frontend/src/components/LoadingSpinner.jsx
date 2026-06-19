import React from "react";

const LoadingSpinner = ({
  size = "40px",
  message = "Loading...",
  fullPage = false,
}) => {
  return (
    <div className={`spinner-wrapper ${fullPage ? "full-page" : ""}`}>
      <div
        className="spinner"
        style={{ width: size, height: size }}
      ></div>

      {message && <p className="spinner-text">{message}</p>}
    </div>
  );
};

export default LoadingSpinner;
 