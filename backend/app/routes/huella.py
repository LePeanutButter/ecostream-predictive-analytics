import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas import ActividadRequest
from app.schemas.huella import AnalisisActividadRequest, AnalisisActividadResponse, ResultadoHuellaResponse
from app.services import CalcularHuellaUseCase, NLPService, mapear_analisis_a_actividad
from app.services.repositories import RepositorioFactoresEmisionLocal
from app.services.calculadora import CalculadoraCarbono
from app.models.exceptions import TipoVehiculoNoSoportadoException, ValorInvalidoException

logger = logging.getLogger(__name__)

router = APIRouter()

_repo = RepositorioFactoresEmisionLocal()
_calculadora = CalculadoraCarbono(_repo)
_use_case = CalcularHuellaUseCase(_calculadora)
_nlp_service = NLPService()


@router.post("/resultado-huella", status_code=status.HTTP_201_CREATED)
def calcular_huella(request: ActividadRequest) -> dict:
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


class ChatResultadoResponse(ResultadoHuellaResponse):
    parsed_activity: AnalisisActividadResponse
    result_text: str


@router.post("/chat-resultado-huella", response_model=ChatResultadoResponse)
async def chat_resultado_huella(request: AnalisisActividadRequest) -> ChatResultadoResponse:
    try:
        analisis = await _nlp_service.analizar_mensaje(request)
        actividad_req = mapear_analisis_a_actividad(analisis)
        resultado = _use_case.ejecutar(actividad_req.model_dump())

        mensaje = (
            f"Con base en tu actividad, tu negocio generó aproximadamente "
            f"{resultado.total_co2e_kg:.2f} kg de CO₂."
        )

        return ChatResultadoResponse(
            total_co2e_kg=resultado.total_co2e_kg,
            total_co2e_ton=resultado.total_co2e_ton,
            _links={
                "self": {"href": "/api/chat-resultado-huella"},
                "actividades": {"href": "/api/actividades"},
            },
            parsed_activity=analisis,
            result_text=mensaje,
        )
    except (TipoVehiculoNoSoportadoException, ValorInvalidoException) as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        logger.exception("Error interno en chat_resultado_huella: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor",
        )
