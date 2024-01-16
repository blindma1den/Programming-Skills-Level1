'''
5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked.
The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
The user must choose if they want to check an additional piece of luggage into the hold.
Hand luggage is free of charge.
The user must purchase both the outbound and return tickets.
The user can choose their preferred meal: Regular, Vegetarian, Kosher.
The program must collect the following data: Name, country of origin, passport, and destination country.
Upon completing the process, the system will display everything the user has previously chosen along with their information. 
The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.

'''




users = {}
countries = ['Turkey', 'Greece', 'Lebanon', 'Spain', 'Portugal']
classes = ['Economy', 'First Class']
meals = ['Regular', 'Vegetarian', 'Kosher']

def user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if username not in users: 
        users[username] = {'password': password} 
        print("Registered successfully.")
    else:
        print("Username already exists. Please choose a different username.")

def login():
    attempts = 0
    while attempts < 3:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
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
        return False, None

def book_flight():
    user_data = {}
    user_exist = login()

    if user_exist:
        print("Available countries:", countries)
        origin_country = input("Choose your origin country: ")
        destination_country = input("Choose your destination country: ")

        if origin_country in countries and destination_country in countries:
            user_data['Origin Country'] = origin_country
            user_data['Destination Country'] = destination_country

            flight_date = input("Enter the flight date: ")
            user_data['Flight Date'] = flight_date

            print("Available classes:", classes)
            travel_class = input("Choose your travel class (Economy/First Class): ")
            if travel_class in classes:
                user_data['Travel Class'] = travel_class

                luggage_choice = input("Do you want to check an additional piece of luggage? (Yes/No): ")
                user_data['Additional Luggage'] = luggage_choice.lower() == 'yes'

                print("Available meals:", meals)
                meal_choice = input("Choose your preferred meal: ")
                if meal_choice in meals:
                    user_data['Meal Choice'] = meal_choice

                    user_data['Name'] = input("Enter your name: ")
                    user_data['Country of Origin'] = input("Enter your country of origin: ")
                    user_data['Passport'] = input("Enter your passport number: ")

                    print("\nSummary of your choices:")
                    for key, value in user_data.items():
                        print(f"{key}: {value}")

                    confirm = input("Do you want to confirm the reservation? (Yes/No): ")
                    if confirm.lower() == 'yes':
                        print("Reservation confirmed. Thank you for choosing Turkish Airlines!")
                    else:
                        print("Reservation canceled. Returning to the main menu.")
                else:
                    print("Invalid meal choice. Returning to the main menu.")
            else:
                print("Invalid travel class. Returning to the main menu.")
        else:
            print("Invalid origin or destination country. Returning to the main menu.")
if __name__ == "__main__":
    book_flight()
    
