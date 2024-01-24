# Ejercicio 2

diccEstaciones = {"Winter": ["Andorra", "Switzerland"], "Summer": [
    "Spain", "Portugal"], "Spring": ["France", "Italy"], "Autumn": ["Belgium", "Austria"]}
diccPresupuesto = {"Winter": 100, "Summer": 400, "Spring": 300, "Autumn": 200}
presupuesto = ["Winter", "Autumn", "Spring", "Summer"]
diccPaises = {"Andorra": "skiing activities", "Switzerland": "tour of the Swiss Alps", "Spain": "hiking and extreme sports activities", "Portugal": "activities on the beaches",
              "France": "extreme sports activities", "Italy": "cultural and historical tour", "Belgium": "hiking and extreme sports activities", "Austria": "cultural and historical activities"}


def menuEstaciones(opciones):
    for i in range(opciones):
        print("\n", i+1, ". ", presupuesto[i])
    res = input("\ningrese estacion deseada: ")
    return int(res)-1


def menuDestinos(dest):
    print("Los destinos posibles son ")
    estacion = presupuesto[dest]
    destinos = diccEstaciones[estacion]

    for destino in destinos:
        print("\n", destino)
    pais = input("\nopcion elegida: (1 o 2) ")
    return pais


def sugerencias(estacion, pais):
    season = presupuesto[estacion]
    country = diccEstaciones[season][pais]
    print("\nEn ", season, " le sugerimos ", country)
    print("\nAlli puede realizar ", diccPaises[country])


bud = int(input("\n Cuanto es el presupuesto? "))
if bud < 100:
    print("No hay opciones por ese monto")
else:
    if bud < 200:
        est = menuEstaciones(1)
    elif bud < 300:
        est = menuEstaciones(2)
    elif bud < 400:
        est = menuEstaciones(3)
    else:
        est = menuEstaciones(4)

    pais = menuDestinos(int(est))

    sugerencias(int(est),int(pais)-1)

print("\nLe deseamos buen viaje\n\n")