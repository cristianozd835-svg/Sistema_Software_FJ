
from excepciones import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)
from registro import RegistroSistema

class Reserva:
    """
    Clase que permite administrar las reservas
    realizadas por los clientes de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion, cantidad=1):
        if not isinstance(identificador, int) or isinstance(identificador, bool) or identificador <= 0:
            raise DatosInvalidosError(
                "El identificador de la reserva debe ser positivo."
            )

        from clientes import Cliente
        from servicios import Servicio

        if not isinstance(cliente, Cliente):
            raise ClienteNoEncontradoError(
                "La reserva debe estar asociada a un cliente valido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio valido."
            )

        servicio.validar_parametros(duracion, cantidad)

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__cantidad = cantidad
        self.__estado = "Pendiente"
        self.__costo = 0
RegistroSistema.registrar_evento(
    f"Reserva creada: ID {self.__identificador} | "
    f"Cliente: {self.__cliente.nombre} | "
    f"Servicio: {self.__servicio.nombre}"
)
    @property
    def identificador(self):
        return self.__identificador

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )
RegistroSistema.registrar_evento(
    f"Reserva {self.identificador} confirmada."
)
        self.__estado = "Confirmada"
        print(f"Reserva {self.identificador} confirmada correctamente.")

    def cancelar(self):
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada."
            )

        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"
        print(f"Reserva {self.identificador} cancelada.")
RegistroSistema.registrar_evento(
    f"Reserva {self.identificador} cancelada."
)
    def procesar(self, descuento=0, impuesto=0):
        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                self.__cantidad,
                descuento,
                impuesto
            )
        except DatosInvalidosError as error: except DatosInvalidosError as error:
    RegistroSistema.registrar_error(
        f"Error al procesar la reserva {self.identificador}",
        error
    )

    raise ReservaInvalidaError(
        "No fue posible calcular el costo de la reserva."
    ) from error
            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error
        else:else:
    self.__estado = "Procesada"

    RegistroSistema.registrar_evento(
        f"Reserva {self.identificador} procesada. "
        f"Costo: ${self.__costo:,.2f}"
    )

    print(
        f"Reserva {self.identificador} procesada. "
        f"Costo: ${self.__costo:,.2f}"
    )
            self.__estado = "Procesada"
            print(
                f"Reserva {self.identificador} procesada. "
                f"Costo: ${self.__costo:,.2f}"
            )
        finally:
    RegistroSistema.registrar_evento(
        f"Finalizo el intento de procesamiento de la reserva "
        f"{self.identificador}."
    )
    print("Finalizo el intento de procesamiento.")
            print("Finalizo el intento de procesamiento.")

    def describir(self):
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion} horas\n"
            f"Cantidad: {self.__cantidad}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}"
        )
