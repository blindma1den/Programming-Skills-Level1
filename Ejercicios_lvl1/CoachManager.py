# Por Felipe (ZenTial)
# 1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
# The program functions as follows: The coach accesses the system and encounters a menu with the following options:
# Player Review: By entering the player's jersey number, they can access the player's characteristics.
# Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
# Identify the fastest player: Displays the player with the most points in speed.
# Identify the top goalscorer: Displays the player with the most points in goals.
# Identify the player with the most assists: Displays the player with the most points in assists.
# Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
# Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
# The system should also allow returning to the main menu.
from os import system

# Declaración de variables

camiseta_8 = {'nombre': 'Bruno Fernandes', 'goles': 5, 'puntos velocidad': 6,
              'puntos asistencia': 9, 'puntos precision pase': 10, 'participacion defensiva': 3}
camiseta_11 = {'nombre': 'Rasmus Hojlund', 'goles': 12, 'puntos velocidad': 8,
               'puntos asistencia': 2, 'puntos precision pase': 6, 'participacion defensiva': 2}
camiseta_5 = {'nombre': 'Harry Maguire', 'goles': 1, 'puntos velocidad': 5,
              'puntos asistencia': 1, 'puntos precision pase': 7, 'participacion defensiva': 9}
camiseta_17 = {'nombre': 'Alejandro Garnacho', 'goles': 8, 'puntos velocidad': 7,
               'puntos asistencia': 8, 'puntos precision pase': 16, 'participacion defensiva': 0}
camiseta_7 = {'nombre': 'Mason Mount', 'goles': 2, 'puntos velocidad': 6,
              'puntos asistencia': 4, 'puntos precision pase': 8, 'participacion defensiva': 1}
numeros_camisetas = ['8', '11', '5', '17', '7']
lista_camisetas = [camiseta_8, camiseta_11, camiseta_5, camiseta_17, camiseta_7]


# Función jugador más velocidad
def jugador_masrapido():
    velocidades = []
    for jugador in lista_camisetas:
        velocidades.append(jugador['puntos velocidad'])
    mas_rapido = max(velocidades)
    indice = velocidades.index(mas_rapido)
    print(f'El jugador más rapido es {lista_camisetas[indice]['nombre']}')
    print(f'Su velocidad es: {mas_rapido}')
    input('Presione cualquier tecla para volver al menú')


# Función jugador con más goles
def jugador_masgoles():
    goles = []
    for jugador in lista_camisetas:
        goles.append(jugador['goles'])
    mas_goles = max(goles)
    indice = goles.index(mas_goles)
    print(f'El jugador con más goles es {lista_camisetas[indice]['nombre']}')
    print(f'Su cantidad de goles es: {mas_goles}')
    input('Presione cualquier tecla para volver al menú')


# Función jugador con más asistencias
def jugador_masasistencias():
    asistencias = []
    for jugador in lista_camisetas:
        asistencias.append(jugador['puntos asistencia'])
    mas_asistencias = max(asistencias)
    indice = asistencias.index(mas_asistencias)
    print(f'El jugador con más asistencias es {lista_camisetas[indice]['nombre']}')
    print(f'Su cantidad de asistencias es: {mas_asistencias}')
    input('Presione cualquier tecla para volver al menú')


# Función jugador con más precisión de pase
def jugador_precisionpase():
    pases = []
    for jugador in lista_camisetas:
        pases.append(jugador['puntos precision pase'])
    mas_pases = max(pases)
    indice = pases.index(mas_pases)
    print(f'El jugador con más precisión de pase es {lista_camisetas[indice]['nombre']}')
    print(f'Su puntaje en precisión de pases es: {mas_pases}')
    input('Presione cualquier tecla para volver al menú')


# Función jugador con más participación defensiva
def jugador_defensivo():
    defensas = []
    for jugador in lista_camisetas:
        defensas.append(jugador['participacion defensiva'])
    mas_defensas = max(defensas)
    indice = defensas.index(mas_defensas)
    print(f'El jugador con mayor participación defensiva es {lista_camisetas[indice]['nombre']}')
    print(f'Su puntaje en participación defensiva es: {mas_defensas}')
    input('Presione cualquier tecla para volver al menú')


# Función de revisión del jugador
def revision_jugador():
    while True:
        print('*' * 50)
        print('Numeros de camiseta de jugadores:')
        print(', '.join(numeros_camisetas))
        try:
            accion = input('Elige un número de camiseta: ')
            indice = numeros_camisetas.index(accion)
            datos = lista_camisetas[indice]
        except ValueError:
            system('cls')
            print('Error, elige una opción correcta')
        else:
            system('cls')
            for key, value in datos.items():
                print(f'{key.capitalize()}: {value}')
            input('Presione cualquier tecla para volver al menu')
            return


# Función comparación
def comparacion():
    while True:
        print('*' * 50)
        print('Elige a 2 jugadores a comparar')
        print('Numeros de camiseta de jugadores:')
        print(', '.join(numeros_camisetas))
        try:
            accion1 = input('Elige al primer jugador: ')
            indice1 = numeros_camisetas.index(accion1)
            accion2 = input('Elige al segundo jugador: ')
            indice2 = numeros_camisetas.index(accion2)
        except ValueError:
            system('cls')
            print('Error, ingrese los valores correctos')
        else:
            system('cls')
            datos_jugador1 = lista_camisetas[indice1]
            datos_jugador2 = lista_camisetas[indice2]
            for key, value in datos_jugador1.items():
                print(f'{key.capitalize()} : {value}')
            print('')
            for key, value in datos_jugador2.items():
                print(f'{key.capitalize()}: {value}')
            input('Presione cualquier tecla para volver al menu')
            return


# Función menú
def menu():
    while True:
        print('*' * 50)
        print('Bienvenido al programa de jugadores del Manchester United')
        print('[1] Ver datos de jugador\n[2] Comparar 2 jugadores\n[3] Ver jugador con más goles\n'
              '[4] Ver jugador con más velocidad\n[5] Ver jugador con más asistencias\n'
              '[6] Ver jugador con más precisión de pase\n[7] Ver jugador más defensivo\n[8] Terminar programa')
        try:
            accion = input('Elige una opción: ')
            ['1', '2', '3', '4', '5', '6', '7', '8'].index(accion)
        except ValueError:
            system('cls')
            print('Error, Elige una opción valida')
        else:
            return accion


# Función main
def main():
    validacion = True
    while validacion:
        system('cls')
        accion = menu()
        if accion == '1':
            system('cls')
            revision_jugador()
            continue
        elif accion == '2':
            system('cls')
            comparacion()
            continue

        elif accion == '3':
            system('cls')
            jugador_masgoles()
            continue

        elif accion == '4':
            system('cls')
            jugador_masrapido()
            continue

        elif accion == '5':
            system('cls')
            jugador_masasistencias()
            continue

        elif accion == '6':
            system('cls')
            jugador_precisionpase()
            continue

        elif accion == '7':
            system('cls')
            jugador_defensivo()
            continue

        else:
            system('cls')
            print('El programa ha sido finalizado')
            validacion = False


if __name__ == '__main__':
    main()
