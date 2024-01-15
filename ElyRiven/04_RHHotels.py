# 4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

# Login; it should be locked after the third failed attempt.
# The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
# Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
# All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
# The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
# Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
# The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
# print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.

USERDATA = {
    'username': 'e',
    'password': 'e'
}

Spain_Hotels = [
    {
        "madrid": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "barcelona": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "valencia": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }    
    }
]

France_Hotels = [
    {
        "paris": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "marseille": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    }
]

Portugal_Hotels = [
    {
        "madeira": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "lisbon": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "porto": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }    
    },
]

Italy_Hotels = [
    {
        "rome": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3,
        }
    },
    {
        "milan": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3, 
        }
    }
]

Germany_Hotels = [
    {
        "munich": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3, 
        }
    },
    {
        "berlin": {
            "single": 3,
            "double": 6,
            "group": 6,
            "vip": 6,
            "luxury": 3, 
        }
    }
]

ROOM_PRICES = {
    "single": 100,
    "double": 200,
    "group": 350,
    "vip": 450,
    "luxury": 550,
}

def main():
    attempt = 3
    print("\t\tWelcome to RH Hotels\n\n")
    while attempt > 0:
        print("Please login with your credentials")
        user, passw = login()
        if (user != None and passw != None):
            print("Login successful")
            break
        else:
            attempt -= 1
            print(f"\nAttempts left {attempt}")
    else:
        print("System Locked out")
    while True:
        country, hotels = getCountry()
        city, rooms = getCity(hotels)
        roomType, cost = getRoomType(rooms)
        nights = getNights()
        userData = getUserInfo()
        reservation = [country, city, roomType, nights, cost * nights]
        print(f"\nReservation details:\n\nCountry: {reservation[0].title()}\nCity: {reservation[1].title()}\nRoom type: {reservation[2].title()}\nNights: {reservation[3]}\nTotal cost: ${reservation[4]}\n")
        if confirmReservation(city, roomType):
            print("Reservation confirmed")
            continue
        else:
            print("Reservation cancelled")
            break

# Ask the user to confirm the reservation
def confirmReservation(selectedCity, roomType):
    countries = [Spain_Hotels, France_Hotels, Portugal_Hotels, Italy_Hotels, Germany_Hotels]
    while True:
        confirm = input("Do you want to confirm the reservation? (y/n): ").lower()
        if confirm == "y":
            for hotels in countries:
                for i, hotel in enumerate(hotels):
                    if selectedCity in hotel:
                        hotel[selectedCity][roomType] -= 1
                        return True
                    else:
                        continue
        elif confirm == "n":
            return False
        else:
            print("Invalid input\n")

# Ask the user information
def getUserInfo():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    id = input("Please enter your ID/Passport: ")
    return [name, surname, id]

# Ask the number of nights
def getNights():
    while True:
        try:
            nights = int(input("Please enter the number of nights: "))
            if nights > 0:
                return nights
            else:
                print("Invalid number of nights\n")
        except ValueError:
            print("Invalid input\n")

# Ask the desired room type
def getRoomType(rooms):
    while True:
        print("Please select a room type")
        for i, available in enumerate(list(rooms.items())):
            print(f"{i+1}. {available[0].title()} - {available[1]} available")
        try:
            room_index = int(input(">> ")) - 1
            if 0 <= room_index < len(rooms):
                selectedRoom = list(rooms.keys())[room_index]
                if rooms[selectedRoom] > 0:
                    return selectedRoom, ROOM_PRICES[selectedRoom]
                else:
                    print(f"Type room {selectedRoom.title()} is not available\n")
            else:
                print("Invalid room type\n")
        except ValueError:
            print("Invalid input\n")

# Ask the desired city and return the list of rooms available
def getCity(availableHotels):
    while True:
        print("Please select a city")
        for i, hotel in enumerate(availableHotels):
            city = list(hotel.keys())[0]
            print(f"{i+1}. {city.title()}")
        try:
            city_index = int(input(">> ")) - 1
            if 0 <= city_index < len(availableHotels):
                selectedCity = list(availableHotels[city_index].keys())[0]
                return selectedCity, availableHotels[city_index][selectedCity]
            else:
                print("Invalid city\n")
        except ValueError:
            print("Invalid input\n")

# Ask the desired country and return the list of hotels available
def getCountry():
    while True:
        print("Please select a country")
        print("1. Spain")
        print("2. France")
        print("3. Portugal")
        print("4. Italy")
        print("5. Germany")
        try:
            country = int(input(">> "))
            if country == 1:
                return "Spain", Spain_Hotels
            elif country == 2:
                return "France", France_Hotels
            elif country == 3:
                return "Portugal", Portugal_Hotels
            elif country == 4:
                return "Italy", Italy_Hotels
            elif country == 5:
                return "Germany", Germany_Hotels
            else:
                print("Invalid country\n")
        except ValueError:
            print("Invalid input\n")

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

if __name__ == "__main__":
    main()