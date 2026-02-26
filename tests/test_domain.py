# tests/domain/test_domain.py

import pytest

from app.domain.entities import (
    ActividadTransporte,
    FactorEmision,
    ResultadoHuella,
    TipoVehiculo
)
from app.domain.services import CalculadoraCarbono
from app.domain.exceptions import (
    ValorInvalidoException,
    TipoVehiculoNoSoportadoException
)


class FakeRepositorioFactores:
    """
    Repositorio en memoria para pruebas unitarias.
    Simula infraestructura sin depender de base de datos.
    """

    def __init__(self, factores=None):
        self._factores = factores or {}

    def obtener_por_tipo(self, tipo_vehiculo):
        return self._factores.get(tipo_vehiculo)


def test_actividad_transporte_valida():
    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        distancia_km=100,
        peso_toneladas=10,
        factor_eficiencia=1.2
    )

    assert actividad.distancia_km == 100
    assert actividad.peso_toneladas == 10


def test_actividad_distancia_negativa_error():
    with pytest.raises(ValorInvalidoException):
        ActividadTransporte(
            tipo_vehiculo=TipoVehiculo.DIESEL,
            distancia_km=-50,
            peso_toneladas=10,
            factor_eficiencia=1.2
        )


def test_actividad_peso_cero_error():
    with pytest.raises(ValorInvalidoException):
        ActividadTransporte(
            tipo_vehiculo=TipoVehiculo.DIESEL,
            distancia_km=100,
            peso_toneladas=0,
            factor_eficiencia=1.2
        )


def test_actividad_eficiencia_invalida_error():
    with pytest.raises(ValorInvalidoException):
        ActividadTransporte(
            tipo_vehiculo=TipoVehiculo.DIESEL,
            distancia_km=100,
            peso_toneladas=10,
            factor_eficiencia=0
        )


def test_factor_emision_valido():
    factor = FactorEmision(
        tipo_vehiculo=TipoVehiculo.ELECTRICO,
        kg_co2e_por_km=0.45
    )

    assert factor.kg_co2e_por_km == 0.45


def test_factor_emision_negativo_error():
    with pytest.raises(ValorInvalidoException):
        FactorEmision(
            tipo_vehiculo=TipoVehiculo.DIESEL,
            kg_co2e_por_km=-2
        )


def test_resultado_conversion_a_toneladas():
    resultado = ResultadoHuella(total_co2e_kg=1500)

    assert resultado.total_co2e_kg == 1500
    assert resultado.total_co2e_ton == 1.5


def test_calculadora_diesel_calculo_correcto():
    """
    Fórmula:
    emisiones = distancia * peso * factor_emision * eficiencia

    100 km * 10 ton * 2.5 * 1.2 = 3000 kg
    """

    factor = FactorEmision(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        kg_co2e_por_km=2.5
    )

    repo = FakeRepositorioFactores({
        TipoVehiculo.DIESEL: factor
    })

    calculadora = CalculadoraCarbono(repo)

    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        distancia_km=100,
        peso_toneladas=10,
        factor_eficiencia=1.2
    )

    resultado = calculadora.calcular(actividad)

    assert resultado.total_co2e_kg == 3000
    assert resultado.total_co2e_ton == 3.0


def test_calculadora_electrico_calculo_correcto():
    factor = FactorEmision(
        tipo_vehiculo=TipoVehiculo.ELECTRICO,
        kg_co2e_por_km=0.5
    )

    repo = FakeRepositorioFactores({
        TipoVehiculo.ELECTRICO: factor
    })

    calculadora = CalculadoraCarbono(repo)

    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.ELECTRICO,
        distancia_km=200,
        peso_toneladas=5,
        factor_eficiencia=1
    )

    resultado = calculadora.calcular(actividad)

    # 200 * 5 * 0.5 * 1 = 500 kg
    assert resultado.total_co2e_kg == 500
    assert resultado.total_co2e_ton == 0.5


def test_calculadora_hibrido_calculo_correcto():
    factor = FactorEmision(
        tipo_vehiculo=TipoVehiculo.HIBRIDO,
        kg_co2e_por_km=1.8
    )

    repo = FakeRepositorioFactores({
        TipoVehiculo.HIBRIDO: factor
    })

    calculadora = CalculadoraCarbono(repo)

    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.HIBRIDO,
        distancia_km=150,
        peso_toneladas=8,
        factor_eficiencia=1.1
    )

    resultado = calculadora.calcular(actividad)

    esperado = round(150 * 8 * 1.8 * 1.1, 3)

    assert resultado.total_co2e_kg == esperado
    assert resultado.total_co2e_ton == round(esperado / 1000, 6)


def test_calculadora_tipo_no_soportado():
    repo = FakeRepositorioFactores({})

    calculadora = CalculadoraCarbono(repo)

    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        distancia_km=100,
        peso_toneladas=10,
        factor_eficiencia=1
    )

    with pytest.raises(TipoVehiculoNoSoportadoException):
        calculadora.calcular(actividad)


def test_calculadora_distancia_cero_permitida():
    """
    Regla actual del dominio:
    distancia < 0 es inválido,
    pero 0 está permitido.
    """

    factor = FactorEmision(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        kg_co2e_por_km=2
    )

    repo = FakeRepositorioFactores({
        TipoVehiculo.DIESEL: factor
    })

    calculadora = CalculadoraCarbono(repo)

    actividad = ActividadTransporte(
        tipo_vehiculo=TipoVehiculo.DIESEL,
        distancia_km=0,
        peso_toneladas=5,
        factor_eficiencia=1
    )

    resultado = calculadora.calcular(actividad)

    assert resultado.total_co2e_kg == 0
    assert resultado.total_co2e_ton == 0