from typing import Any

from app.models import ActividadTransporte, ResultadoHuella, TipoVehiculo
from app.models.exceptions import ValorInvalidoException
from app.services.calculadora import CalculadoraCarbono

CAMPOS_ACTIVIDAD = ("tipo_vehiculo", "distancia_km", "peso_toneladas", "factor_eficiencia")


def _validar_y_crear_actividad(item: dict[str, Any]) -> ActividadTransporte:
    if not isinstance(item, dict):
        raise ValorInvalidoException("Se espera un diccionario con los campos de actividad")
    for campo in CAMPOS_ACTIVIDAD:
        if campo not in item:
            raise ValorInvalidoException(f"Campo requerido ausente: {campo}")
    try:
        # Normalizar el tipo de vehículo para que coincida con el Enum (ej: "diesel" -> "Diesel")
        tipo_raw = str(item.get("tipo_vehiculo", "")).capitalize()
        tipo_vehiculo = TipoVehiculo(tipo_raw)
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
    def __init__(self, calculadora: CalculadoraCarbono):
        self._calculadora = calculadora

    def ejecutar(self, request_data: dict[str, Any]) -> ResultadoHuella:
        actividad = _validar_y_crear_actividad(request_data)
        return self._calculadora.calcular(actividad)
