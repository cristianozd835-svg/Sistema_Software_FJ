
from clientes import Cliente
from servicios import ReservaSala
from reservas import Reserva
from excepciones import ErrorSistema

print("===== PRUEBA DEL SISTEMA DE RESERVAS =====")

try:
    # Crear un cliente
    cliente = Cliente(
        1,
        "Cristian Diaz",
        "cristian@gmail.com",
        "3001234567"
    )

    # Crear un servicio
    sala = ReservaSala(
        1,
        "Sala de reuniones",
        50000,
        20
    )

    # Crear una reserva
    reserva = Reserva(
        1,
        cliente,
        sala,
        2
    )

    print("\nReserva creada:")
    print(reserva.describir())

    # Confirmar la reserva
    print("\n===== CONFIRMACION =====")
    reserva.confirmar()

    # Procesar la reserva
    print("\n===== PROCESAMIENTO =====")
    reserva.procesar(descuento=10, impuesto=19)

    # Mostrar resultado final
    print("\n===== RESULTADO FINAL =====")
    print(reserva.describir())

except ErrorSistema as error:
    print("Error controlado:", error)

print("\n===== FIN DE LA PRUEBA =====")
