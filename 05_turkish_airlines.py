import os
import sys

countries = ["Turkey", "Greece", "Lebanon", "Spain", "Portugal"]
login_attempts = 0
username = "mitnick"
password = "god"
login_success = False
flight_round_trip_price = 1000
luggage_price = 50
first_class_multi = 2.2
total_price = 0
option = 0

def print_menu():
    os.system('clear')
    print("WELCOME TO TURKISH AIRLINES")
    print("===========================")
    print("1. Create a reservation")
    print("2. Exit")

def print_countries():
    count = 1
    for country in countries:
        print(count, "-", country)
        count += 1

def print_class():
    print("\n1. Economy")
    print("2. First Class")

def print_meals():
    print("\n1. Regular")
    print("2. Vegetarian")
    print("3. Kosher")

os.system('clear')
print("WELCOME TO TURKISH AIRLINES")
print("===========================")
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
        print_countries()
        origin = int(input("Choose origin country: "))
        print_countries()
        destination = int(input("Choose a destination: "))
        date = input("Date you want to travel: ")
        print_class()
        flight_class = input("Which class do you want to travel? ")
        luggage = input("Do you want to check an additional luggage? (y/n) ")
        print_meals()
        meal = input("What would you like to eat in your flight? ")
        print("\nNow we need some information about you...")
        name = input("Name: ")
        nationality = input("Nationality: ")
        passport = input("Passport number: ")
        
        #Show everything to confirm the purchase
        print("\nPurchase details")
        print("----------------")
        
        print("Country of origin:", countries[origin - 1])
        print("Destination:", countries[destination - 1])
        print("Trip date:", date)
        
        if int(flight_class) == 2:
            print("Class: First class")
            total_price = flight_round_trip_price * first_class_multi
        else:
            print("Class: Economy class")
            total_price = flight_round_trip_price
        
        if int(meal) == 2:
            print("Meal: Vetetarian")
        elif int(meal) == 3:
            print("Meal: Kosher")
        else:
            print("Meal: Regular")
        
        if luggage == "y" or luggage == "Y":
            print("Luggage: Yes")
            total_price += luggage_price
        
        print("\nTotal price:", total_price, "USD")
        print("Name:", name)
        print("Nationality:", nationality)
        print("Passport number:", passport)
        
        print("\nIs this information OK?")
        verify = input("Do you confirm this reservation? (y/n)")
        if verify == "y" or verify == "Y":
            print("\nThank you for using Turkish Airlines. Your reservation is complete.")
            print("Goodbye!")
            sys.exit()
        else:
            print("\nYour reservation will not be saved.")
            input("Press ENTER to continue")





