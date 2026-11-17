
from clientes import Cliente
from excepciones import DatosInvalidosError

# Intentamos registrar un cliente valido
try:
    cliente1 = Cliente(
        1,
        "Cristian Diaz",
        "cristian@gmail.com",
        "3001234567"
    )

    print("Cliente registrado correctamente.")
    cliente1.mostrar_informacion()

except DatosInvalidosError as error:
    print("Error al registrar el cliente:", error)


# Intentamos registrar un cliente con correo incorrecto
try:
    cliente2 = Cliente(
        2,
        "Carlos Perez",
        "correo-invalido",
        "3001234567"
    )

except DatosInvalidosError as error:
    print("Error controlado:", error)
