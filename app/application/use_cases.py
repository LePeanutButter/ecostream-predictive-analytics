from typing import Any

from ..domain.entities import ActividadTransporte, ResultadoHuella, TipoVehiculo
from ..domain.exceptions import ValorInvalidoException
from ..domain.services import CalculadoraCarbono

CAMPOS_ACTIVIDAD = ("tipo_vehiculo", "distancia_km", "peso_toneladas", "factor_eficiencia")


def _validar_y_crear_actividad(item: dict[str, Any]) -> ActividadTransporte:
    """Valida el dict y crea ActividadTransporte. Lanza ValorInvalidoException si falta un campo o es inválido."""
    if not isinstance(item, dict):
        raise ValorInvalidoException("Se espera un diccionario con los campos de actividad")

    for campo in CAMPOS_ACTIVIDAD:
        if campo not in item:
            raise ValorInvalidoException(f"Campo requerido ausente: {campo}")

    try:
        tipo_vehiculo = TipoVehiculo(item["tipo_vehiculo"])
        distancia_km = float(item["distancia_km"])
        peso_toneladas = float(item["peso_toneladas"])
        factor_eficiencia = float(item["factor_eficiencia"])
    except (ValueError, TypeError) as e:
        raise ValorInvalidoException(f"Valor inválido en campo: {e}") from e
    except KeyError as e:
        raise ValorInvalidoException(f"Campo requerido ausente: {e}") from e

    return ActividadTransporte(
        tipo_vehiculo=tipo_vehiculo,
        distancia_km=distancia_km,
        peso_toneladas=peso_toneladas,
        factor_eficiencia=factor_eficiencia,
    )


class CalcularHuellaUseCase:
    """
    Caso de uso que orquesta el flujo:
    Controller -> Application -> Domain -> Repository
    """

    def __init__(self, calculadora: CalculadoraCarbono):
        self._calculadora = calculadora

    def ejecutar(self, request_data: dict[str, Any]):
        actividad = _validar_y_crear_actividad(request_data)
        return self._calculadora.calcular(actividad)


class PredecirHuellaMensualUseCase:
    """
    Caso de uso que proyecta la huella de carbono mensual a partir
    de un listado de actividades de transporte planificadas.
    Reutiliza CalculadoraCarbono para cada actividad y devuelve el acumulado.
    """

    def __init__(self, calculadora: CalculadoraCarbono):
        self._calculadora = calculadora

    def ejecutar(self, request_data: dict[str, Any]) -> ResultadoHuella:
        actividades_raw = request_data.get("actividades", [])

        if not isinstance(actividades_raw, list):
            raise ValorInvalidoException("Se espera una lista de actividades")

        acumulado_kg = 0.0

        for item in actividades_raw:
            actividad = _validar_y_crear_actividad(item)
            resultado = self._calculadora.calcular(actividad)
            acumulado_kg += resultado.total_co2e_kg

        return ResultadoHuella(total_co2e_kg=round(acumulado_kg, 3))