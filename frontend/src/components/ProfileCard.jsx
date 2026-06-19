import React from "react";

const ProfileCard = ({
  title = "Climate Profile",
  label = "",
  description = "",
  features = [],
  confidence = null,
}) => {
  return (
    <div className="profile-card">
      <div className="profile-header">
        <h3>{title}</h3>
        {label && <span className="profile-label">{label}</span>}
      </div>

      <div className="profile-body">
        {description && (
          <p className="profile-desc">{description}</p>
        )}

        {features.length > 0 && (
          <ul className="profile-features">
            {features.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        )}

        {confidence !== null && (
          <p className="profile-confidence">
            Confidence: <strong>{confidence}%</strong>
          </p>
        )}
      </div>
    </div>
  );
};

export default ProfileCard; 
