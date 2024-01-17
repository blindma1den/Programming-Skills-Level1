import sys

class account:    
    def __init__(self):
        self.user = "a"
        self.password = "1"


class login(account):
    def __init__(self):
        super().__init__()
        self.failed_attempts = 0
    
    def verify_user(self, input_user, input_password):
        if input_user == self.user and input_password == self.password:
            print("Successful Login!!")

            return True
            
        else:
            print("Incorrect Password!")
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                print("error number 3. The program will close")
                sys.exit()
            return False
        


class menu(account):
    def select(self):
        
        print("Select the country")
        print("1. Spain")
        print("2. France")
        print("3. Portugal")
        print("4. Italy")
        print("5. Germany")
        print("6. Exit")
    
    
    
        self.opcion = int(input(f"Enter option number: "))
        return self.opcion
    

class actions(menu):
    


    def numbers(self, opcion):
        if opcion == 1:
            country = countries()
            country.spain()
        elif opcion == 2:
            country = countries()
            country.france()
        elif opcion == 3:
            country = countries()
            country.portugal()
        elif opcion == 4:
            country = countries()
            country.italy()
        elif opcion == 5:
            country = countries()
            country.germany()
        elif opcion == 6:
            sys.exit()
        else:
           print("Invalid option")


class countries(actions):
    
    precios = {
        'VIP': 450,
        'single': 100,
        'double': 200,
        'group': 350,
        'suites': 550
    }

    hoteles = {
    'Spain': {
        'Madrid': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Barcelona': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Valencia': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3}
    },
    'France': {
        'Paris': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Marseille': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3}
    },
    'Portugal': {
        'Madeira': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Lisbon': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Porto': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3}
    },
    'Italy': {
        'Rome': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Milan': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3}
    },
    'Germany': {
        'Munich': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3},
        'Berlin': {'VIP': 6, 'single': 3, 'double': 6, 'group': 6, 'suites': 3}
    }
}

    def __init__(self):
        print("Select the city")

    
    def spain(self):
        print("1. Madrid")
        print("2. Barcelona")
        print("3. Valencia")
        city = input("Enter option: ")
        room_type = input("select room (VIP, single, double, group, suites): ")
        country = "Spain"
        if self.hoteles[country][city][room_type] > 0:
            self.hoteles[country][city][room_type] -= 1
            print(f"Room {room_type} booked successfully in {city}, {country}.")
            num_nights = int(input("Enter number of nights: "))
            total_price = self.precios[room_type]*num_nights
            print(f"The total price is ${total_price}.")
            ticket = user()
            ticket.confirm_reservation(total_price)
        else:
            print("Sorry, no rooms of that type are available.")


        
    
    def france(self):
        print("1. Paris")
        print("2. Marseille")
        city = input("Enter option: ")
        room_type = input("select room (VIP, single, double, group, suites): ")
        country = "France"
        if self.hoteles[country][city][room_type] > 0:
            self.hoteles[country][city][room_type] -= 1
            print(f"Room {room_type} booked successfully in {city}, {country}.")
            num_nights = int(input("Enter number of nights: "))
            total_price = self.precios[room_type]*num_nights
            print(f"The total price is ${total_price}.")
            ticket = user()
            ticket.confirm_reservation(total_price)

        else:
            print("Sorry, no rooms of that type are available.")

    
    def portugal(self):
        print("1. Madeira")
        print("2. Lisbon")
        print("3. Porto")
        city = input("Enter option: ")
        room_type = input("select room (VIP, single, double, group, suites): ")
        country = "Portugal"
        if self.hoteles[country][city][room_type] > 0:
            self.hoteles[country][city][room_type] -= 1
            print(f"Room {room_type} booked successfully in {city}, {country}.")
            num_nights = int(input("Enter number of nights: "))
            total_price = self.precios[room_type]*num_nights
            print(f"The total price is ${total_price}.")
            ticket = user()
            ticket.confirm_reservation(total_price)
        else:
            print("Sorry, no rooms of that type are available.")
    
    def italy(self):
        print("1. Rome")
        print("2. Milan")
        city = input("Enter option: ")
        room_type = input("select room (VIP, single, double, group, suites): ")
        country = "Italy"
        if self.hoteles[country][city][room_type] > 0:
            self.hoteles[country][city][room_type] -= 1
            print(f"Room {room_type} booked successfully in {city}, {country}.")
            num_nights = int(input("Enter number of nights: "))
            total_price = self.precios[room_type]*num_nights
            print(f"The total price is ${total_price}.")
            ticket = user()
            ticket.confirm_reservation(total_price)
        else:
            print("Sorry, no rooms of that type are available.")

    def germany(self):
        print("1. Munich")
        print("2. Berlin")
        city = input("Enter option: ")
        room_type = input("select room (VIP, single, double, group, suites): ")
        country = "Germany"
        if self.hoteles[country][city][room_type] > 0:
            self.hoteles[country][city][room_type] -= 1
            print(f"Room {room_type} booked successfully in {city}, {country}.")
            num_nights = int(input("Enter number of nights: "))
            total_price = self.precios[room_type]*num_nights
            print(f"The total price is ${total_price}.")
            ticket = user()
            ticket.confirm_reservation(total_price)
        else:
            print("Sorry, no rooms of that type are available.")

class user(countries):
    def __init__(self):

        self.name = input("Enter your name: ")
        self.lastname = input("Enter your last name: ")
        self.id = input("Enter your ID/passport: ")

    def confirm_reservation(self, total_price):
        print(f"The total cost is ${total_price}.")
        confirmation = input("Do you agree with the total cost? (yes/no): ")
        if confirmation.lower() == 'yes':
            print("Reservation confirmed. Thank you for choosing RH Hotels.")
            print("Returning to the main menu.")
            print("-------------------------------------------------------------------------------")
        else:
            print("Reservation not confirmed. Returning to the main menu.")
            print("-------------------------------------------------------------------------------")


if __name__ == "__main__":
    login_instance = login()

    logging = False
    while not logging:
        input_user = input("Enter your username: ")
        input_password = input("Enter your password: ")
        logging = login_instance.verify_user(input_user, input_password)

    menu_instance = menu()
    
    actions_instance = actions()
    while True:
        opcion = menu_instance.select()
        actions_instance.numbers(opcion)



