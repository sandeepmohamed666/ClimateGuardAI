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


class RiskScoreInput(BaseModel):
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)
    temperature_celsius: float | None = Field(default=None, ge=-50, le=60)
    humidity: float | None = Field(default=None, ge=0, le=100)
    precip_mm: float | None = Field(default=None, ge=0)
    wind_kph: float | None = Field(default=None, ge=0)
    pressure_mb: float | None = Field(default=None, ge=800, le=1200)


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


def _risk_level_from_score(score: float) -> str:
    if score >= 75:
        return "Extreme"
    if score >= 55:
        return "High"
    if score >= 35:
        return "Moderate"
    return "Low"


def _fallback_weather_from_location(latitude: float, longitude: float) -> dict:
    lat_factor = abs(latitude) / 90.0
    lon_factor = abs(longitude) / 180.0

    temperature_celsius = round(30.0 - (lat_factor * 22.0) + (lon_factor * 2.5), 1)
    humidity = round(45.0 + (lat_factor * 30.0) - (lon_factor * 8.0), 1)
    precip_mm = round(max(0.0, 2.5 + lat_factor * 6.0 - lon_factor * 1.5), 1)
    pressure_mb = round(1008.0 - (lat_factor * 8.0) + (lon_factor * 4.0), 1)
    wind_kph = round(7.0 + (lat_factor * 6.0) + (lon_factor * 4.0), 1)

    return {
        "temperature_celsius": max(-20.0, min(45.0, temperature_celsius)),
        "humidity": max(0.0, min(100.0, humidity)),
        "precip_mm": max(0.0, precip_mm),
        "pressure_mb": max(800.0, min(1200.0, pressure_mb)),
        "wind_kph": max(0.0, wind_kph),
        "observed_at": None,
        "raw": {
            "source": "synthetic-fallback",
            "latitude": latitude,
            "longitude": longitude,
        },
        "source": "synthetic-fallback",
    }


async def _climate_input_from_payload(payload: RiskScoreInput) -> tuple[ClimateInput, dict | None]:
    if (
        payload.temperature_celsius is not None
        and payload.humidity is not None
        and payload.precip_mm is not None
        and payload.wind_kph is not None
        and payload.pressure_mb is not None
    ):
        return (
            ClimateInput(
                temperature_celsius=payload.temperature_celsius,
                humidity=payload.humidity,
                precip_mm=payload.precip_mm,
                wind_kph=payload.wind_kph,
                pressure_mb=payload.pressure_mb,
            ),
            None,
        )

    if payload.latitude is not None and payload.longitude is not None:
        weather = await _fetch_current_weather(payload.latitude, payload.longitude)
        return (
            ClimateInput(
                temperature_celsius=weather["temperature_celsius"],
                humidity=weather["humidity"],
                precip_mm=weather["precip_mm"],
                wind_kph=weather["wind_kph"],
                pressure_mb=weather["pressure_mb"],
            ),
            weather,
        )

    default_weather = {
        "temperature_celsius": 24.0,
        "humidity": 55.0,
        "precip_mm": 0.0,
        "wind_kph": 8.0,
        "pressure_mb": 1013.0,
        "observed_at": None,
        "raw": {},
    }
    return (
        ClimateInput(
            temperature_celsius=default_weather["temperature_celsius"],
            humidity=default_weather["humidity"],
            precip_mm=default_weather["precip_mm"],
            wind_kph=default_weather["wind_kph"],
            pressure_mb=default_weather["pressure_mb"],
        ),
        default_weather,
    )


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
    except httpx.HTTPError:
        return _fallback_weather_from_location(latitude, longitude)

    current = payload.get("current") or {}
    if not current:
        return _fallback_weather_from_location(latitude, longitude)

    return {
        "temperature_celsius": float(current.get("temperature_2m", 0.0)),
        "humidity": float(current.get("relative_humidity_2m", 0.0)),
        "precip_mm": float(current.get("precipitation", 0.0)),
        "pressure_mb": float(current.get("pressure_msl", 1013.0)),
        "wind_kph": float(current.get("wind_speed_10m", 0.0)),
        "observed_at": current.get("time"),
        "raw": current,
        "source": "open-meteo",
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


@app.post("/predict/profile")
def predict_profile(data: ClimateInput) -> dict:
    return predict_cluster(data)


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


@app.post("/risk-score")
async def risk_score(payload: RiskScoreInput) -> dict:
    climate_input, weather = await _climate_input_from_payload(payload)

    rainfall = _rainfall_score(climate_input)
    heatwave = _heatwave_score(climate_input)
    anomaly = _anomaly_score(climate_input)
    score = round(rainfall * 0.35 + heatwave * 0.4 + anomaly * 0.25, 2)
    level = _risk_level_from_score(score)

    return {
        "risk_score": score,
        "level": level,
        "components": {
            "rainfall": round(rainfall, 2),
            "heatwave": round(heatwave, 2),
            "anomaly": round(anomaly, 2),
        },
        "location": None
        if payload.latitude is None or payload.longitude is None
        else {"latitude": payload.latitude, "longitude": payload.longitude},
        "weather": weather,
    }


@app.post("/climate-intelligence")
async def climate_intelligence(payload: RiskScoreInput) -> dict:
    climate_input, weather = await _climate_input_from_payload(payload)
    rainfall = _rainfall_score(climate_input)
    heatwave = _heatwave_score(climate_input)
    anomaly = _anomaly_score(climate_input)
    score = round(rainfall * 0.35 + heatwave * 0.4 + anomaly * 0.25, 2)
    level = _risk_level_from_score(score)

    return {
        "summary": (
            f"Current conditions indicate {level.lower()} climate risk with a combined score of {score:.2f}."
        ),
        "riskLevel": level,
        "stats": {
            "normalPatterns": max(0, int(100 - score)),
            "anomalies": int(round(anomaly)),
            "highRiskEvents": int(round((rainfall + heatwave) / 2)),
        },
        "trends": [
            {
                "label": "Rainfall Pressure",
                "value": "Elevated" if rainfall >= 40 else "Stable",
                "impact": "High" if rainfall >= 70 else "Medium" if rainfall >= 40 else "Low",
            },
            {
                "label": "Heat Stress",
                "value": "Elevated" if heatwave >= 40 else "Stable",
                "impact": "High" if heatwave >= 70 else "Medium" if heatwave >= 40 else "Low",
            },
            {
                "label": "Anomaly Signal",
                "value": "Elevated" if anomaly >= 55 else "Stable",
                "impact": "High" if anomaly >= 70 else "Medium" if anomaly >= 55 else "Low",
            },
        ],
        "alerts": [
            "Monitor rapidly changing weather conditions.",
            "Review rainfall and heatwave indicators for short-term risk.",
            "Check anomaly signal if conditions continue to diverge.",
        ],
        "weather": weather,
        "components": {
            "rainfall": round(rainfall, 2),
            "heatwave": round(heatwave, 2),
            "anomaly": round(anomaly, 2),
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=5000, reload=True)
