from registro import RegistroSistema, RUTA_ARCHIVO
import os

print("===== PRUEBA DEL REGISTRO DE EVENTOS =====")

print("Ubicacion del archivo:", RUTA_ARCHIVO)

RegistroSistema.registrar_evento(
    "El sistema Software FJ ha iniciado correctamente."
)

RegistroSistema.registrar_evento(
    "Se ha creado un nuevo cliente."
)

try:
    resultado = 10 / 0

except ZeroDivisionError as error:
    print("Se ha detectado un error y sera registrado.")

    RegistroSistema.registrar_error(
        "Error al realizar una division.",
        error
    )

print("\n¿Existe sistema.log?:", os.path.exists(RUTA_ARCHIVO))

print("\n===== FIN DE LA PRUEBA =====")