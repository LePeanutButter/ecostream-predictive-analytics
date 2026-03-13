from typing import Any

from app.schemas.huella import (
    ActividadRequest,
    AnalisisActividadRequest,
    AnalisisActividadResponse,
)


class NLPService:
    async def analizar_mensaje(self, payload: AnalisisActividadRequest) -> AnalisisActividadResponse:
        # Aquí deberías integrar la llamada real al proveedor de LLM (OpenAI, Azure, etc.)
        # usando el prompt definido en prompts.md (934-963).
        #
        # Para no acoplar esta demo a un proveedor concreto, dejamos un stub
        # que devuelve siempre valores vacíos.
        return AnalisisActividadResponse(
            electricity_kwh=None,
            vehicles=None,
            fuel_liters=None,
            activity=None,
            notes="analizador NLP no configurado",
        )


def mapear_analisis_a_actividad(datos: AnalisisActividadResponse) -> ActividadRequest:
    tipo_vehiculo = "Diesel"
    actividad = (datos.activity or "").lower()

    if "delivery" in actividad and (datos.electricity_kwh or 0) > 0:
        tipo_vehiculo = "Electrico"
    elif "hibrido" in actividad or "híbrido" in actividad:
        tipo_vehiculo = "Hibrido"

    return ActividadRequest(
        tipo_vehiculo=tipo_vehiculo,
        distancia_km=0.0,
        peso_toneladas=1.0,
        factor_eficiencia=1.0,
    )

