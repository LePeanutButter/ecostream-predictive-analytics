import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas import ActividadRequest
from app.services import CalcularHuellaUseCase
from app.services.repositories import RepositorioFactoresEmisionLocal
from app.services.calculadora import CalculadoraCarbono
from app.models.exceptions import TipoVehiculoNoSoportadoException, ValorInvalidoException

logger = logging.getLogger(__name__)

router = APIRouter()

_repo = RepositorioFactoresEmisionLocal()
_calculadora = CalculadoraCarbono(_repo)
_use_case = CalcularHuellaUseCase(_calculadora)


@router.post("/resultado-huella", status_code=status.HTTP_201_CREATED)
def calcular_huella(request: ActividadRequest):
    try:
        resultado = _use_case.ejecutar(request.model_dump())
        return {
            "total_co2e_kg": resultado.total_co2e_kg,
            "total_co2e_ton": resultado.total_co2e_ton,
            "_links": {
                "self": {"href": "/api/resultado-huella"},
                "actividades": {"href": "/api/actividades"},
            },
        }
    except TipoVehiculoNoSoportadoException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ValorInvalidoException as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        logger.exception("Error interno en calcular_huella: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor",
        )
