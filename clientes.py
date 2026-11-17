
from entidades import Entidad
from excepciones import DatosInvalidosError
import re
from registro import RegistroSistema

class Cliente(Entidad):

    """
    Clase que representa a los clientes de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):RegistroSistema.registrar_evento(
    f"Cliente registrado: {self.nombre} | ID: {self.identificador}"
)

        # Inicializamos los atributos de la clase padre
        super().__init__(identificador, nombre)

        # Validamos el correo electronico
        if not isinstance(correo, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            correo.strip()
        ):
            raise DatosInvalidosError(
                "El correo electronico no tiene un formato valido."
            )

        # Validamos el telefono
        if not isinstance(telefono, str) or not re.fullmatch(
            r"\+?[0-9]{7,15}", telefono.strip()
        ):
            raise DatosInvalidosError(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        # Encapsulamos los datos personales
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def describir(self):
        return (
            f"Cliente: {self.nombre} | "
            f"ID: {self.identificador} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}"
        )

    def mostrar_informacion(self):
        print(self.describir())
