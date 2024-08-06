'''The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.'''

class User:
    username:str
    password:str
    limit:int

class Appointment:
    generalMedicine:str
    emergencyCare:str
    clinicalAnalysis:str
    cardiology:str
    neurology:str
    nutrition:str
    physiotherapy:str
    traumatology:str
    internalMedicine:str

def login(username, password):
    for i in range(3):
        if username and password:
            return True
        else:False
