# Por Felipe (ZenTial)

# 5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon,
# Spain, and Portugal. Develop an algorithm with the following characteristics: It must have a login and validate the
# data; after the third failed attempt, it should be locked. The user must choose the origin country and the
# destination country, the flight date, and the condition: Economy or First Class. The user must choose if they want
# to check an additional piece of luggage into the hold. Hand luggage is free of charge. The user must purchase both
# the outbound and return tickets. The user can choose their preferred meal: Regular, Vegetarian, Kosher. The program
# must collect the following data: Name, country of origin, passport, and destination country. Upon completing the
# process, the system will display everything the user has previously chosen along with their information. The system
# will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message
# will appear. If not, it will return to the main menu.
from os import system
import re

# Declaración de variables
destinos = ['turquia', 'grecia', 'lebanon', 'españa', 'portugal']
comidas = ['regular', 'vegetariana', 'kosher']


# Función de inicio de sesión
def inicio_sesion():
    usuario = 'admin'
    password = 'python'
    intentos = 0
    while True:
        try:
            usuario_input = input('Ingrese un usuario: ')
            contrasena_input = input('Ingrese una contraseña: ')
            [usuario].index(usuario_input)
            [password].index(contrasena_input)

        except ValueError:
            intentos += 1
            system('cls')
            print('Ingresa las credenciales correctas.')

        else:
            system('cls')
            return True

        finally:
            if intentos == 3:
                system('cls')
                print('El sistema ha sido bloqueado debido a que ha hecho muchos intentos')
                return False


# Función para calcular el precio según la cantidad de equipaje
def cantidad_equipaje():
    while True:
        try:
            cantidad = input('Cuantas maletas extra va a llevar?: ')
            precio = int(cantidad) * 20
        except TypeError:
            system('cls')
            print('Error, elige un valor que sea un número')
        else:
            return precio


# Función para el equipaje adicional
def equipaje_adicional(lista):
    precio_total = 200
    while True:
        try:
            equipaje = input('¿Desea llevar equipaje adicional? [S/N]: ')
            print('Se le cobraran $20 extra por cada equipaje')
            ['s', 'n'].index(equipaje)
        except ValueError:
            system('cls')
            print('Error, ingrese una opción valida')
        else:
            if equipaje == 'n':
                lista[5] = precio_total
                return lista
            else:
                precio = cantidad_equipaje()
                precio_total += precio
                lista[5] = precio_total
                return lista


# Función para decidir si confirmar datos o volver al menú
def imprimir_confirmar(lista):
    nombre = input('Escriba su nombre: ')
    passport = input('Escriba la id de su pasaporte: ')
    while True:
        system('cls')
        print('*' * 50)
        print(f'Nombre: {nombre}\nId de pasaporte: {passport}\nPaís de origen: {lista[0]}\n'
              f'País de destino: {lista[1]}\nFecha de vuelo: {lista[2]}\nComida preferida: {lista[3]}\n'
              f'Tipo de billete: {lista[4]}\nPrecio total: ${lista[5]}')
        try:
            reservacion = input('¿Desea confirmar la reservación? [S/N]: ')
            ['s', 'n'].index(reservacion)
        except ValueError:
            system('cls')
            print('Error, elija una opción valida')
        else:
            return reservacion


# Función para la preferencia de comida
def comidaycondicion(lista):
    while True:
        print('*' * 50)
        print('Elige tu tipo de comida preferida de esta lista: ')
        for comida in comidas:
            print(comida.capitalize())
        try:
            comida_elegida = input('Elige tu comida: ').lower()
            comidas.index(comida_elegida)
            system('cls')
            condicion_viaje = input('¿Desea ir en Primera clase o en clase Economica?: ').lower()
            ['primera clase', 'economica'].index(condicion_viaje)
        except ValueError:
            system('cls')
            print('Error, elige un tipo de comida valido')
        else:
            lista[3] = comida_elegida.capitalize()
            lista[4] = condicion_viaje.capitalize()
            return lista


# Función para la fecha de vuelo
def fecha_vuelo(lista):
    patron = r'\d{2}-\d{2}'
    while True:
        print('*' * 50)
        try:
            vuelo = input('Escriba la fecha de su vuelo en el siguiente formato (%%-%%): ')
            confirmacion = re.search(patron, vuelo).group()
        except AttributeError:
            system('cls')
            print('Error, ingrese un tipo de fecha valido')
        else:
            lista[2] = confirmacion
            return lista


# Función del menú
def menu(lista):
    while True:
        print('*' * 50)
        print('Bienvenido a nuestras aerolineas, ambos billetes de ida y vuelta cuestan $100')
        for destino in destinos:
            print(destino.capitalize())
        try:
            pais_origen = input('De esta lista, elige tu país de origen: ').lower()
            destinos.index(pais_origen)
            pais_destino = input('De esta lista, elige tu país de destino: ').lower()
            destinos.index(pais_destino)
        except ValueError:
            system('cls')
            print('Error, escriba un país valido')
        else:
            lista[0] = pais_origen.capitalize()
            lista[1] = pais_destino.capitalize()
            return lista


# Función main del programa
def main():
    inicio_sesion()
    while True:
        lista_datos = ['', '', '', '', '', '']
        system('cls')
        lista_datos = menu(lista_datos)
        system('cls')
        lista_datos = fecha_vuelo(lista_datos)
        system('cls')
        lista_datos = comidaycondicion(lista_datos)
        system('cls')
        lista_datos = equipaje_adicional(lista_datos)
        system('cls')
        confirmacion = imprimir_confirmar(lista_datos)
        if confirmacion == 's':
            system('cls')
            print('Gracias por usar nuestro servicios')
            return
        else:
            continue


if __name__ == '__main__':
    main()
