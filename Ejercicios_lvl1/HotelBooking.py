# Por Felipe (ZenTial)

# 4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application: Login; it should
# be locked after the third failed attempt. The RH Hotels chain exists in 5 countries: Spain, France, Portugal,
# Italy, and Germany. Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome,
# Milan, Paris, Marseille, Madeira, Lisbon, and Porto. All hotels have 24 rooms each: 6 VIP suites, 3 single rooms,
# 6 double rooms, 6 group rooms, and 3 luxury suites. The user can make reservations at any time of the year and at
# any hour, and book as many rooms as desired. Single rooms are priced at $100 per night, double rooms at $200 per
# night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night,
# applicable at any time of the year. The algorithm functions as follows: Login, choose country, choose city,
# choose room type, select the number of nights, collect user data (name, surname, ID/passport), print the total
# cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.
from os import system

# Declaración de variables
paises = ['españa', 'francia', 'portugal', 'italia', 'alemania']
ciudades = ['madrid', 'barcelona', 'valencia', 'munich', 'berlin', 'roma', 'milan', 'paris', 'marsella',
            'madeira', 'lisboa']
españa = ['madrid', 'barcelona', 'valencia']
francia = ['paris', 'marsella']
portugal = ['lisboa', 'madeira']
italia = ['roma', 'milan']
alemania = ['munich', 'berlin']
lista_paises = [españa, francia, portugal, italia, alemania]
dict_precios = {'individual': 100, 'doble': 200, 'grupal': 350, 'vip': 450, 'lujo': 550}


# Función del menú
def menu(lista_vacia):
    while True:
        print('*' * 50)
        print('Bievenido a la cadena de hoteles RH')
        for pais in paises:
            print(pais.capitalize())
        try:
            pais_elegido = input('Elija un país: ').lower()
            indice = paises.index(pais_elegido)
        except ValueError:
            system('cls')
            print('Error, elija un país que exista')
        else:
            lista_vacia[0] = pais_elegido.capitalize()
            lista_vacia[3] = lista_paises[indice]
            return lista_vacia


# Función para elegir ciudad
def elegir_ciudad(lista_datos):
    while True:
        print('*' * 50)
        print('Elige una ciudad de la lista de las disponibles:')
        for ciudad in lista_datos[3]:
            print(ciudad.capitalize())
        try:
            ciudad_elegida = input('').lower()
            lista_datos[3].index(ciudad_elegida)
        except ValueError:
            system('cls')
            print('Error, elige una ciudad que exista')
        else:
            lista_datos[1] = ciudad_elegida.capitalize()
            return lista_datos


# Función calcular cantidad de dinero según habitaciones agendadas
def calcular_habitaciones():
    balance = 0
    individual = 3
    doble = 6
    grupal = 6
    vip = 6
    lujo = 3
    lista_cantidades = [individual, doble, grupal, vip, lujo]
    while True:
        indice_cantidad = 0
        system('cls')
        print('*' * 50)
        print('Agende la cantidad de habitaciones que desee')
        print('Lista de tipo de habitación, precio por noche y cantidad disponible:')
        for key, value in dict_precios.items():
            print(f'{key.capitalize()} = ${value}')
            print(lista_cantidades[indice_cantidad])
            indice_cantidad += 1
        print('[C] Escriba este valor cuando quiera terminar de agendar habitaciones')
        try:
            habitacion_elegida = input('Escoge una habitación: ').lower()
            indice = ['individual', 'doble', 'grupal', 'vip', 'lujo', 'c'].index(habitacion_elegida)
        except ValueError:
            system('cls')
            print('Error, elija un tipo de habitación que exista')
        else:
            if habitacion_elegida != 'c':
                precio = dict_precios[habitacion_elegida]
                precio_habitaciones, habitaciones_reservadas = cantidad_habitaciones(precio, lista_cantidades, indice)
                lista_cantidades[indice] -= habitaciones_reservadas
                precio_habitacion_total = cantidad_noches(precio_habitaciones)
                balance += precio_habitacion_total
            else:
                return balance


# Función que pide la cantidad de habitaciones de un tipo
def cantidad_habitaciones(precio_habitacion, listacantidad, indice):
    while True:
        try:
            cantidad = input('Cuantas habitaciones de este tipo desea: ')
            precio = precio_habitacion * int(cantidad)
        except TypeError:
            system('cls')
            print('Error, elige un valor que sea un número')
        else:
            if int(cantidad) > listacantidad[indice]:
                print('Esta ordenando más habitaciones de las que nos quedan de este tipo')
            else:
                return precio, int(cantidad)


# Función para calcular precior por la cantidad de noches
def cantidad_noches(precio):
    while True:
        try:
            noches = input('¿Cuantas noches desea estar?: ')
            precio_final = precio * int(noches)
        except TypeError:
            system('cls')
            print('Error, ingrese un valor númerico')
        else:
            return precio_final


# Función para imprimir los datos del usuario
def imprimir_usuario(datos):
    nombre = input('Escriba su nombre: ')
    apellido = input('Escriba su apellido: ')
    passport = input('Escriba su id: ')
    system('cls')
    while True:
        print(f'Datos:\nNombre: {nombre}\nApellido: {apellido}\nID/Passport: {passport}\n'
              f'País: {datos[0]}\nCiudad: {datos[1]}\nPrecio total: ${datos[2]}')
        try:
            accion = input('¿Quiere confirmar la operación? [S/N]: ')
            ['s', 'n'].index(accion)
        except ValueError:
            system('cls')
            print('Error, elige una opción correcta\n')
        else:
            if accion == 'n':
                return accion
            else:
                system('cls')
                print('Su operación ha sido confirmada con exito\nGracias por usar nuestro servicios')
                return accion


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


# Función main del programa
def main():
    inicio_sesion()
    while True:
        system('cls')
        datos_usuario = ['', '', '', '', '', '']
        system('cls')
        datos_usuario = menu(datos_usuario)
        system('cls')
        datos_usuario = elegir_ciudad(datos_usuario)
        system('cls')
        datos_usuario[2] = calcular_habitaciones()
        system('cls')
        finalizacion = imprimir_usuario(datos_usuario)
        if finalizacion == 'n':
            continue
        else:
            return


if __name__ == '__main__':
    main()
