

# # ========================================================================================================
# # ========================================================================================================
# # 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# # ========================================================================================================
# # ========================================================================================================



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
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_xgboost.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_logistic_regression.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_random_forest.pkl"))
# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_xgboost.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm_best_params.pkl"))

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



# # ========================================================================================================
# # ========================================================================================================
# # 222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
# # ========================================================================================================
# # ========================================================================================================


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
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_xgboost.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_logistic_regression.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_random_forest.pkl"))
# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_xgboost.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm_best_params.pkl"))

# climate_risk_model = load_pickle(os.path.join(BASE_PATH, "climate_risk_model.pkl"))

# explainer = load_pickle(os.path.join(BASE_PATH, "explainer.pkl"))

# robust_scaler = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "robust_scaler.pkl"))
# onehot_encoder = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "kmeans_onehot_encoder.pkl"))


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

# # ========================================================================================================
# # ========================================================================================================
# # 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
# # ========================================================================================================
# # ========================================================================================================


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# import numpy as np
# import pickle
# import os
# from pathlib import Path

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
# # BASE PATH (FIXED - RELATIVE)
# # ==================================================

# BASE_PATH = Path(__file__).resolve().parent / "ml" / "artifacts"

# # ==================================================
# # SAFE LOADER (DOES NOT CRASH APP)
# # ==================================================

# def load_pickle_safe(filename):
#     path = BASE_PATH / filename
#     if not path.exists():
#         print(f"[WARNING] Missing model: {path}")
#         return None
#     with open(path, "rb") as f:
#         return pickle.load(f)

# # ==================================================
# # LOAD MODELS (SAFE)
# # ==================================================

# climate_kmeans = load_pickle(os.path.join(BASE_PATH, "climate_kmeans.pkl"))
# climate_scaler = load_pickle(os.path.join(BASE_PATH, "climate_scaler.pkl"))

# rainfall_model = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_random_forest.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_scaler.pkl"))
# rainfall_encoder = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_label_encoder.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_xgboost.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_logistic_regression.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_random_forest.pkl"))
# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_xgboost.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm_best_params.pkl"))

# climate_risk_model = load_pickle(os.path.join(BASE_PATH, "climate_risk_model.pkl"))

# explainer = load_pickle(os.path.join(BASE_PATH, "explainer.pkl"))

# robust_scaler = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "robust_scaler.pkl"))
# onehot_encoder = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "kmeans_onehot_encoder.pkl"))

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
#     return {
#         "status": "ok",
#         "models_loaded": {
#             "rainfall": rainfall_model is not None,
#             "heatwave": heatwave_model is not None,
#             "anomaly": anomaly_model is not None
#         }
#     }

# # ==================================================
# # RAINFALL
# # ==================================================

# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     if None in (rainfall_model, rainfall_scaler, rainfall_encoder):
#         raise HTTPException(status_code=500, detail="Rainfall model not loaded")

#     X = np.array([[data.temperature_celsius,
#                    data.humidity,
#                    data.pressure_mb,
#                    data.wind_kph]])

#     X_scaled = rainfall_scaler.transform(X)

#     pred = rainfall_model.predict(X_scaled)[0]
#     label = rainfall_encoder.inverse_transform([pred])[0]

#     return {"rainfall_risk": str(label)}

# # ==================================================
# # HEATWAVE
# # ==================================================

# @app.post("/predict/heatwave")
# def predict_heatwave(data: ClimateInput):

#     if None in (heatwave_model, heatwave_encoder):
#         raise HTTPException(status_code=500, detail="Heatwave model not loaded")

#     X = np.array([[data.temperature_celsius,
#                    data.humidity,
#                    data.pressure_mb,
#                    data.wind_kph]])

#     pred = heatwave_model.predict(X)[0]
#     label = heatwave_encoder.inverse_transform([pred])[0]

#     return {"heatwave_risk": str(label)}

# # ==================================================
# # ANOMALY
# # ==================================================

# @app.post("/predict/anomaly")
# def predict_anomaly(data: ClimateInput):

#     if None in (anomaly_model, anomaly_scaler):
#         raise HTTPException(status_code=500, detail="Anomaly model not loaded")

#     X = np.array([[data.temperature_celsius,
#                    data.humidity,
#                    data.precip_mm,
#                    data.wind_kph,
#                    data.pressure_mb]])

#     X_scaled = anomaly_scaler.transform(X)
#     pred = anomaly_model.predict(X_scaled)[0]

#     return {
#         "anomaly": "Anomaly" if pred == -1 else "Normal"
#     }

# # ==================================================
# # RUN
# # ==================================================

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)


# # ========================================================================================================
# # ========================================================================================================
# # 44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
# # ========================================================================================================
# # ========================================================================================================


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field
# import numpy as np
# import pickle
# from pathlib import Path

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
# # MODEL PATH
# # ==================================================

# BASE_PATH = Path(__file__).resolve().parent / "ml" / "artifacts"

# # ==================================================
# # SAFE PICKLE LOADER
# # ==================================================

# def load_pickle_safe(filename):
#     path = BASE_PATH / filename

#     if not path.exists():
#         print(f"[WARNING] Missing model: {path}")
#         return None

#     try:
#         with open(path, "rb") as f:
#             return pickle.load(f)
#     except Exception as e:
#         print(f"[ERROR] Failed loading {filename}: {e}")
#         return None

# # ==================================================
# # LOAD MODELS
# # ==================================================

# climate_kmeans = load_pickle(os.path.join(BASE_PATH, "climate_kmeans.pkl"))
# climate_scaler = load_pickle(os.path.join(BASE_PATH, "climate_scaler.pkl"))

# rainfall_model = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_random_forest.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_scaler.pkl"))
# rainfall_encoder = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_label_encoder.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_xgboost.pkl"))
# rainfall_scaler = load_pickle(os.path.join(BASE_PATH, "rainfall_risk_logistic_regression.pkl"))

# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_random_forest.pkl"))
# heatwave_model = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_xgboost.pkl"))
# heatwave_encoder = load_pickle(os.path.join(BASE_PATH, "heatwave_risk_label_encoder.pkl"))

# anomaly_model = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_scaler.pkl"))
# anomaly_scaler = load_pickle(os.path.join(BASE_PATH, "climate_anomaly_svm_best_params.pkl"))

# climate_risk_model = load_pickle(os.path.join(BASE_PATH, "climate_risk_model.pkl"))

# explainer = load_pickle(os.path.join(BASE_PATH, "explainer.pkl"))

# robust_scaler = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "robust_scaler.pkl"))
# onehot_encoder = load_pickle(os.path.join(GLOBAL_ARTIFACTS, "kmeans_onehot_encoder.pkl"))


# ==================================================
# # INPUT SCHEMA
# # ==================================================

# # class ClimateInput(BaseModel):
# #     temperature_celsius: float = Field(..., ge=-50, le=60)
# #     humidity: float = Field(..., ge=0, le=100)
# #     precip_mm: float = Field(0, ge=0)
# #     wind_kph: float = Field(0, ge=0)
# #     pressure_mb: float = Field(1000, ge=800, le=1200)

# class ClimateInput(BaseModel):
#     temperature_celsius: float = Field(..., ge=-50, le=60)
#     humidity: float = Field(..., ge=0, le=100)
#     pressure_mb: float = Field(..., ge=800, le=1200)

#     # air_quality_PM2.5: float = Field(..., ge=0)
#     # air_quality_PM10: float = Field(..., ge=0)
#     # visibility_km: float = Field(..., ge=0)
#     # uv_index: float = Field(..., ge=0)

#     wind_kph: float = Field(..., ge=0)

#     # precip_mm: float = Field(0, ge=0)
# # ==================================================
# # ROOT
# # ==================================================

# @app.get("/")
# def root():
#     return {
#         "app": "Climate Guard AI",
#         "status": "running"
#     }

# ==================================================
# HEALTH
# ==================================================

# @app.get("/health")
# def health():
#     return {
#         "status": "ok",
#         "models_loaded": {
#             "rainfall": rainfall_model is not None,
#             "heatwave": heatwave_model is not None,
#             "anomaly": anomaly_model is not None,
#             "profile": climate_profile_model is not None,
#             "risk_score": climate_risk_model is not None,
#             "explainer": climate_explainer is not None,
#         }
#     }

# ==================================================
# RAINFALL
# ==================================================

# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     if None in (rainfall_model, rainfall_scaler, rainfall_encoder):
#         raise HTTPException(
#             status_code=500,
#             detail="Rainfall model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.pressure_mb,
#         data.wind_kph
#     ]])

#     X_scaled = rainfall_scaler.transform(X)

#     pred = rainfall_model.predict(X_scaled)[0]
#     label = rainfall_encoder.inverse_transform([pred])[0]

#     return {
#         "rainfall_risk": str(label)
#     }
# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     try:
#         print("Rainfall request received")

#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.pressure_mb,
#             data.wind_kph
#         ]])

#         print("Input shape:", X.shape)

#         X_scaled = rainfall_scaler.transform(X)

#         pred = rainfall_model.predict(X_scaled)[0]

#         label = rainfall_encoder.inverse_transform([pred])[0]

#         return {"rainfall_risk": str(label)}

#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=500, detail=str(e))


# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     if None in (rainfall_model, rainfall_scaler, rainfall_encoder):
#         raise HTTPException(
#             status_code=500,
#             detail="Rainfall model not loaded"
#         )

#         X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.pressure_mb,
#         # data.air_quality_PM2.5,
#         data.air_quality_PM10,
#         data.visibility_km,
#         data.uv_index,
#         data.wind_kph
#     ]])

#     X_scaled = rainfall_scaler.transform(X)

#     pred = rainfall_model.predict(X_scaled)[0]

#     label = rainfall_encoder.inverse_transform([pred])[0]
#     # X_scaled = rainfall_scaler.transform(X)

#     # prediction = rainfall_model.predict(X_scaled)
#     return {
#         "rainfall_risk": str(label)
#     }
#     # except Exception as e:
#     #     print("ERROR:", str(e))
#     #     raise HTTPException(status_code=500, detail=str(e))

# ==================================================
# RAINFALL
# ==================================================

# @app.post("/predict/rainfall")
# def predict_rainfall(data: ClimateInput):

#     if None in (rainfall_model, rainfall_scaler, rainfall_encoder):
#         raise HTTPException(
#             status_code=500,
#             detail="Rainfall model not loaded"
#         )

#     try:
#         X = np.array([[
#             data.temperature_celsius,
#             data.humidity,
#             data.pressure_mb,
#             # data.air_quality_PM10,
#             # data.visibility_km,
#             # data.uv_index,
#             data.wind_kph
#         ]])

#         X_scaled = rainfall_scaler.transform(X)
#         pred = rainfall_model.predict(X_scaled)[0]
#         label = rainfall_encoder.inverse_transform([pred])[0]

#         return {
#             "rainfall_risk": str(label)
#         }
        
#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=500, detail=str(e))
    
# from fastapi import FastAPI, HTTPException
# import numpy as np
# import pickle

# app = FastAPI()

# # Load artifacts
# model = pickle.load(open("backend/ml/artifacts/rainfall_risk_random_forest.pkl", "rb"))
# scaler = pickle.load(open("backend/ml/artifacts/rainfall_risk_scaler.pkl", "rb"))
# encoder = pickle.load(open("backend/ml/artifacts/rainfall_risk_label_encoder.pkl", "rb"))

# # IMPORTANT: use ONLY the 4 features your model was trained on
# FEATURES = ["temperature_celsius", "humidity", "pressure_mb", "wind_kph"]  # 🔴 replace with your real column names


# @app.post("/predict/rainfall")
# def predict_rainfall(data: dict):
#     try:
#         # Extract ONLY 4 features (ignore extra 7 inputs if coming)
#         X = np.array([[
#             data["temperature_celsius"],
#             data["humidity"],
#             data["pressure_mb"],
#             data["wind_kph"]
#         ]])

#         # Scale input
#         X_scaled = scaler.transform(X)

#         # Predict
#         pred = model.predict(X_scaled)

#         # Convert label
#         result = encoder.inverse_transform(pred)

#         return {
#             "prediction": result[0]
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))




# from fastapi import HTTPException

# @app.post("/predict/rainfall")
# def predict(data: dict):
#     try:
#         # SAFE extraction (prevents KeyError)
#         temp = data.get("temperature_celsius")
#         humidity = data.get("humidity")
#         pressure = data.get("pressure_hpa")
#         wind = data.get("wind_speed_kmph")

#         if None in [temp, humidity, pressure, wind]:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Missing required input features"
#             )

#         X = np.array([[temp, humidity, pressure, wind]])

#         X_scaled = scaler.transform(X)
#         pred = model.predict(X_scaled)
#         result = encoder.inverse_transform(pred)

#         return {"prediction": result[0]}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# ==================================================
# HEATWAVE
# ==================================================

# @app.post("/predict/heatwave")
# def predict_heatwave(data: ClimateInput):

#     if None in (heatwave_model, heatwave_encoder):
#         raise HTTPException(
#             status_code=500,
#             detail="Heatwave model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.pressure_mb,
#         data.wind_kph
#     ]])

#     pred = heatwave_model.predict(X)[0]
#     label = heatwave_encoder.inverse_transform([pred])[0]

#     return {
#         "heatwave_risk": str(label)
#     }

# # ==================================================
# # ANOMALY
# # ==================================================

# @app.post("/predict/anomaly")
# def predict_anomaly(data: ClimateInput):

#     if None in (anomaly_model, anomaly_scaler):
#         raise HTTPException(
#             status_code=500,
#             detail="Anomaly model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.precip_mm,
#         data.wind_kph,
#         data.pressure_mb
#     ]])

#     X_scaled = anomaly_scaler.transform(X)

#     pred = anomaly_model.predict(X_scaled)[0]

#     return {
#         "anomaly": "Anomaly" if pred == -1 else "Normal"
#     }

# # ==================================================
# # CLIMATE PROFILE
# # ==================================================

# @app.post("/predict/profile")
# def predict_profile(data: ClimateInput):

#     if climate_profile_model is None:
#         raise HTTPException(
#             status_code=500,
#             detail="Climate profile model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.precip_mm,
#         data.wind_kph,
#         data.pressure_mb
#     ]])

#     cluster = int(climate_profile_model.predict(X)[0])

#     return {
#         "climate_profile": f"Cluster {cluster}"
#     }

# # ==================================================
# # CLIMATE RISK SCORE
# # ==================================================

# @app.post("/predict/risk-score")
# def predict_risk_score(data: ClimateInput):

#     if climate_risk_model is None:
#         raise HTTPException(
#             status_code=500,
#             detail="Climate risk model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.precip_mm,
#         data.wind_kph,
#         data.pressure_mb
#     ]])

#     score = climate_risk_model.predict(X)[0]

#     return {
#         "climate_risk_score": float(score)
#     }

# # ==================================================
# # EXPLAINABLE AI (SAFE PLACEHOLDER)
# # ==================================================

# @app.post("/predict/explain")
# def explain_prediction(data: ClimateInput):

#     return {
#         "message": "Explainer endpoint available",
#         "status": "pending integration with explainer.pkl"
#     }

# # ==================================================
# # RUN
# # ==================================================

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=5000,
#         reload=True
#     )


# # ========================================================================================================
# # ========================================================================================================
# # 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
# # ========================================================================================================
# # ========================================================================================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
from pathlib import Path

app = FastAPI(
    title="Climate Guard AI API",
    description="""
# Climate Guard AI API

An AI-powered climate intelligence and risk prediction system.

## Features
- 📊 Climate Profiling
- 🔍 Climate Anomaly Detection
- 🌧️ Rainfall Prediction
- 🌡️ Heatwave Detection
- ⚠️ Climate Risk Scoring
- 🧠 Explainable AI Insights
- 📈 Climate Intelligence Analytics

## Available Endpoints

- `/predict/profile`
- `/predict/anomaly`
- `/predict/rainfall`
- `/predict/heatwave`
- `/predict/risk`
- `/explain`
- `/health`
- `/`

Built using FastAPI, Scikit-learn, and Explainable AI techniques.
    """,
    version="1.0.0",
    contact={
        "name": "Sandeep M",
        "email": "sandeepmohamed666@gmail.com"
    },
    license_info={
        "name": "MIT License"
    }
)
# ==================================================
# APP INIT
# ==================================================

app = FastAPI(
    title="Climate Guard AI",
    version="1.0",
    description="AI-powered Climate Risk Prediction System"
)
# =====================================
# ROOT ENDPOINT
# =====================================

@app.get("/")
def home():
    return {
        "message": "Climate Guard AI API is running"
    }

# =====================================
# CORS
# =====================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================================
# BASE PATH (CHANGE THIS IF NEEDED)
# ==================================================

# BASE_PATH = Path("D:/ClimateGuardAI/backend/ml/artifacts")

BASE_DIR = Path(__file__).resolve().parent
BASE_PATH = BASE_DIR / "ml" / "artifacts"

print("BASE_DIR:", BASE_DIR)
print("MODEL_PATH:", BASE_PATH)
# ==================================================
# FEATURE SETS
# ==================================================

CLIMATE_PROFILING_FEATURES = [
    'temperature_celsius',
    'humidity',
    'precip_mm',
    'pressure_mb',
    'air_quality_PM2.5',
    'air_quality_PM10',
    'visibility_km',
    'uv_index'
]

CLIMATE_ANOMALY_FEATURES = [
    'temperature_celsius',
    'humidity',
    'precip_mm',
    'pressure_mb'
]

RAINFALL_FEATURES = [
    'temperature_celsius',
    'humidity',
    'pressure_mb',
    'air_quality_PM2.5',
    'air_quality_PM10',
    'visibility_km',
    'uv_index',
    'wind_kph'
]

HEATWAVE_FEATURES = [
    'temperature_celsius',
    'humidity',
    'pressure_mb',
    'wind_kph',
    'precip_mm',
    'visibility_km',
    'air_quality_PM2.5',
    'air_quality_PM10'
]

EXPLAIN_FEATURES = [
    'temperature_celsius',
    'humidity',
    'pressure_mb',
    'cloud',
    'wind_kph',
    'visibility_km',
    'air_quality_PM2.5',
    'air_quality_PM10'
]

# ==================================================
# LOAD PICKLE FILES
# ==================================================

def load_pickle(file_name):
    path = BASE_PATH / file_name
    if not path.exists():
        raise FileNotFoundError(f"{file_name} not found at {path}")
    with open(path, "rb") as f:
        return pickle.load(f)

try:
    # Climate Profiling
             
    kmeans = load_pickle("climate_kmeans.pkl")
    climate_scaler = load_pickle("climate_scaler.pkl")

    # Anomaly Detection
    anomaly_svm = load_pickle("climate_anomaly_svm.pkl")
    anomaly_scaler = load_pickle("climate_anomaly_scaler.pkl")
    anomaly_best_params = load_pickle("climate_anomaly_svm_best_params.pkl")
    # Rainfall Models
    rainfall_rf = load_pickle("rainfall_risk_random_forest.pkl")
    rainfall_xgb = load_pickle("rainfall_risk_xgboost.pkl")
    rainfall_lr = load_pickle("rainfall_risk_logistic_regression.pkl")
    rainfall_scaler = load_pickle("rainfall_risk_scaler.pkl")
    rainfall_encoder = load_pickle("rainfall_risk_label_encoder.pkl")

    # Heatwave Models
    heat_rf = load_pickle("heatwave_risk_random_forest.pkl")
    heat_xgb = load_pickle("heatwave_risk_xgboost.pkl")
    heat_encoder = load_pickle("heatwave_risk_label_encoder.pkl")

    # Risk Score
    risk_model = load_pickle("climate_risk_model.pkl")

    # Explainability
    explainer = load_pickle("explainer.pkl")

    # Other artifacts
    # robust_scaler = load_pickle("robust_scaler.pkl")
    # onehot_encoder = load_pickle("kmeans_onehot_encoder.pkl")

except Exception as e:
    print("Model loading error:", e)

# ==================================================
# REQUEST MODEL
# ==================================================

# class ClimateInput(BaseModel):
#     temperature_celsius: float
#     humidity: float
#     precip_mm: float
#     pressure_mb: float
#     air_quality_PM2_5: float
#     air_quality_PM10: float
#     visibility_km: float
#     uv_index: float = 0
#     wind_kph: float = 0
#     cloud: float = 0

from pydantic import BaseModel, Field

class ClimateInput(BaseModel):
    temperature_celsius: float = Field(30.0, ge=-50, le=60)
    humidity: float = Field(70.0, ge=0, le=100)
    precip_mm: float = Field(5.0, ge=0)

    pressure_mb: float = Field(1013.0, ge=800, le=1200)

    air_quality_PM2_5: float = Field(40.0, ge=0)
    air_quality_PM10: float = Field(60.0, ge=0)

    visibility_km: float = Field(10.0, ge=0, le=50)

    uv_index: float = Field(5.0, ge=0, le=12)

    wind_kph: float = Field(15.0, ge=0)

    cloud: float = Field(50.0, ge=0, le=100)
# ==================================================
# UTILITY FUNCTION
# ==================================================

def to_array(data: ClimateInput, features):
    mapping = data.dict()
    return np.array([mapping.get(f, 0) for f in features]).reshape(1, -1)

# =====================================================
@app.get("/", tags=["System"])
def home():
    return {
        "message": "Climate Guard AI API is running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
# ==================================================
# ENDPOINTS
# ==================================================

@app.post("/climate-profile")
def climate_profile(data: ClimateInput):
    try:
        X = to_array(data, CLIMATE_PROFILING_FEATURES)
        X_scaled = climate_scaler.transform(X)
        cluster = int(kmeans.predict(X_scaled)[0])
        return {"cluster": cluster}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/climate-anomaly")
def climate_anomaly(data: ClimateInput):
    try:
        X = to_array(data, CLIMATE_ANOMALY_FEATURES)
        X_scaled = anomaly_scaler.transform(X)
        pred = int(anomaly_svm.predict(X_scaled)[0])
        return {"anomaly": pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @app.post("/rainfall-risk")
# def rainfall_risk(data: ClimateInput):
#     try:
#         X = to_array(data, RAINFALL_FEATURES)
#         X_scaled = rainfall_scaler.transform(X)

#         rf = rainfall_rf.predict(X_scaled)[0]
#         xgb = rainfall_xgb.predict(X_scaled)[0]
#         lr = rainfall_lr.predict(X_scaled)[0]

#         final = int(round((rf + xgb + lr) / 3))

#         return {
#             "random_forest": int(rf),
#             "xgboost": int(xgb),
#             "logistic_regression": int(lr),
#             "final_prediction": final
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# -----------------------------------------------------------------

@app.post("/rainfall-risk")
def rainfall_risk(data: ClimateInput):
    try:
        X = to_array(data, RAINFALL_FEATURES)
        X_scaled = rainfall_scaler.transform(X)

        rf = rainfall_rf.predict(X_scaled)[0]
        xgb = rainfall_xgb.predict(X_scaled)[0]
        lr = rainfall_lr.predict(X_scaled)[0]

        # 🔥 FORCE SAFE TYPE CONVERSION
        rf = int(rf) if not isinstance(rf, str) else int(rf == "Yes")
        xgb = int(xgb) if not isinstance(xgb, str) else int(xgb == "Yes")
        lr = int(lr) if not isinstance(lr, str) else int(lr == "Yes")

        final = int(round((rf + xgb + lr) / 3))

        return {
            "random_forest": int(rf),
            "xgboost": int(xgb),
            "logistic_regression": int(lr),
            "final_prediction": final
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#-------------------------------------------------------------
@app.post("/heatwave-risk")
def heatwave_risk(data: ClimateInput):
    try:
        X = to_array(data, HEATWAVE_FEATURES)

        rf = heat_rf.predict(X)[0]
        xgb = heat_xgb.predict(X)[0]

        final = int(round((rf + xgb) / 2))

        return {
            "random_forest": int(rf),
            "xgboost": int(xgb),
            "final_prediction": final
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @app.post("/climate-risk-score")
# def climate_risk_score(data: ClimateInput):
#     try:
#         X = to_array(data, RAINFALL_FEATURES)
#         score = float(risk_model.predict(X)[0])
#         return {"risk_score": score}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.post("/explain")
# def explain_ai(data: ClimateInput):
#     try:
#         X = to_array(data, EXPLAIN_FEATURES)
#         explanation = explainer.explain_instance(X[0].tolist())
#         return {"explanation": str(explanation)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    

# @app.post("/predict/risk-score")
# def predict_risk_score(data: ClimateInput):

#     if climate_risk_model is None:
#         raise HTTPException(
#             status_code=500,
#             detail="Climate risk model not loaded"
#         )

#     X = np.array([[
#         data.temperature_celsius,
#         data.humidity,
#         data.precip_mm,
#         data.wind_kph,
#         data.pressure_mb
#     ]])

#     score = climate_risk_model.predict(X)[0]

#     return {
#         "climate_risk_score": float(score)
#     }

@app.post("/predict/risk-score")
def climate_risk_score(data: ClimateInput):
    try:
        X = to_array(data, CLIMATE_ANOMALY_FEATURES)

        if risk_model is None:
            raise ValueError("risk_model not loaded properly")

        score = risk_model.predict(X)

        return {
            "risk_score": float(score[0])
        }

    except Exception as e:
        print("ERROR in risk-score:", str(e))  # 🔥 IMPORTANT LOG
        raise HTTPException(status_code=500, detail=str(e))


# ==================================================
# EXPLAINABLE AI (SAFE PLACEHOLDER)
# ==================================================

# @app.post("/predict/explain")
# def explain_prediction(data: ClimateInput):

#     return {
#         "message": "Explainer endpoint available",
#         "status": "pending integration with explainer.pkl"
#     }


@app.post("/predict/explain")
def explain_prediction(data: ClimateInput):

    explanations = []

    if data.humidity > 80:
        explanations.append(
            "High humidity increases the probability of rainfall."
        )

    if data.pressure_mb < 1000:
        explanations.append(
            "Low atmospheric pressure indicates unstable weather conditions."
        )

    if data.cloud > 70:
        explanations.append(
            "High cloud cover supports rain formation."
        )

    if data.wind_kph > 25:
        explanations.append(
            "Strong winds may contribute to weather disturbances."
        )

    if data.temperature_celsius > 35:
        explanations.append(
            "High temperature increases heatwave risk."
        )

    if data.air_quality_PM2_5 > 50:
        explanations.append(
            "Poor air quality may increase environmental risk levels."
        )

    if len(explanations) == 0:
        explanations.append(
            "All climate indicators are within normal ranges."
        )

    return {
        "status": "success",
        "model": "Climate Guard AI Explainability Engine",
        "explanation_count": len(explanations),
        "explanations": explanations,
        "message": "Climate factors influencing the prediction have been analyzed."
    }



# import shap
# explainer = shap.TreeExplainer( rainfall_rf)

# @app.post("/explain/rainfall_ml")
# def explain_ml(data: dict):
#     input_array = np.array([[ 
#         data["temperature_celsius"],
#         data["humidity"],
#         data["precip_mm"],
#         data["pressure_mb"],
#         data["air_quality_PM2_5"],
#         data["air_quality_PM10"],
#         data["visibility_km"],
#         data["uv_index"],
#         data["wind_kph"],
#         data["cloud"]
#     ]])

#     shap_values = explainer.shap_values(input_array)

#     feature_names = [
#         "temperature", "humidity", "precipitation", "pressure",
#         "PM2.5", "PM10", "visibility", "UV", "wind", "cloud"
#     ]

#     explanation = []

#     for i, val in enumerate(shap_values[0]):
#         if abs(val) > 0.1:
#             explanation.append(f"{feature_names[i]} influenced prediction")

#     return {
#         "prediction":  rainfall_rf.predict(input_array)[0],
#         "explanation": explanation
#     }