"""
Configuración de factores de emisión.
Externalizada para no exponer lógica de negocio sensible en el código.
Se cargan desde variables de entorno con valores por defecto.
"""
import os


def _float_env(key: str, default: float) -> float:
    """Lee variable de entorno numérica con fallback."""
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return float(val)
    except ValueError:
        return default


# Factores de emisión (kg CO₂e/km) por tipo de vehículo
FACTOR_DIESEL = _float_env("FACTOR_EMISION_DIESEL", 2.68)
FACTOR_ELECTRICO = _float_env("FACTOR_EMISION_ELECTRICO", 0.12)
FACTOR_HIBRIDO = _float_env("FACTOR_EMISION_HIBRIDO", 1.45)
