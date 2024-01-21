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
        option_specialty = int(input("Choose a specialty:"))
        print(doctors[specialties[option_specialty - 1]])
        input("Press ENTER to continue")