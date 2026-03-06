import os


def _float_env(key: str, default: float) -> float:
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return float(val)
    except ValueError:
        return default


FACTOR_DIESEL = _float_env("FACTOR_EMISION_DIESEL", 2.68)
FACTOR_ELECTRICO = _float_env("FACTOR_EMISION_ELECTRICO", 0.12)
FACTOR_HIBRIDO = _float_env("FACTOR_EMISION_HIBRIDO", 1.45)
