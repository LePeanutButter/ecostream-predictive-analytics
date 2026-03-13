from typing import Optional

from pydantic import BaseModel, Field

MAX_DISTANCIA_KM = 1_000_000
MAX_PESO_TON = 10_000
MAX_FACTOR_EFICIENCIA = 100.0


class ActividadRequest(BaseModel):
    tipo_vehiculo: str
    distancia_km: float = Field(ge=0, le=MAX_DISTANCIA_KM)
    peso_toneladas: float = Field(gt=0, le=MAX_PESO_TON)
    factor_eficiencia: float = Field(gt=0, le=MAX_FACTOR_EFICIENCIA)


class ResultadoHuellaResponse(BaseModel):
    total_co2e_kg: float
    total_co2e_ton: float
    _links: dict


class AnalisisActividadRequest(BaseModel):
    message: str


class AnalisisActividadResponse(BaseModel):
    electricity_kwh: Optional[float]
    vehicles: Optional[int]
    fuel_liters: Optional[float]
    activity: Optional[str]
    notes: Optional[str]
