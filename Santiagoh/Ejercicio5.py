import sys
import datetime

class Account:    
    def __init__(self):
        self.user = "a"
        self.password = "1"
        self.user_data = {}

class Login(Account):
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

    def collect_user_data(self):
        self.user_data['origin country'] = input("Enter your origin country(Turkey, Greece, Lebanon, Spain, and Portugal. ): ")
        self.user_data['destination country'] = input("Enter your destination country(Turkey, Greece, Lebanon, Spain, and Portugal. ): ")
        while True:
            flight_date = input("Enter your flight date (dd/mm/aa): ")
            try:
                datetime.datetime.strptime(flight_date, '%d/%m/%y')
                self.user_data['flight_date'] = flight_date
                break
            except ValueError:
                print("Incorrect date format, should be dd/mm/aa")

        self.user_data['class'] = input("Enter your class (Economy or First Class): ")
        self.user_data['additional_luggage'] = input("Do you want to check an additional piece of luggage into the hold? (yes/no): ")
        self.user_data['meal'] = input("Choose your preferred meal (Regular, Vegetarian, Kosher): ")

    def display_reservation(self):
        print("Your reservation details are as follows:")
        for key, value in self.user_data.items():
            print(f"{key}: {value}")

    def confirm_reservation(self):
        confirmation = input("Do you want to confirm the reservation? (yes/no): ")
        if confirmation.lower() == 'yes':
            print("Your reservation has been confirmed.")
        else:
            print("Your reservation has been cancelled.")
            sys.exit()

if __name__ == "__main__":
    login_instance = Login()

    logging = False
    while not logging:
        input_user = input("Enter your username: ")
        input_password = input("Enter your password: ")
        logging = login_instance.verify_user(input_user, input_password)

    login_instance.collect_user_data()
    login_instance.display_reservation()
    login_instance.confirm_reservation()

