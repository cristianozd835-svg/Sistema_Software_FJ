
from pathlib import Path

# Obtener la carpeta donde se encuentra este generador.
CARPETA_PROYECTO = Path(__file__).resolve().parent

# Archivos nuevos que vamos a generar.
archivos = {

    "main.py": r'''
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import ErrorSistema, DatosInvalidosError
from registro import RegistroSistema


def ejecutar_demo():
    print("=" * 55)
    print("       SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    clientes = []
    servicios = []
    reservas = []

    def operacion(numero, descripcion, accion):
        print(f"\n--- OPERACION {numero}: {descripcion} ---")

        try:
            resultado = accion()
            RegistroSistema.registrar_evento(
                f"Operacion {numero} exitosa: {descripcion}"
            )
            print("Resultado: operacion exitosa.")
            return resultado

        except ErrorSistema as error:
            RegistroSistema.registrar_error(
                f"Error en operacion {numero}: {descripcion}", error
            )
            print(f"Error controlado: {error}")

        except Exception as error:
            RegistroSistema.registrar_error(
                f"Error inesperado en operacion {numero}", error
            )
            print(f"Error inesperado controlado: {error}")

        return None

    # OPERACION 1: Registro de un cliente valido.
    def crear_cliente_valido():
        cliente = Cliente(
            1, "Cristian Diaz",
            "cristian@gmail.com", "3001234567"
        )
        clientes.append(cliente)
        print(cliente.describir())
        return cliente

    cliente_principal = operacion(
        1, "Registro de cliente valido", crear_cliente_valido
    )

    # OPERACION 2: Registro de cliente con correo incorrecto.
    operacion(
        2,
        "Registro de cliente con correo invalido",
        lambda: Cliente(2, "Carlos Perez", "correo-malo", "3001234567")
    )

    # OPERACION 3: Registro de cliente con telefono incorrecto.
    operacion(
        3,
        "Registro de cliente con telefono invalido",
        lambda: Cliente(3, "Ana Lopez", "ana@gmail.com", "ABC123")
    )

    # OPERACION 4: Creacion de una sala valida.
    def crear_sala():
        sala = ReservaSala(1, "Sala de reuniones", 50000, 20)
        servicios.append(sala)
        print(sala.describir())
        return sala

    sala_principal = operacion(
        4, "Creacion de servicio de reserva de sala", crear_sala
    )

    # OPERACION 5: Intento de crear un servicio con tarifa invalida.
    operacion(
        5,
        "Creacion de servicio con tarifa negativa",
        lambda: ReservaSala(2, "Sala incorrecta", -5000, 10)
    )

    # OPERACION 6: Creacion de alquiler de equipos.
    def crear_equipo():
        equipo = AlquilerEquipo(
            3, "Computador portatil", 15000, 10
        )
        servicios.append(equipo)
        print(equipo.describir())
        return equipo

    equipo_principal = operacion(
        6, "Creacion de servicio de alquiler de equipos", crear_equipo
    )

    # OPERACION 7: Creacion de asesoria especializada.
    def crear_asesoria():
        asesoria = AsesoriaEspecializada(
            4, "Asesoria informatica", 80000, "Programacion"
        )
        servicios.append(asesoria)
        print(asesoria.describir())
        return asesoria

    asesoria_principal = operacion(
        7, "Creacion de asesoria especializada", crear_asesoria
    )

    # OPERACION 8: Reserva correcta, confirmacion y procesamiento.
    def reserva_exitosa():
        reserva = Reserva(1, cliente_principal, sala_principal, 2)
        reservas.append(reserva)
        reserva.confirmar()
        reserva.procesar(descuento=10, impuesto=19)
        print(reserva.describir())
        return reserva

    if cliente_principal and sala_principal:
        operacion(
            8, "Creacion y procesamiento de reserva exitosa",
            reserva_exitosa
        )
    else:
        print("\nOperacion 8 omitida: faltan datos validos.")

    # OPERACION 9: Intento de reserva con cliente inexistente.
    if sala_principal:
        operacion(
            9,
            "Intento de reserva con cliente inexistente",
            lambda: Reserva(2, None, sala_principal, 2)
        )

    # OPERACION 10: Crear y cancelar una reserva.
    def cancelar_reserva():
        reserva = Reserva(3, cliente_principal, sala_principal, 1)
        reservas.append(reserva)
        reserva.cancelar()
        print(reserva.describir())
        return reserva

    if cliente_principal and sala_principal:
        operacion(
            10, "Creacion y cancelacion de una reserva",
            cancelar_reserva
        )

    print("\n" + "=" * 55)
    print("RESUMEN DEL SISTEMA")
    print("=" * 55)
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")
    print("Consulte logs/sistema.log para revisar los registros.")
    print("=" * 55)

    RegistroSistema.registrar_evento(
        "Finalizo la simulacion integral de Software FJ."
    )


if __name__ == "__main__":
    ejecutar_demo()
''',

    "prueba_integral.py": r'''
from main import ejecutar_demo

print("INICIANDO LAS PRUEBAS INTEGRALES DE SOFTWARE FJ\n")

ejecutar_demo()

print("\nPRUEBAS INTEGRALES FINALIZADAS.")
'''
}


def generar_archivos():
    print("=" * 55)
    print("GENERADOR DEL PROYECTO SOFTWARE FJ")
    print("=" * 55)

    # Crear la carpeta logs si no existe.
    carpeta_logs = CARPETA_PROYECTO / "logs"
    carpeta_logs.mkdir(exist_ok=True)

    print("\nCarpeta logs comprobada.")

    # Crear solamente los archivos que no existan.
    for nombre, contenido in archivos.items():
        ruta = CARPETA_PROYECTO / nombre

        if ruta.exists():
            print(f"[CONSERVADO] {nombre} ya existe. No se modifico.")
        else:
            ruta.write_text(contenido.strip() + "\n", encoding="utf-8")
            print(f"[CREADO] {nombre}")

    print("\nProceso finalizado.")
    print("Los archivos existentes fueron conservados.")
    print("=" * 55)


if __name__ == "__main__":
    generar_archivos()
