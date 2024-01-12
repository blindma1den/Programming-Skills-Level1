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
    
        print("1. General Medicine")
        print("2. Emergency Care")
        print("3. Clinical Analysis")
        print("4. Cardiology")
        print("5. Neurology")
        print("6. Nutrition")
        print("7. Physiotherapy")
        print("8. Traumatology")
        print("9. Internal Medicine")
        print("10. Exit")
    
    
    
        self.opcion = int(input(f"Enter option: "))
        return self.opcion
    

class actions(menu):
    


    def numbers(self, opcion):
        if opcion == 1:
            print("1")
        elif opcion == 2:
            print("2")
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("5")
        elif opcion == 6:
            print("6")
        elif opcion == 7:
            print("7")
        elif opcion == 8:
            print("8")
        elif opcion == 9:
            print("opcion 9")
        elif opcion == 10:
            sys.exit()
        else:
           print("Invalid option")



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