"""3. 

The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot."""

import datetime

# Hacemos una clase Hospital la cual va tener toda la informacion para validar y acceder a la misma con sus respectivos setter y getter

class Hospital:
    def __init__(self):
        self.usuario = {"Lucas":12345,"Martin":1234,"Keila":123}
        self.doctor = {"General Medicine":["juan","lucas","Gallo"],"Emergency Care":["jehova","david","jonathan"],"Clinical Analysis":["Lula","Milei","Trump"],"Cardiology":["marcos","facundo","Roberto"],"Neurology":["kian","Osiris","Liana"],"Nutrition":["Clarita","bulma","Kiara"],"Physiotherapy":["Sofia","Sabrina","delfina"],"Traumatology":["juana","Riana","Artemisa"],"Internal Medicine":["Raul","Lucio","Ambesa"]}
        self.category = ["General Medicine", "Emergency Care", "Clinical Analysis", "Cardiology", "Neurology", "Nutrition", "Physiotherapy", "Traumatology", "Internal Medicine"]
        self.appointments = {} # se agregaran las citas como datetime:[doctor,especialidad,usuario]


    def validate_pass(self, usuario, password):
        """Función que valida las contraseñas ingresadas"""
        if usuario not in self.usuario:
            raise ValueError("Usuario inválido")
        if self.usuario[usuario] != password:
            raise ValueError("Contraseña incorrecta")
        return True  # Si el usuario y la contraseña son correctos
    
    def validate_doctor(self, doctor, date_time):
        """Función que valida si un doctor está disponible en una fecha y hora"""
        if date_time in self.appointments:
            # Verificamos si el doctor ya tiene una cita programada en esa fecha
            for appointment in self.appointments[date_time]:
                if appointment[0] == doctor:
                    raise ValueError(f"El doctor {doctor} ya tiene una cita a esta hora.")
        else:
            self.appointments[date_time] = []  # Crear una nueva lista de citas en esa hora

        return True

    def make_appointment(self, usuario, doctor, category, date_time):
        """Función que permite al usuario hacer una cita"""
        if self.validate_doctor(doctor, date_time):  # Valida si el doctor está disponible
            self.appointments[date_time].append([doctor, category, usuario])
            print(f"Cita confirmada con {doctor} para la categoría {category} a las {date_time}")
        else:
            print("El doctor no está disponible en este horario.")
        
    

####################################### Aplicacion Principal #######################################

hospital = Hospital()

# Primero validamos un usuario
try:
    hospital.validate_pass("Lucas", 12345)
    print("Usuario validado correctamente")
except ValueError as e:
    print(f"Error: {e}")

# Luego hacemos una cita
try:
    # Hacemos una cita para el doctor "juan" en "General Medicine" a las 2024-12-03 10:00
    date_time = datetime.datetime(2024, 12, 3, 10, 0)
    hospital.make_appointment("Lucas", "juan", "General Medicine", date_time)
except ValueError as e:
    print(f"Error: {e}")

# Intentamos hacer otra cita para el mismo doctor a la misma hora
try:
    hospital.make_appointment("Martin", "juan", "Emergency Care", date_time)
except ValueError as e:
    print(f"Error: {e}")

