'''
4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

Login; it should be locked after the third failed attempt.

The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome,
Milan, Paris, Marseille, Madeira, Lisbon, and Porto.

All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night,
group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night,
applicable at any time of the year.

The algorithm functions as follows: Login, choose country, choose city, choose room type,
select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation.
If not, return to the main menu.

'''


users= {}
locations = {'Spain': ['Barcelona', 'Madrid', 'Valencia'], 'France': ['Paris', 'Marseille'],'Portugal': ['Madeira', 'Lisbon', 'Porto'],
                'Italy': ['Rome', 'Milan'], 'Germany': ['Munich', 'Berlin']}
rooms = {'VIPS': 6, 'single rooms': 3, 'double rooms': 6, 'group rooms': 6, 'suites': 3}
price = {'VIPS': 450, 'single rooms': 100, 'double rooms': 200, 'group rooms': 350, 'suites': 550}


import getpass


def user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    
    if username not in users: 
        users[username] = {'password': password} 
        print("Registered successfully.")
    else:
        print("Username already exists. Please choose a different username.")
        

def login():
    
    attempts= 0
    while attempts < 3:
        
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        if username in users:
            if users[username]['password'] == password: 
                print("Welcome,", username)
                return True, username
            else:
                attempts += 1
                print("Invalid username or password.")
                print("Attempts:", attempts, "Remember you only have 3 attempts to access your account.")
        else:
            print("Invalid username or password.")
    else:
        print("You cannot access your account. Too many unsuccessful attempts")
        return False

def country():
    logic= True

    while logic:
         print(locations.keys())
         country = input('Choose a country: ')
         if country in locations:
             city = locations[country]
             print(f'Cities in {country_choice}:')
             city_choice = input('CHoose a city: ')
             logic = False
         else:
             print('Choose a right country and city')
             logic= True
            
      
        
def room_type():
    logic = True

    while logic:
        print(rooms.keys())
        room_type = input('Choose a room type: ')
        if room_type in rooms:
            return room_type
        else:
            print('Invalid room type. Please choose from the available options.')


def nights():
    while True:
        try:
            num_nights = int(input('Enter the number of nights: '))
            if num_nights > 0:
                return num_nights
            else:
                print('Please enter a valid number of nights.')
        except ValueError:
            print('Please enter a valid numeric value.')
def user_data():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    id_passport = input('Enter your ID/passport: ')
    return {'name': name, 'surname': surname, 'id_passport': id_passport}

def calculate_cost(room_type, num_nights):
    return price[room_type] * num_nights

def confirm_reservation(cost):
    print(f'The total cost of your reservation is: ${cost}')
    confirm = input('Do you want to confirm the reservation? (yes/no): ')
    return confirm.lower() == 'yes'

def reservation(username, country, city, room_type, num_nights, user_info):
    cost = calculate_cost(room_type, num_nights)
    if confirm_reservation(cost):
        reservation_details = {
            'username': username,
            'country': country,
            'city': city,
            'room_type': room_type,
            'num_nights': num_nights,
            'user_info': user_info,
            'total_cost': cost
        }
        print('Reservation confirmed!')
        return reservation_details
    else:
        print('Reservation canceled.')
        

def main():
    nuevo_usuario = user()
    usuario_existente = login()

    while usuario_existente:
        print(locations.keys())
        country_choice = input('Choose a country: ')
        if country_choice in locations:
            city_choice = input(f'Choose a city in {country_choice}: ')
            if city_choice in locations[country_choice]:
                room_type_choice = room_type()
                num_nights_choice = nights()
                user_info_choice = user_data()

                reservation_details = reservation(
                    usuario_existente, country_choice, city_choice, room_type_choice, num_nights_choice, user_info_choice
                )

                if reservation_details:
                    print(reservation_details)
                    break

if __name__ == "__main__":
    main()
    



