from app.models import ActividadTransporte, ResultadoHuella
from app.models.exceptions import TipoVehiculoNoSoportadoException


class CalculadoraCarbono:
    def __init__(self, repositorio_factores):
        self._repositorio_factores = repositorio_factores

    def _calcular_una(self, actividad: ActividadTransporte) -> ResultadoHuella:
        factor = self._repositorio_factores.obtener_por_tipo(actividad.tipo_vehiculo)
        if factor is None:
            raise TipoVehiculoNoSoportadoException(
                f"Vehículo {actividad.tipo_vehiculo} no soportado"
            )
        emisiones = (
            actividad.distancia_km
            * actividad.peso_toneladas
            * factor.kg_co2e_por_km
            * actividad.factor_eficiencia
        )
        return ResultadoHuella(total_co2e_kg=round(emisiones, 3))

    def calcular(self, actividades):
        if isinstance(actividades, ActividadTransporte):
            return self._calcular_una(actividades)
        return list(map(self._calcular_una, actividades))
