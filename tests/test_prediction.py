# tests/test_prediction.py

import pytest

from app.domain.entities import FactorEmision, ResultadoHuella, TipoVehiculo
from app.domain.services import CalculadoraCarbono
from app.domain.exceptions import ValorInvalidoException, TipoVehiculoNoSoportadoException
from app.application.use_cases import PredecirHuellaMensualUseCase


class FakeRepositorioFactores:
    """
    Repositorio en memoria para pruebas unitarias.
    Simula infraestructura sin depender de base de datos.
    """

    def __init__(self, factores=None):
        self._factores = factores or {}

    def obtener_por_tipo(self, tipo_vehiculo):
        return self._factores.get(tipo_vehiculo)


def _crear_use_case_prediccion():
    """Fixture helper: CalculadoraCarbono + PredecirHuellaMensualUseCase con FakeRepo."""
    factores = {
        TipoVehiculo.DIESEL: FactorEmision(TipoVehiculo.DIESEL, 2.68),
        TipoVehiculo.ELECTRICO: FactorEmision(TipoVehiculo.ELECTRICO, 0.12),
        TipoVehiculo.HIBRIDO: FactorEmision(TipoVehiculo.HIBRIDO, 1.45),
    }
    repo = FakeRepositorioFactores(factores)
    calculadora = CalculadoraCarbono(repo)
    return PredecirHuellaMensualUseCase(calculadora)


def test_prediccion_mensual_lista_valida_devuelve_acumulado():
    """
    Dado una lista de actividades válidas,
    cuando se ejecuta el Use Case de predicción,
    entonces devuelve ResultadoHuella con el acumulado en kg y toneladas.
    """
    use_case = _crear_use_case_prediccion()

    request_data = {
        "actividades": [
            {
                "tipo_vehiculo": "Diesel",
                "distancia_km": 100,
                "peso_toneladas": 5,
                "factor_eficiencia": 3.0,
            },
            {
                "tipo_vehiculo": "Electrico",
                "distancia_km": 50,
                "peso_toneladas": 2,
                "factor_eficiencia": 1.2,
            },
        ]
    }

    resultado = use_case.ejecutar(request_data)

    assert isinstance(resultado, ResultadoHuella)
    assert resultado.total_co2e_kg == pytest.approx(4034.4, rel=1e-2)
    assert resultado.total_co2e_ton == pytest.approx(4.0344, rel=1e-5)


def test_prediccion_distancia_km_negativa_lanza_valor_invalido_exception():
    """
    Dado una actividad con distancia_km negativa,
    cuando se ejecuta el Use Case de predicción,
    entonces se lanza ValorInvalidoException (definida en el dominio).
    """
    use_case = _crear_use_case_prediccion()

    request_data = {
        "actividades": [
            {
                "tipo_vehiculo": "Diesel",
                "distancia_km": -100,
                "peso_toneladas": 5,
                "factor_eficiencia": 3.0,
            }
        ]
    }

    with pytest.raises(ValorInvalidoException) as exc_info:
        use_case.ejecutar(request_data)

    assert "distancia" in str(exc_info.value).lower()


def test_prediccion_lista_vacia_devuelve_cero():
    """Lista vacía de actividades debe devolver ResultadoHuella con total 0."""
    use_case = _crear_use_case_prediccion()

    request_data = {"actividades": []}

    resultado = use_case.ejecutar(request_data)

    assert resultado.total_co2e_kg == 0
    assert resultado.total_co2e_ton == 0


def test_prediccion_no_lista_lanza_valor_invalido_exception():
    """Si 'actividades' no es una lista, se lanza ValorInvalidoException."""
    use_case = _crear_use_case_prediccion()

    request_data = {"actividades": "no es una lista"}

    with pytest.raises(ValorInvalidoException) as exc_info:
        use_case.ejecutar(request_data)

    assert "lista" in str(exc_info.value).lower()


def test_prediccion_tipo_vehiculo_no_soportado_lanza_exception():
    """Si una actividad usa tipo de vehículo no soportado, se propaga TipoVehiculoNoSoportadoException."""
    factores = {TipoVehiculo.DIESEL: FactorEmision(TipoVehiculo.DIESEL, 2.68)}
    repo = FakeRepositorioFactores(factores)
    calculadora = CalculadoraCarbono(repo)
    use_case = PredecirHuellaMensualUseCase(calculadora)

    request_data = {
        "actividades": [
            {
                "tipo_vehiculo": "Electrico",
                "distancia_km": 100,
                "peso_toneladas": 5,
                "factor_eficiencia": 1.0,
            }
        ]
    }

    with pytest.raises(TipoVehiculoNoSoportadoException):
        use_case.ejecutar(request_data)