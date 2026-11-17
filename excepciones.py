
# Excepciones personalizadas del sistema Software FJ


class ErrorSistema(Exception):
    """Excepcion general del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se produce cuando los datos ingresados no son validos."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se produce cuando no se encuentra un cliente."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se produce cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se produce cuando una reserva tiene datos incorrectos."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se produce cuando se intenta realizar una operacion no permitida."""
    pass
