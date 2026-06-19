# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# import numpy as np
# import pickle
# import os

# # ==================================================
# # APP INIT
# # ==================================================

# app = FastAPI(
#     title="Climate Guard AI",
#     version="1.0",
#     description="AI-powered Climate Risk Prediction System"
# )

# # ==================================================
# # CORS (Frontend React)
# # ==================================================

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ==================================================
# # PATHS
# # ==================================================

# BASE_PATH = os.path.join("ml", "artifacts")
# GLOBAL_ARTIFACTS = r"C:\Users\hp\Documents\ClimateGuardAI\backend\ml\artifacts"

# # ==================================================
# # LOAD PICKLE SAFELY
# # ==================================================

# def load_pickle(path):
#     if not os.path.exists(path):
#         raise FileNotFoundError(f"Missing model file: {path}")
#     with open(path, "rb") as f:
#         return pickle.load(f)

# # ==================================================
# # LOAD MODELS
# # ==================================================

# climate_kmeans = load_pickle(os.path.join(BASE_PATH, "climate_kmeans.pkl"))
# climate_scaler = load_pickle(os.path.join(BASE_PATH, "climate_scaler.pkl"))

# rainfall_model = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_random_forest.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_scaler.pkl"))
# rainfall_encoder = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_label_encoder.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_model.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))

# climate_risk_model = load_pickle(os.path.join(BASE_PATH, "climate_risk_model.pkl"))

# explainer = load_pickle(os.path.join(BASE_PATH, "explainer.pkl"))

# robust_scaler = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "robust_scaler.pkl"))
# onehot_encoder = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "kmeans_onehot_encoder.pkl"))

# # ==================================================
# # REQUEST SCHEMA (MATCHES YOUR DATASET)
# # ==================================================

# class ClimateInput(BaseModel):
#     temperature_celsius: float = Field(..., ge=-50, le=60)
#     humidity: float = Field(..., ge=0, le=100)
#     precip_mm: float = Field(0, ge=0)
#     wind_kph: float = Field(0, ge=0)
#     pressure_mb: float = Field(1000, ge=800, le=1200)

# # ==================================================
# # ROOT
# # ==================================================

# @app.get("/")
# def root():
#     return {
#         "app": "Climate Guard AI",
#         "status": "running",
#         "version": "1.0"
#     }

# # ==================================================
# # HEALTH CHECK
# # ==================================================

# @app.get("/health")
# def health():
#     return {
#         "status": "ok",
#         "message": "Climate Guard AI API is running"
#     }

# # ==================================================
# # RAINFALL PREDICTION
# # ==================================================

# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     try:
#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.pressure_mb,
#             data.wind_kph
#         ]])

#         X_scaled = rainfall_scaler.transform(X)

#         pred = rainfall_model.predict(X_scaled)[0]

#         label = rainfall_encoder.inverse_transform([pred])[0]

#         response = {
#             "rainfall_risk": str(label)
#         }

#         if hasattr(rainfall_model, "predict_proba"):
#             confidence = np.max(rainfall_model.predict_proba(X_scaled)[0]) * 100
#             response["confidence"] = round(float(confidence), 2)

#         return response

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # HEATWAVE PREDICTION
# # ==================================================

# @app.post("/predict/heatwave")
# def predict_heatwave(data: ClimateInput):

#     try:
#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.pressure_mb,
#             data.wind_kph
#         ]])

#         pred = heatwave_model.predict(X)[0]

#         label = heatwave_encoder.inverse_transform([pred])[0]

#         response = {
#             "heatwave_risk": str(label)
#         }

#         if hasattr(heatwave_model, "predict_proba"):
#             confidence = np.max(heatwave_model.predict_proba(X)[0]) * 100
#             response["confidence"] = round(float(confidence), 2)

#         return response

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # ANOMALY DETECTION
# # ==================================================

# @app.post("/predict/anomaly")
# def predict_anomaly(data: ClimateInput):

#     try:
#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.precip_mm,
#             data.wind_kph,
#             data.pressure_mb
#         ]])

#         X_scaled = anomaly_scaler.transform(X)

#         pred = anomaly_model.predict(X_scaled)[0]

#         return {
#             "anomaly": "Anomaly" if pred == -1 else "Normal"
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # CLIMATE CLUSTER (PROFILE)
# # ==================================================

# @app.post("/predict/cluster")
# def predict_cluster(data: ClimateInput):

#     try:
#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.precip_mm,
#             data.wind_kph,
#             data.pressure_mb
#         ]])

#         X_scaled = climate_scaler.transform(X)

#         cluster = climate_kmeans.predict(X_scaled)[0]

#         return {
#             "climate_cluster": int(cluster)
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # RUN SERVER
# # ==================================================

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=5000,
#         reload=True
#     )
# # from flask import Flask, jsonify

# # app = Flask(__name__)

# # # ----------------------
# # # Home route
# # # ----------------------
# # @app.route("/", methods=["GET"])
# # def home():
# #     return jsonify({
# #         "message": "Climate Guard AI Backend is running 🚀"
# #     })

# # # ----------------------
# # # Test route
# # # ----------------------
# # @app.route("/test", methods=["GET"])
# # def test():
# #     return jsonify({
# #         "status": "ok",
# #         "backend": "working"
# #     })

# # # ----------------------
# # # Run server
# # # ----------------------
# # if __name__ == "__main__":
# #     app.run(debug=True)


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# import numpy as np
# import pickle
# import os

# # ==================================================
# # APP INIT
# # ==================================================

# app = FastAPI(
#     title="Climate Guard AI",
#     version="1.0",
#     description="AI-powered Climate Risk Prediction System"
# )

# # ==================================================
# # CORS
# # ==================================================

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ==================================================
# # MODEL PATH (YOUR FIXED LOCATION)
# # ==================================================

# BASE_PATH = r"C:\Users\hp\Documents\ClimateGuardAI\backend\ml\artifacts"

# # ==================================================
# # LOAD PICKLE SAFE FUNCTION
# # ==================================================

# def load_pickle(path):
#     if not os.path.exists(path):
#         raise FileNotFoundError(f"Missing model file: {path}")
#     with open(path, "rb") as f:
#         return pickle.load(f)

# # ==================================================
# # LOAD MODELS
# # ==================================================

# climate_kmeans = load_pickle(os.path.join(BASE_PATH, "climate_kmeans.pkl"))
# climate_scaler = load_pickle(os.path.join(BASE_PATH, "climate_scaler.pkl"))

# rainfall_model = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_random_forest.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_scaler.pkl"))
# rainfall_encoder = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_label_encoder.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_model.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))

# # ==================================================
# # INPUT SCHEMA
# # ==================================================

# class ClimateInput(BaseModel):
#     temperature_celsius: float = Field(..., ge=-50, le=60)
#     humidity: float = Field(..., ge=0, le=100)
#     precip_mm: float = Field(0, ge=0)
#     wind_kph: float = Field(0, ge=0)
#     pressure_mb: float = Field(1000, ge=800, le=1200)

# # ==================================================
# # ROOT
# # ==================================================

# @app.get("/")
# def root():
#     return {"app": "Climate Guard AI", "status": "running"}

# # ==================================================
# # HEALTH
# # ==================================================

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# # ==================================================
# # RAINFALL PREDICTION
# # ==================================================

# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     try:
#         X = np.array([[data.temperature_celsius,
#                        data.humidity,
#                        data.pressure_mb,
#                        data.wind_kph]])

#         X_scaled = rainfall_scaler.transform(X)

#         pred = rainfall_model.predict(X_scaled)[0]
#         label = rainfall_encoder.inverse_transform([pred])[0]

#         return {"rainfall_risk": str(label)}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # HEATWAVE PREDICTION
# # ==================================================

# @app.post("/predict/heatwave")
# def predict_heatwave(data: ClimateInput):

#     try:
#         X = np.array([[data.temperature_celsius,
#                        data.humidity,
#                        data.pressure_mb,
#                        data.wind_kph]])

#         pred = heatwave_model.predict(X)[0]
#         label = heatwave_encoder.inverse_transform([pred])[0]

#         return {"heatwave_risk": str(label)}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # ANOMALY DETECTION
# # ==================================================

# @app.post("/predict/anomaly")
# def predict_anomaly(data: ClimateInput):

#     try:
#         X = np.array([[data.temperature_celsius,
#                        data.humidity,
#                        data.precip_mm,
#                        data.wind_kph,
#                        data.pressure_mb]])

#         X_scaled = anomaly_scaler.transform(X)

#         pred = anomaly_model.predict(X_scaled)[0]

#         return {
#             "anomaly": "Anomaly" if pred == -1 else "Normal"
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # ==================================================
# # RUN SERVER
# # ==================================================

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import numpy as np
import pickle
import os
from pathlib import Path

# ==================================================
# APP INIT
# ==================================================

app = FastAPI(
    title="Climate Guard AI",
    version="1.0",
    description="AI-powered Climate Risk Prediction System"
)

# ==================================================
# CORS
# ==================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================================
# BASE PATH (FIXED - RELATIVE)
# ==================================================

BASE_PATH = Path(__file__).resolve().parent / "ml" / "artifacts"

# ==================================================
# SAFE LOADER (DOES NOT CRASH APP)
# ==================================================

def load_pickle_safe(filename):
    path = BASE_PATH / filename
    if not path.exists():
        print(f"[WARNING] Missing model: {path}")
        return None
    with open(path, "rb") as f:
        return pickle.load(f)

# ==================================================
# LOAD MODELS (SAFE)
# ==================================================

rainfall_model = load_pickle_safe("rainfall_risk_random_forest.pkl")
rainfall_scaler = load_pickle_safe("rainfall_risk_scaler.pkl")
rainfall_encoder = load_pickle_safe("rainfall_risk_label_encoder.pkl")

heatwave_model = load_pickle_safe("heatwave_risk_model.pkl")
heatwave_encoder = load_pickle_safe("heatwave_label_encoder.pkl")

anomaly_model = load_pickle_safe("climate_anomaly_svm.pkl")
anomaly_scaler = load_pickle_safe("climate_anomaly_scaler.pkl")

# ==================================================
# INPUT SCHEMA
# ==================================================

class ClimateInput(BaseModel):
    temperature_celsius: float = Field(..., ge=-50, le=60)
    humidity: float = Field(..., ge=0, le=100)
    precip_mm: float = Field(0, ge=0)
    wind_kph: float = Field(0, ge=0)
    pressure_mb: float = Field(1000, ge=800, le=1200)

# ==================================================
# ROOT
# ==================================================

@app.get("/")
def root():
    return {"app": "Climate Guard AI", "status": "running"}

# ==================================================
# HEALTH
# ==================================================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "models_loaded": {
            "rainfall": rainfall_model is not None,
            "heatwave": heatwave_model is not None,
            "anomaly": anomaly_model is not None
        }
    }

# ==================================================
# RAINFALL
# ==================================================

@app.post("/predict/rainfall")
def predict_rainfall(data: ClimateInput):

    if None in (rainfall_model, rainfall_scaler, rainfall_encoder):
        raise HTTPException(status_code=500, detail="Rainfall model not loaded")

    X = np.array([[data.temperature_celsius,
                   data.humidity,
                   data.pressure_mb,
                   data.wind_kph]])

    X_scaled = rainfall_scaler.transform(X)

    pred = rainfall_model.predict(X_scaled)[0]
    label = rainfall_encoder.inverse_transform([pred])[0]

    return {"rainfall_risk": str(label)}

# ==================================================
# HEATWAVE
# ==================================================

@app.post("/predict/heatwave")
def predict_heatwave(data: ClimateInput):

    if None in (heatwave_model, heatwave_encoder):
        raise HTTPException(status_code=500, detail="Heatwave model not loaded")

    X = np.array([[data.temperature_celsius,
                   data.humidity,
                   data.pressure_mb,
                   data.wind_kph]])

    pred = heatwave_model.predict(X)[0]
    label = heatwave_encoder.inverse_transform([pred])[0]

    return {"heatwave_risk": str(label)}

# ==================================================
# ANOMALY
# ==================================================

@app.post("/predict/anomaly")
def predict_anomaly(data: ClimateInput):

    if None in (anomaly_model, anomaly_scaler):
        raise HTTPException(status_code=500, detail="Anomaly model not loaded")

    X = np.array([[data.temperature_celsius,
                   data.humidity,
                   data.precip_mm,
                   data.wind_kph,
                   data.pressure_mb]])

    X_scaled = anomaly_scaler.transform(X)
    pred = anomaly_model.predict(X_scaled)[0]

    return {
        "anomaly": "Anomaly" if pred == -1 else "Normal"
    }

# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)