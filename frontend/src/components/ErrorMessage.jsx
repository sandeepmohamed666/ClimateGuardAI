import React from "react";

const ErrorMessage = ({
  message = "Something went wrong",
  type = "error",
  onRetry = null,
}) => {
  return (
    <div className={`error-box ${type}`}>
      <div className="error-content">
        <span className="error-icon">⚠️</span>
        <span className="error-text">{message}</span>
      </div>

      {onRetry && (
        <button className="error-retry-btn" onClick={onRetry}>
          Retry
        </button>
      )}
    </div>
  );
};

export default ErrorMessage;
 