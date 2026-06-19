import React from "react";
import "./ClimateProfiles.css";


const ClimateProfiles = () => {
  const profiles = [
    {
      title: "🌴 Tropical Profile",
      description:
        "High temperature, high humidity, and frequent rainfall. Typical of coastal and equatorial regions.",
      features: ["High Temp", "High Humidity", "Heavy Rainfall"],
      color: "#22c55e",
    },
    {
      title: "🏜️ Dry / Arid Profile",
      description:
        "Hot or warm temperatures with very low humidity and minimal rainfall.",
      features: ["High Temp", "Low Humidity", "Low Rainfall"],
      color: "#f59e0b",
    },
    {
      title: "❄️ Cold Climate Profile",
      description:
        "Low temperatures with dry air and limited rainfall or snowfall.",
      features: ["Low Temp", "Low Humidity", "Snow/Cold Conditions"],
      color: "#60a5fa",
    },
    {
      title: "🌦️ Temperate Profile",
      description:
        "Moderate temperature and balanced humidity with seasonal variations.",
      features: ["Balanced Temp", "Moderate Humidity", "Seasonal Rain"],
      color: "#34d399",
    },
  ];


  return (
    <div className="cp-container">
      <div className="cp-card">
        <h1>Climate Profiles 🌍</h1>


        <p>
          Using <b>K-Means clustering</b>, Climate Guard AI groups environmental
          data into distinct climate profiles based on temperature, humidity,
          rainfall, pressure, and air quality.
        </p>


        <div className="grid">
          {profiles.map((profile, index) => (
            <div
              key={index}
              className="profile-card"
              style={{ borderLeft: `4px solid ${profile.color}` }}
            >
              <h2>{profile.title}</h2>
              <p>{profile.description}</p>


              <ul>
                {profile.features.map((f, i) => (
                  <li key={i}>{f}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>


        <h2>🧠 Why Clustering?</h2>
        <p>
          Since climate data is unlabeled, unsupervised learning helps discover
          hidden patterns without predefined categories.
        </p>


        <div className="note">
          K-Means helps convert raw environmental data into meaningful climate
          insights.
        </div>
      </div>
    </div>
  );
};


export default ClimateProfiles;

 
