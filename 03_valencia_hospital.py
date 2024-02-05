import os
import sys

specialties = [
    "General medicine", 
    "Emergency Care", 
    "Clinical Analysis", 
    "Cardiology", 
    "Neurology", 
    "Nutrition", 
    "Physiotherapy", 
    "Traumatology", 
    "Internal Medicine"
]

doctors = {
    "General medicine": {"doctors": ["Doctor House", "Meredith Grey","Derek Shepherd"]},
    "Emergency Care": {"doctors": ["Alex Karev", "Lexie Grey", "Izzie Stevens"]},
    "Clinical Analysis": {"doctors": ["Andrew DeLuca", "Mark Sloan", "Miranda Bailey"]},
    "Cardiology": {"doctors": ["Cristina Yang", "Owen Hunt", "Maggie Pierce"]},
    "Neurology": {"doctors": ["Amelia Sheperd", "April Kepner", "Jackson Avery"]},
    "Nutrition": {"doctors": ["Richard Webber", "Ellis Grey", "Addison Montgomery"]},
    "Physiotherapy": {"doctors": ["George O'Malley", "Finn Dandridge", "Eric Foreman"]},
    "Traumatology": {"doctors": ["Allison Cameron", "Robert Chase", "Remy Hadley"]},
    "Internal Medicine": {"doctors": ["Chris Taub", "Philip Weber", "Dana Miller"]}
}

users = []

appointments = []

login_attempts = 0
username = "mitnick"
password = "god"
option = 0

def print_menu():
    os.system('clear')
    print("WELCOME TO VALENCIA HOSPITAL")
    print("============================")
    print("1. Schedule an appointment")
    print("2. Exit")

def print_specialties():
    count = 1
    for specialty in specialties:
        print(count, "-", specialty)
        count += 1

def verify_appointment(name, doctor, specialty):
    if len(appointments) == 0:
        return [True,""]
    count_name = 0
    count_doctor = 0
    count_specialty = 0
    for appointment in appointments:
        if appointment[0] == name:
            count_name += 1
        if appointment[0] == name and appointment[1] == doctor:
            count_doctor += 1
        if appointment[0] == name and appointment[2] == specialty:
            count_specialty += 1
    # print("Counts:", count_name, count_doctor, count_specialty)
    
    if count_doctor >= 1:
        return [False, "You already have an appointment with " + doctor]
    
    if count_specialty >= 1:
        return [False, "You already have an appointment in the specialty " + specialty]
    
    if count_name > 2:
        return [False, "You already have 3 appointments. Sorry"]
    else:
        return [True,""]

os.system('clear')
print("WELCOME TO VALENCIA HOSPITAL")
print("============================")
while login_attempts !=3:
    user_login = input("Username: ")
    pass_login = input("Password: ")
    if username == user_login and password == pass_login:
        login_success = True
        break
    else:
        login_attempts += 1
        if login_attempts == 3:
            print("Better luck next time! Bye.")
            sys.exit()
        print("Sorry, try again.")

while option != 2:
    print_menu()
    option = int(input("Choose an option: "))
    if option == 1:
        print_specialties()
        option_specialty = int(input("Choose a specialty: "))
        print("")
        user_name = input("What's your name? ")
        print("")
        i = 1
        for doctor in doctors[specialties[option_specialty - 1]]["doctors"]:
            print(str(i) + "- " + doctor)
            i += 1
        
        doctor_option = int(input("Choose a doctor: "))
        select_doctor = doctors[specialties[option_specialty - 1]]["doctors"][doctor_option - 1]
        result = [True, ""]
        result = verify_appointment(user_name, select_doctor, specialties[option_specialty - 1])
        if result[0] == True:
            appointments.append([user_name, select_doctor, specialties[option_specialty - 1]])
            print("Your appointment is saved.")
        else:
            print("\nThere is an error with your appointment. " + result[1])
        input("\nPress ENTER to continue")