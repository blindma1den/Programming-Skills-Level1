# 3.The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
# There are 3 doctors for each specialty.
# The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
# The maximum limit for appointments, in general, is 3.
# Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
# Display available specialists.
# The user can choose their preferred specialist.
# The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

USERDATA = {
    'username': 'e',
    'password': 'e'
}
AVAILABLE_SCHEDULE = ["morning - 08:00", "afternoon - 16:30"]

DOCTORS = {
    "general medicine": ["Dr. A", "Dr. B", "Dr. C"],
    "emergency care": ["Dr. A", "Dr. B", "Dr. C"],
    "clinical analysis": ["Dr. G", "Dr. H", "Dr. I"],
    "cardiology": ["Dr. J", "Dr. K", "Dr. L"],
    "neurology": ["Dr. M", "Dr. N", "Dr. O"],
    "nutrition": ["Dr. P", "Dr. Q", "Dr. R"],
    "physiotherapy": ["Dr. S", "Dr. T", "Dr. U"],
    "traumatology": ["Dr. V", "Dr. W", "Dr. X"],
    "internal medicine": ["Dr. Y", "Dr. Z", "Dr. AA"],
}

def main():
    attempts = 3
    loggedUser = User("","")
    print("\t\tWelcome to Valencia Hospital\n\n")
    while attempts > 0:
        print("Please login with your credentials:")
        user, passw = login()
        if (user != None and passw != None):
            print("Login successful")
            loggedUser.username = user
            loggedUser.password = passw
            break
        else:
            attempts -= 1
            print(f"\nAttempts left {attempts}")
    else:
        print("System Locked out")
    while not False:
        specialty = getSpecialty()
        if specialty == None:
            break
        else:
            doctor = showDoctor(specialty)
            if doctor != None:
                print(f"You have chosen {doctor} as your doctor")
                schedule = getSchedule()
                if schedule != None:
                    if loggedUser.checkAppointment(doctor,specialty):
                        print("You already have an appointment")
                    else:
                        if loggedUser.addAppointment(doctor,specialty,schedule):
                            print(f"Appointment added: {doctor} {specialty} {schedule}")
                        else:
                            print("Appointment limit exceeded")
            else:
                print("Invalid input")

def getSpecialty():
    specialty = ""
    print("\n\nChoose one specialty\n")
    print("1. General Medicine\n2. Emergency Care\n3. Clinical Analysis\n4. Cardiology\n5. Neurology\n6. Nutrition\n7. Physiotherapy\n8. Traumatology\n9. Internal Medicine\n0. Exit")
    try:
        option = int(input(">> "))
        if option == 0:
            return None
        if option == 1:
            specialty = "general medicine"
        if option == 2:
            specialty = "emergency care"
        if option == 3:
            specialty = "clinical analysis"
        if option == 4:
            specialty = "cardiology"
        if option == 5:
            specialty = "neurology"
        if option == 6:
            specialty = "nutrition"
        if option == 7:
            specialty = "physiotherapy"
        if option == 8:
            specialty = "traumatology"
        if option == 9:
            specialty = "internal medicine"
        return specialty
    except:
        print("Invalid input")

def getSchedule():
    print("Available schedules: ")
    for i in range(len(AVAILABLE_SCHEDULE)):
        print(f"{i+1}. {AVAILABLE_SCHEDULE[i]}")
    try:
        option = int(input(">> "))
        return AVAILABLE_SCHEDULE[option-1]
    except:
        print("Invalid input")

def getDoctor(specialty):
    doctors = DOCTORS[specialty]
    for i in range(len(doctors)):
        print(f"{i+1}. {doctors[i]}")
    try:
        option = int(input(">> "))
        return doctors[option-1]
    except:
        print("Invalid input")

def showDoctor(specialty):
    print("Choose one doctor: ")
    selection = getDoctor(specialty)
    return selection


def login():
    try:
        user = input("Username: ")
        if user == USERDATA['username']:
            passw = input("Password: ")
            if passw == USERDATA['password']:
                return user, passw
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None, None
    except:
        print("Invalid input")

class User:
    appointmentIndex = 0
    def __init__(self, username, password, appointments = {}):
        self.username = username
        self.password = password
        self.appointments = appointments
    
    def addAppointment(self, doctor, specialty, schedule):
        if len(self.appointments) < 3:
            self.appointments[self.appointmentIndex] = [doctor,specialty,schedule]
            self.appointmentIndex += 1
            return True
        else:
            return False
    
    def checkAppointment(self, doctor, specialty):
        for appointment in self.appointments.values():
            if appointment[0] == doctor or appointment[1] == specialty:
                return True
        return False

if __name__ == "__main__":
    main()