print("EXERCISE 1")

class Jugador:
    def __init__(self, nombre, goles, velocidad, asistencias, precision_pase, involucramientos_defensivos, numero_camiseta):
        self.nombre = nombre
        self.goles = goles
        self.velocidad = velocidad
        self.asistencias = asistencias
        self.precision_pase = precision_pase
        self.involucramientos_defensivos = involucramientos_defensivos
        self.numero_camiseta = numero_camiseta

jugadores = [
    Jugador("Bruno Fernandes", 5, 6, 9, 10, 3, 8),
    Jugador("Rasmus Hojlund", 12, 8, 2, 6, 2, 11),
    Jugador("Harry Maguire", 1, 5, 1, 7, 9, 5),
    Jugador("Alejandro Garnacho", 8, 7, 8, 6, 0, 17),
    Jugador("Mason Mount", 2, 6, 4, 8, 1, 7)
]

def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Revisar Jugador")
    print("2. Comparar dos Jugadores")
    print("3. Identificar al Jugador más Rápido")
    print("4. Identificar al Máximo Goleador")
    print("5. Identificar al Jugador con más Asistencias")
    print("6. Identificar al Jugador con Mayor Precisión de Pase")
    print("7. Identificar al Jugador con más Involucramientos Defensivos")
    print("8. Salir")

def revisar_jugador(numero_camiseta):
    for jugador in jugadores:
        if jugador.numero_camiseta == numero_camiseta:
            print("\nDetalles de", jugador.nombre)
            print("Goles:", jugador.goles)
            print("Velocidad:", jugador.velocidad)
            print("Asistencias:", jugador.asistencias)
            print("Precisión de Pase:", jugador.precision_pase)
            print("Involucramientos Defensivos:", jugador.involucramientos_defensivos)
            return
    print("Número de camiseta no encontrado.")

def comparar_jugadores(num_camiseta1, num_camiseta2):
    jugador1 = None
    jugador2 = None

    for jugador in jugadores:
        if jugador.numero_camiseta == num_camiseta1:
            jugador1 = jugador
        elif jugador.numero_camiseta == num_camiseta2:
            jugador2 = jugador

    if jugador1 and jugador2:
        print("\nComparación entre", jugador1.nombre, "y", jugador2.nombre)
        print("Goles:", jugador1.goles, "vs", jugador2.goles)
        print("Velocidad:", jugador1.velocidad, "vs", jugador2.velocidad)
        print("Asistencias:", jugador1.asistencias, "vs", jugador2.asistencias)
        print("Precisión de Pase:", jugador1.precision_pase, "vs", jugador2.precision_pase)
        print("Involucramientos Defensivos:", jugador1.involucramientos_defensivos, "vs", jugador2.involucramientos_defensivos)
    else:
        print("Número de camiseta no encontrado.")

def identificar_maximo(atributo):
    max_valor = -1
    max_jugador = None

    for jugador in jugadores:
        valor = getattr(jugador, atributo)
        if valor > max_valor:
            max_valor = valor
            max_jugador = jugador

    print("\nJugador con", atributo.capitalize(), "más alto:", max_jugador.nombre, "(", max_valor, "puntos)")

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-8): ")

    if opcion == '1':
        num_camiseta = int(input("\nIngrese el número de camiseta del jugador: "))
        revisar_jugador(num_camiseta)
    elif opcion == '2':
        num_camiseta1 = int(input("\nIngrese el número de camiseta del primer jugador: "))
        num_camiseta2 = int(input("Ingrese el número de camiseta del segundo jugador: "))
        comparar_jugadores(num_camiseta1, num_camiseta2)
    elif opcion == '3':
        identificar_maximo('velocidad')
    elif opcion == '4':
        identificar_maximo('goles')
    elif opcion == '5':
        identificar_maximo('asistencias')
    elif opcion == '6':
        identificar_maximo('precision_pase')
    elif opcion == '7':
        identificar_maximo('involucramientos_defensivos')
    elif opcion == '8':
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, seleccione una opción del 1 al 8.")


"""con esto se termina el numero 1"""