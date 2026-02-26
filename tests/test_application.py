# tests/application/test_application.py

from app.domain.entities import FactorEmision, TipoVehiculo
from app.domain.services import CalculadoraCarbono
from app.application.use_cases import CalcularHuellaUseCase


class FakeRepositorioFactores:
    """Repositorio en memoria para pruebas."""

    def __init__(self, factores=None):
        self._factores = factores or {}

    def obtener_por_tipo(self, tipo_vehiculo):
        return self._factores.get(tipo_vehiculo)


def test_use_case_calculo_diesel_flujo_completo():
    """
    Flujo: UseCase -> Domain -> Repository.
    Fórmula: emisiones = distancia * peso * factor_emision * factor_eficiencia
    """
    factor = FactorEmision(TipoVehiculo.DIESEL, 2.68)
    repo = FakeRepositorioFactores({TipoVehiculo.DIESEL: factor})
    calculadora = CalculadoraCarbono(repo)
    use_case = CalcularHuellaUseCase(calculadora)

    request = {
        "tipo_vehiculo": "Diesel",
        "distancia_km": 500,
        "peso_toneladas": 10,
        "factor_eficiencia": 3.0,
    }

    resultado = use_case.ejecutar(request)

    assert resultado.total_co2e_kg == 40200
    assert resultado.total_co2e_ton == 40.2