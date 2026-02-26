from .entities import ActividadTransporte, ResultadoHuella
from .exceptions import TipoVehiculoNoSoportadoException


class CalculadoraCarbono:
    """
    Servicio de dominio encargado del cálculo.
    Aplica fórmula: 
    emisiones = distancia * peso * factor_emision * factor_eficiencia
    """

    def __init__(self, repositorio_factores):
        self._repositorio_factores = repositorio_factores

    def _calcular_una(self, actividad: ActividadTransporte) -> ResultadoHuella:
        """Calcula la huella para una única actividad."""
        factor = self._repositorio_factores.obtener_por_tipo(actividad.tipo_vehiculo)

        if factor is None:
            raise TipoVehiculoNoSoportadoException(
                f"Vehículo {actividad.tipo_vehiculo} no soportado"
            )

        emisiones = (
            actividad.distancia_km *
            actividad.peso_toneladas *
            factor.kg_co2e_por_km *
            actividad.factor_eficiencia
        )

        return ResultadoHuella(total_co2e_kg=round(emisiones, 3))

    def calcular(self, actividades):
        """
        Calcula la huella de carbono.
        Acepta una actividad o lista de actividades.
        Para una: devuelve ResultadoHuella. Para lista: devuelve list[ResultadoHuella].
        """
        if isinstance(actividades, ActividadTransporte):
            return self._calcular_una(actividades)
        return list(map(self._calcular_una, actividades))