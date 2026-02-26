import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from ..domain.exceptions import (
    TipoVehiculoNoSoportadoException,
    ValorInvalidoException
)
from ..application.use_cases import CalcularHuellaUseCase

logger = logging.getLogger(__name__)

router = APIRouter()


# Límites para evitar valores extremos (km, toneladas, factor adimensional)
MAX_DISTANCIA_KM = 1_000_000
MAX_PESO_TON = 10_000
MAX_FACTOR_EFICIENCIA = 100.0


class ActividadRequest(BaseModel):
    tipo_vehiculo: str
    distancia_km: float = Field(ge=0, le=MAX_DISTANCIA_KM)
    peso_toneladas: float = Field(gt=0, le=MAX_PESO_TON)
    factor_eficiencia: float = Field(gt=0, le=MAX_FACTOR_EFICIENCIA)


@router.post("/resultado-huella", status_code=status.HTTP_201_CREATED)
def calcular_huella(request: ActividadRequest, use_case: CalcularHuellaUseCase):
    try:
        resultado = use_case.ejecutar(request.dict())

        return {
            "total_co2e_kg": resultado.total_co2e_kg,
            "total_co2e_ton": resultado.total_co2e_ton,
            "_links": {
                "self": {"href": "/resultado-huella"},
                "actividades": {"href": "/actividades"}
            }
        }

    except TipoVehiculoNoSoportadoException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except ValorInvalidoException as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )

    except Exception as e:
        logger.exception("Error interno en calcular_huella: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )