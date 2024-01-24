columnas=["Nombre", "goles", "speed", "assist", "passing accuracy", "defense involments", 
        "jersey"]
bruno=["Bruno Fernandez", 5, 6 ,9,10, 3, 8]
rasmus=["Rasmus Hojlund", 12,8, 2,6,2,11]
maguire=["Harry Maguire", 1, 5, 1, 7, 9, 5]
garnacho=["Alejandro Garnacho", 8, 7, 8, 6, 0, 17]
mount=["Mason Mount", 2, 6, 4,8,1,7]

diccUsers={"haag":"1234"}

def login():
    auth=0
    oportunidades=3
    while (auth==0 and oportunidades>0):
        name=input("Ingrese su usuario: ")
        clave=input ("Ingrese su contrasenia: ")
        if clave==diccUsers.get(name):
            auth=1
            print(" ")
            print ("Usuario logueado correctamente")
            print(" ")
        else:
            print(" ")
            print ("Clave Incorrecta")
            print(" ")
            oportunidades = oportunidades-1
    if oportunidades==0:
        salida(0)
    return 

def salida(motivo):
    if motivo==0:
        print ("\nNo es posible loguearlo.")
        exit()
    return    

def menuPrincipal():
    choise=None
    while choise not in ["1","2","3", "4"]:
        print("\nProgramas posibles.")    
        print("\n1. Player review\n2. Compare \n3. Tops \n4. Salir")
        #3. fastest player \n4. top goal scorer \n5. player with the most assists \n6. player with the highest passing accuracy 7. player with the most defensive involvements")
        choise=input("\nElija la opcion deseada: ")
    return choise

def datosEnPantalla(datos,columnas):
    i=0
    print("\n")
    for columna in columnas:
        print(columna, ": ", datos[i])
        i=i+1
    return

def encontrarPosicion(bd, jersey):
    found=False
    pos=-1
    for i in range(len(bd)):
        if bd[i][6]==int(jersey):
            datosEnPantalla(bd[i],bd[0])
            found=True
            pos=i
    return found, pos

def mostrarJugador(bd): #Recibe una base de datos. Pide elegir un numero de camiseta y muestra por pantalla sus datos.
    jersey=input("\nIngrese nro de camiseta: ")
    found, posicion=encontrarPosicion(bd, jersey)
    if found:
        return
    else:
        print("No se ha encontrado el judagor")
        return

def compararJugadores(bd):
    jug1=""
    jug2=" "
    while jug1 not in ["8","11","5","17","7"] or jug2 not in ["8","11","5","17","7"] or jug1==jug2:
        jug1=input("\nIngrese jersey del primer jugador: ")
        jug2=input("\nIngrese jersey del jugador 2: ")
    found1,pos1=encontrarPosicion(bd,jug1)
    found2,pos2=encontrarPosicion(bd,jug2)

    return

def maxim(bd, columna):
    max=int(bd[1][columna])
    jugador=1
    for i in range(1,len(bd)):
        if int(bd[i][columna])>max:
            max=bd[i][columna]
            jugador=i
    print("el maximo en ", bd[0][columna], "es ", bd[jugador][0], "con ", bd[jugador][columna])

def tops(bd):
    opcion=""
    while opcion not in ["1", "2", "3", "4", "5", "6"]: 
        print("\n1. Fastest \n2. Goal Scorer \n3. asisst \4. passing accuracy \n5. defensive \n6. Salir")
        opcion=input("\nElija la opcion deseada:")
    
    if opcion in ["1", "2", "3", "4", "5"]:
        maxim(bd,int(opcion))
    else:
        return

login()
data=[columnas,bruno, rasmus, maguire, garnacho, mount]
opcion=menuPrincipal()
while True:
    if opcion=="1":
        mostrarJugador(data)
        opcion=menuPrincipal()
    else:
        if opcion=="2":
            compararJugadores(data)
            opcion=menuPrincipal()
        else:
            if opcion=="3":
                tops(data)
                opcion=menuPrincipal()
            else:
                exit()