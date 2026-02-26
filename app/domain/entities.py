from dataclasses import dataclass
from enum import Enum
from .exceptions import ValorInvalidoException


class TipoVehiculo(str, Enum):
    ELECTRICO = "Electrico"
    DIESEL = "Diesel"
    HIBRIDO = "Hibrido"


@dataclass(frozen=True)
class ActividadTransporte:
    tipo_vehiculo: TipoVehiculo
    distancia_km: float
    peso_toneladas: float
    factor_eficiencia: float

    def __post_init__(self):
        if self.distancia_km < 0:
            raise ValorInvalidoException("La distancia no puede ser negativa")

        if self.peso_toneladas <= 0:
            raise ValorInvalidoException("El peso debe ser mayor que cero")

        if self.factor_eficiencia is None or self.factor_eficiencia <= 0:
            raise ValorInvalidoException("El factor de eficiencia debe ser mayor que cero")
        

@dataclass(frozen=True)
class FactorEmision:
    tipo_vehiculo: TipoVehiculo
    kg_co2e_por_km: float

    def __post_init__(self):
        if self.kg_co2e_por_km <= 0:
            raise ValorInvalidoException("El factor de emisión debe ser mayor que cero")


@dataclass(frozen=True)
class ResultadoHuella:
    total_co2e_kg: float

    @property
    def total_co2e_ton(self) -> float:
        return round(self.total_co2e_kg / 1000, 6)