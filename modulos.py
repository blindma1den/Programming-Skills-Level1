def login(users):
    auth = 0
    oportunidades = 3
    while (auth == 0 and oportunidades > 0):
        name = input("Ingrese su usuario: ")
        clave = input("Ingrese su contrasenia: ")
        if clave == users.get(name):
            auth = 1
            print(" ")
            print("Usuario logueado correctamente")
            print(" ")
        else:
            print(" ")
            print("Clave Incorrecta")
            print(" ")
            oportunidades = oportunidades-1
    if oportunidades == 0:
        salida(0)
    return name


def salida(motivo): #0 Login Incorrecto, #1 Salida Voluntaria
    if motivo == 0:
        print("\nNo es posible loguearlo.")
        exit()
    return

def crearMenu(lista):

    for i in range(len(lista)):
        print("\n",i,". ", lista[i])
    print("\n", len(lista), " Volver")
    try:
        opcion = int(input("\nElija la opcion deseada: "))
    except ValueError:
        print("\nPor favor, ingrese un valor numérico.")
        opcion= crearMenu(lista)
    return opcion