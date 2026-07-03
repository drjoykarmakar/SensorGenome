from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SensorGenome API", version="0.1.0")


class Health(BaseModel):
    status: str
    project: str


@app.get("/health", response_model=Health)
def health() -> Health:
    return Health(status="ok", project="SensorGenome")


@app.get("/")
def root() -> dict:
    return {
        "name": "SensorGenome",
        "mission": "AI-guided molecular sensing benchmarks and active-learning workflows.",
        "starter_benchmark": "FluoroGenome-ProbeResponse",
    }
