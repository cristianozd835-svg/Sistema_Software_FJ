
from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador, nombre):

        # Validar el identificador
        if not isinstance(identificador, int) or isinstance(identificador, bool) or identificador <= 0:
            raise DatosInvalidosError(
                "El identificador debe ser un numero entero positivo."
            )

        # Validar el nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre no puede estar vacio."
            )

        self._identificador = identificador
        self._nombre = nombre.strip()

    # Obtener el identificador
    @property
    def identificador(self):
        return self._identificador

    # Obtener el nombre
    @property
    def nombre(self):
        return self._nombre

    # Metodo abstracto
    @abstractmethod
    def describir(self):
        pass
