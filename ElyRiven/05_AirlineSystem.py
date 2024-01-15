# 5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:

# It must have a login and validate the data; after the third failed attempt, it should be locked.
# The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
# The user must choose if they want to check an additional piece of luggage into the hold.
# Hand luggage is free of charge.
# The user must purchase both the outbound and return tickets.
# The user can choose their preferred meal: Regular, Vegetarian, Kosher.
# The program must collect the following data: Name, country of origin, passport, and destination country.
# Upon completing the process, the system will display everything the user has previously chosen along with their information. 
# The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.

from datetime import datetime

USERDATA = {
    'username': 'elizabeth',
    'password': 'pass123'
}

DESTINATIONS = ['turkey', 'greece', 'lebanon', 'spain', 'portugal']
CONDITIONS = ['economy', 'first class']
MEALS = ['regular', 'vegetarian', 'kosher']

def main():
    print("Welcome to Turkish Airlines\n")
    login()
    while True:
        originCountry = getOriginCountry()
        destinationCountry = getDestinationCountry(originCountry)
        date = getDate()
        condition = getCondition()
        additionalLuggage = getAdditionalLuggage()
        meal = getMeal()
        userData = getUserData(originCountry, destinationCountry)
        print("\nFlight Summary\n")
        print(f"User Data:\nName: {userData[0]} \nPassport: {userData[1]}\n")
        print(f"Origin Country: {originCountry.title()}\nDestination Country: {destinationCountry.title()}\nDate: {date}\nCondition: {condition.title()}\nAdditional Luggage: {additionalLuggage}\nMeal: {meal.title()}\n")
        if getConfirmation():
            print("Reservation confirmed\n")
        else:
            print("Reservation cancelled\n")

# Confirm flight
def getConfirmation():
    while True:
        confirmation = input("Confirm flight? (Y/N): ").lower()
        if confirmation == 'y':
            return True
        elif confirmation == 'n':
            return False
        else:
            print("Invalid input\n")

# Get user data
def getUserData(origin, destination):
    name = input("Name: ")
    passport = input("Passport: ")
    print(f"Origin Country: {origin.title()}")
    print(f"Destination Country: {destination.title()}")
    return [name,passport]

# Get meal preference
def getMeal():
    while True:
        print("Available Meals \n")
        for i,meal in enumerate(MEALS):
            print(f"{i+1}. {meal.title()}")
        try:
            meal = int(input(">> ")) -1
            if 0 <= meal < len(MEALS):
                return MEALS[meal]
            else:
                print("Invalid meal\n")
        except ValueError:
            print("Invalid input\n")

# Ask if user wants to check additional luggage
def getAdditionalLuggage():
    while True:
        additionalLuggage = input("Do you want to check additional luggage? (Y/N): ").lower()
        if additionalLuggage == 'y':
            return "Yes"
        elif additionalLuggage == 'n':
            return "No"
        else:
            print("Invalid input\n")

# Get condition of flight
def getCondition():
    while True:
        print("Available Conditions \n")
        for i,condition in enumerate(CONDITIONS):
            print(f"{i+1}. {condition.title()}")
        try:
            condition = int(input(">> ")) -1
            if 0 <= condition < len(CONDITIONS):
                return CONDITIONS[condition]
            else:
                print("Invalid condition\n")
        except ValueError:
            print("Invalid input\n")

# Get date of flight
def getDate():
    while True:
        date = input("Date of flight (DD/MM/YYYY): ")
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return date
        except ValueError:
            print("Invalid input\n")

# Show available destinations based on origin country
def getDestinationCountry(origin):
    while True:
        print("Available Final Destinations \n")
        for i,country in enumerate(DESTINATIONS):
            if country != origin:
                print(f"{i+1}. {country.title()}")
        try:
            destinationCountry = int(input(">> ")) -1
            if 0 <= destinationCountry < len(DESTINATIONS) and DESTINATIONS[destinationCountry] != origin:
                return DESTINATIONS[destinationCountry]
            else:
                print("Invalid country\n")
        except:
            print("Invalid input\n")

# Show available origin countries
def getOriginCountry():
    while True:
        print("Available Origin Destinations \n")
        for i,country in enumerate(DESTINATIONS):
            print(f"{i+1}. {country.title()}")
        try:
            originCountry = int(input(">> ")) -1
            if 0 <= originCountry < len(DESTINATIONS):
                return DESTINATIONS[originCountry]
            else:
                print("Invalid country\n")
        except ValueError:
            print("Invalid input\n")

def login():
    attempts = 3
    print("Please login to continue\n")
    while attempts > 0:
        try:
            user = input("Username: ")
            if user == USERDATA['username']:
                passw = input("Password: ")
                if passw == USERDATA['password']:
                    return True
                else:
                    print("Invalid password")
            else:
                print("Invalid username")
            attempts -= 1
            print(f"Attempts left: {attempts}\n")
        except:
            print("Invalid input")
    else:
        print("Too many failed attempts. Please try again later")
        return False

if __name__ == "__main__":
    main()