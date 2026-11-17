
from registro import RegistroSistema
from registro import RUTA_ARCHIVO
import os

print("Ubicacion del archivo:", RUTA_ARCHIVO)
print("¿Existe el archivo?:", os.path.exists(RUTA_ARCHIVO))
print("===== PRUEBA DEL REGISTRO DE EVENTOS =====")

# Registrar eventos normales.
RegistroSistema.registrar_evento(
    "El sistema Software FJ ha iniciado correctamente."
)

RegistroSistema.registrar_evento(
    "Se ha creado un nuevo cliente."
)

# Simular un error.
try:
    resultado = 10 / 0

except ZeroDivisionError as error:
    print("Se ha detectado un error y será registrado.")

    RegistroSistema.registrar_error(
        "Error al realizar una division.",
        error
    )

print("\nLos registros se han guardado correctamente.")
print("===== FIN DE LA PRUEBA =====")
