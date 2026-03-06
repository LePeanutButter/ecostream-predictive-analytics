class DomainException(Exception):
    """Excepción base del dominio."""
    pass


class TipoVehiculoNoSoportadoException(DomainException):
    """Se lanza cuando el tipo de vehículo no está soportado."""
    pass


class ValorInvalidoException(DomainException):
    """Se lanza cuando un valor numérico es inválido."""
    pass
