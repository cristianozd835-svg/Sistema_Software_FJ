
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from excepciones import ErrorSistema


print("===== SISTEMA SOFTWARE FJ =====")

try:
    # Crear una sala
    sala = ReservaSala(1, "Sala de reuniones", 50000, 20)

    # Crear un equipo
    equipo = AlquilerEquipo(2, "Computador portatil", 15000, 10)

    # Crear una asesoria
    asesoria = AsesoriaEspecializada(
        3, "Asesoria informatica", 80000, "Programacion"
    )

    # Guardar los servicios en una lista
    servicios = [sala, equipo, asesoria]

    # Mostrar la informacion de cada servicio
    for servicio in servicios:
        print("\n", servicio.describir())

    # Calcular costos
    print("\n===== CALCULO DE COSTOS =====")

    print("Reserva de sala:",
          sala.calcular_costo(2))

    print("Alquiler de equipos:",
          equipo.calcular_costo(3, 2, 10))

    print("Asesoria especializada:",
          asesoria.calcular_costo(2, 1, 5, 19))

except ErrorSistema as error:
    print("Error controlado:", error)

print("\nPrograma finalizado.")
