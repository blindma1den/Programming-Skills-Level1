
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

    def __init__(self):
        print("Select the city")

    
    def spain(self):
        print("1. Madrid")
        print("2. Barcelona")
        print("3. Valencia")
    
    def france(self):
        print("1. Paris")
        print("2. Marseille")

    
    def portugal(self):
        print("1. Madeira")
        print("2. Lisbon")
        print("3. Porto")
    
    def italy(self):
        print("1. Rome")
        print("2. Milan")

    def germany(self):
        print("1. Munich")
        print("2. Berlin")





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