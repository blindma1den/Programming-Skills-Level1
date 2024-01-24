"""The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot."""

from modulos import *

def chequearBloque(opcion, doctor, bloque, hora):
    doc=diccDoctors[especialidades[opcion]][doctor]
    turno=diccSchedule[doc][bloque][hora]
    return turno==0

diccUsers = {"Mena": "1234"}
diccDoctors = {"General Medicine":["Romero", "Figal", "Rojo"], "Emergency Care":[], "Clinical Analysis":[], "Cardiology":[],
               "Neurology":[], "Nutrition":[], "Physiotherapy":[], "Traumatology":["Advincula", "Blondel", "Cavani"], "Internal Medicine":[]}
diccSchedule = {"Romero":[[1,1,1,1],[0,0,0,0]], "Figal":[[0,0,0,0],[1,1,1,1]], "Rojo":[[0,0,1,1],[1,0,1,0]]}
especialidades=["General Medicine", "Emergency Care", "Clinical Analysis", "Cardiology", "Neurology", "Nutrition", "Physiotherapy", "Traumatology", "Internal Medicine"]
turnos=["maniana", "tarde"]
horarios=[["9 hs", "10 hs", "11 hs", "12 hs"],["15 hs", "16 hs", "17 hs", "18 hs"]]
diccTurnosPaciente=dict.fromkeys(diccUsers.keys(),[3])

paciente=login(diccUsers)
opcion=crearMenu(especialidades)
while opcion!=len(especialidades):
    doctor=crearMenu(diccDoctors[especialidades[opcion]])
    docName = diccDoctors[especialidades[opcion]][doctor]
    if doctor==len(diccDoctors[especialidades[opcion]]):
        opcion=crearMenu(especialidades)
    else:
        bloque=crearMenu(turnos)
        if bloque==len(turnos):
            opcion = crearMenu(especialidades)
        else:
            hora=crearMenu(horarios[bloque])
            if hora==len(horarios[bloque]):
                opcion = crearMenu(especialidades)
            else:
                if chequearBloque(opcion, doctor, bloque, hora):
                    if diccTurnosPaciente[paciente][0]>0:
                        if docName not in diccTurnosPaciente[paciente]:
                            diccTurnosPaciente[paciente][0] = diccTurnosPaciente[paciente][0]-1
                            diccTurnosPaciente[paciente].append(docName)
                            print("\nTurno Guardado correctamente")
                        else:
                            print("\nYa tiene un turno con ese medico")
                    else:
                        print("Ya no puede tomar mas turnos por hoy")
                else:
                    print("Horario no disponible")
                opcion=crearMenu(especialidades)

salida(1)
