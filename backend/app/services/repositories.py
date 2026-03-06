from app.config import FACTOR_DIESEL, FACTOR_ELECTRICO, FACTOR_HIBRIDO
from app.models import FactorEmision, TipoVehiculo


class RepositorioFactoresEmisionLocal:
    def __init__(self):
        self._factores = {
            TipoVehiculo.DIESEL: FactorEmision(TipoVehiculo.DIESEL, FACTOR_DIESEL),
            TipoVehiculo.ELECTRICO: FactorEmision(TipoVehiculo.ELECTRICO, FACTOR_ELECTRICO),
            TipoVehiculo.HIBRIDO: FactorEmision(TipoVehiculo.HIBRIDO, FACTOR_HIBRIDO),
        }

    def obtener_por_tipo(self, tipo_vehiculo):
        return self._factores.get(tipo_vehiculo)
