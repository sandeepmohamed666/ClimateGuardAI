from __future__ import annotations

from typing import Literal

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

app = FastAPI(
    title="Climate Guard AI API",
    version="2.0.0",
    description="Integrated backend for Climate Guard AI with Open-Meteo weather data.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ClimateInput(BaseModel):
    temperature_celsius: float = Field(..., ge=-50, le=60)
    humidity: float = Field(..., ge=0, le=100)
    precip_mm: float = Field(0, ge=0)
    wind_kph: float = Field(0, ge=0)
    pressure_mb: float = Field(1013, ge=800, le=1200)


class LocationInput(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class WeatherAndPredictInput(LocationInput):
    mode: Literal["rainfall", "heatwave", "anomaly", "profile"] = "rainfall"


def _rainfall_score(data: ClimateInput) -> float:
    score = (
        data.humidity * 0.55
        + max(0.0, 1015 - data.pressure_mb) * 0.6
        + max(0.0, 25 - data.temperature_celsius) * 0.4
        + max(0.0, data.wind_kph - 10) * 0.3
        + data.precip_mm * 0.8
    )
    return max(0.0, min(100.0, score))


def _heatwave_score(data: ClimateInput) -> float:
    score = (
        max(0.0, data.temperature_celsius - 25) * 3.2
        + max(0.0, 55 - data.humidity) * 0.6
        + max(0.0, 1015 - data.pressure_mb) * 0.3
        + max(0.0, 15 - data.wind_kph) * 0.4
    )
    return max(0.0, min(100.0, score))


def _anomaly_score(data: ClimateInput) -> float:
    score = (
        abs(data.temperature_celsius - 24) * 1.8
        + abs(data.humidity - 55) * 0.8
        + data.precip_mm * 1.2
        + max(0.0, 1000 - data.pressure_mb) * 0.4
        + max(0.0, data.wind_kph - 20) * 0.9
    )
    return max(0.0, min(100.0, score))


def _profile_from_data(data: ClimateInput) -> str:
    if data.temperature_celsius >= 30 and data.humidity >= 65:
        return "Tropical"
    if data.temperature_celsius >= 28 and data.humidity <= 45 and data.precip_mm < 3:
        return "Arid"
    if data.temperature_celsius <= 14:
        return "Cold"
    return "Temperate"


async def _fetch_current_weather(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "pressure_msl",
            "wind_speed_10m",
        ],
        "timezone": "auto",
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(OPEN_METEO_URL, params=params)
            response.raise_for_status()
            payload = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=f"Open-Meteo request failed: {exc}") from exc

    current = payload.get("current") or {}
    if not current:
        raise HTTPException(status_code=502, detail="Open-Meteo returned no current data")

    return {
        "temperature_celsius": float(current.get("temperature_2m", 0.0)),
        "humidity": float(current.get("relative_humidity_2m", 0.0)),
        "precip_mm": float(current.get("precipitation", 0.0)),
        "pressure_mb": float(current.get("pressure_msl", 1013.0)),
        "wind_kph": float(current.get("wind_speed_10m", 0.0)),
        "observed_at": current.get("time"),
        "raw": current,
    }


@app.get("/")
def root() -> dict:
    return {
        "app": "Climate Guard AI",
        "status": "running",
        "version": "2.0.0",
    }


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "message": "Climate Guard AI API is running",
    }


@app.get("/weather/current")
async def weather_current(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
) -> dict:
    weather = await _fetch_current_weather(latitude, longitude)
    return {
        "source": "open-meteo",
        "latitude": latitude,
        "longitude": longitude,
        **weather,
    }


@app.post("/predict/rainfall")
def predict_rainfall(data: ClimateInput) -> dict:
    score = _rainfall_score(data)
    risk = "High" if score >= 70 else "Medium" if score >= 40 else "Low"
    return {
        "rainfall_risk": risk,
        "probability": round(score, 2),
        "confidence": round(65 + (score / 100) * 30, 2),
    }


@app.post("/predict/heatwave")
def predict_heatwave(data: ClimateInput) -> dict:
    score = _heatwave_score(data)
    risk = "High" if score >= 70 else "Medium" if score >= 45 else "Low"
    return {
        "heatwave_risk": risk,
        "risk_score": round(score, 2),
        "confidence": round(60 + (score / 100) * 35, 2),
    }


@app.post("/predict/anomaly")
def predict_anomaly(data: ClimateInput) -> dict:
    score = _anomaly_score(data)
    label = "Anomaly" if score >= 55 else "Normal"
    return {
        "anomaly": label,
        "anomaly_score": round(score, 2),
        "confidence": round(70 + (score / 100) * 25, 2),
    }


@app.post("/predict/cluster")
def predict_cluster(data: ClimateInput) -> dict:
    profile = _profile_from_data(data)
    return {
        "climate_cluster": profile,
        "input": data.model_dump(),
    }


@app.post("/predict/from-location")
async def predict_from_location(payload: WeatherAndPredictInput) -> dict:
    weather = await _fetch_current_weather(payload.latitude, payload.longitude)
    climate_input = ClimateInput(
        temperature_celsius=weather["temperature_celsius"],
        humidity=weather["humidity"],
        precip_mm=weather["precip_mm"],
        wind_kph=weather["wind_kph"],
        pressure_mb=weather["pressure_mb"],
    )

    if payload.mode == "rainfall":
        prediction = predict_rainfall(climate_input)
    elif payload.mode == "heatwave":
        prediction = predict_heatwave(climate_input)
    elif payload.mode == "anomaly":
        prediction = predict_anomaly(climate_input)
    else:
        prediction = predict_cluster(climate_input)

    return {
        "source": "open-meteo",
        "mode": payload.mode,
        "location": {"latitude": payload.latitude, "longitude": payload.longitude},
        "weather": weather,
        "prediction": prediction,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
