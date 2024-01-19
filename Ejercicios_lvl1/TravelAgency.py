# Por Felipe (ZenTial)
# 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:
#
# Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the
# Swiss Alps. Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal,
# there are activities on the beaches. Spring: France and Italy. In France, there are extreme sports activities,
# and in Italy, there's a cultural and historical tour. Autumn: Belgium and Austria. In Belgium, there are hiking and
# extreme sports activities, and in Austria, there are cultural and historical activities. Note: Traveling in winter
# costs $100, in autumn $200, in spring $300, and in summer $400.
# Design a system that helps users choose their best destination according to their personal preferences and the
# season they want to travel in. 12. Important: With the information you have, you should ask the user the right
# questions and display on screen what their best destination would be.
#
# Clue: You could consider the user's budget
from os import system

# Declaración de variables
actividades = ['esquiar', 'turismo de los alpes suizos', 'senderismo', 'deportes extremos',
               'playas', 'turismo historico y cultural']
invierno = ['esquiar', 'turismo de los alpes suizos', {'nombre': 'invierno', 'precio': '100'}]
verano = ['senderismo', 'deportes extremos', 'playas', {'nombre': 'verano', 'precio': '200'}]
primavera = ['deportes extremos', 'turismo histórico y cultural', {'nombre': 'primavera', 'precio': '300'}]
otoño = ['senderismo', 'deportes extremos', 'turismo histórico y cultural', {'nombre': 'otoño', 'precio': '400'}]
estaciones = [invierno, verano, primavera, otoño]
indice_estaciones = ['invierno', 'verano', 'primavera', 'otoño']
precios = ['100', '200', '300', '400']


# Función de busqueda de actividad en las estaciones correspondiente
def busqueda(actividad1, actividad2):
    actividades_elegidas = []
    for estacion in estaciones:
        if actividad1 in estacion:
            actividades_elegidas.append(estacion)
    for estacion in estaciones:
        if actividad2 in estacion:
            actividades_elegidas.append(estacion)
    return actividades_elegidas


# Función del menú
def preguntas():
    while True:
        print('*' * 50)
        print('Bienvenido a nuestra agencía de viaje usuario, por favor\n'
              'Elige 2 actividades entre las disponibles a continuación:')
        for actividad in actividades:
            print(f'[{actividad.capitalize()}]')
        try:
            eleccion1 = input('Elige la primera actividad: ')
            actividades.index(eleccion1.lower())
            eleccion2 = input('Elige la segunda actividad: ')
            actividades.index(eleccion2.lower())
        except ValueError:
            system('cls')
            print('Error, elige una actividad valida')
        else:
            system('cls')
            opciones = busqueda(eleccion1.lower(), eleccion2.lower())
            precios_disponibles = set([])
            lista_precios = []
            for zona in opciones:
                precios_disponibles.add(zona[-1]['precio'])
            for precio in precios_disponibles:
                lista_precios.append(precio)
            return lista_precios


# Función para elegir opción final según presupuesto
def elegir_viaprecios(lista):
    while True:
        lista.sort()
        print('*' * 50)
        print('Elige un presupuesto en base a esta lista: ')
        print(', '.join(lista))
        try:
            presupuesto = input('¿Cual es su presupuesto?: ')
            indice = precios.index(presupuesto)
        except ValueError:
            system('cls')
            print('Elige un presupuesto valido')
        else:
            system('cls')
            estacion_elegida = estaciones[indice]
            print(f'La mejor opción en base a sus preferencias sera viajar en {estacion_elegida[-1]['nombre']}')
            return


# Función main del programa
def main():
    while True:
        system('cls')
        preferencias = preguntas()
        elegir_viaprecios(preferencias)
        print('Gracias por usar nuestro servicios')
        return


if __name__ == '__main__':
    main()
