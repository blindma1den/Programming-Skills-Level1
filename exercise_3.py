#The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:
#It must have a login and validate the data; after the third failed attempt, it should be locked.
#The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology
#Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
#There are 3 doctors for each specialty.
#The user can only book one appointment per specialist. 
# An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty.
# As a developer, you can choose the doctors' names.
#The maximum limit for appointments, in general, is 3.
#Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours.
# As a developer, you can choose the hours.
#Display available specialists.
#The user can choose their preferred specialist.
#The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

departments = {
    "General Medicine" : {
        "General Medicine Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "General Medicine Doctor 2": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "General Medicine Doctor 3": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Emergency Care": {
        "Emergency Care Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Emergency Care Doctor 2": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Emergency Care Doctor 3": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Clinical Analysys": {
        "Clinical Analysis Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Clinical Analysis Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Clinical Analysis Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Cardiology": {
        "Cardiology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Cardiology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Cardiology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Neurology": {
        "Neurology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Neurology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Neurology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Nutrition": {
        "Nutrition Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Nutrition Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Nutrition Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Phisiotherapy": {
        "Phisiotherapy Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Phisiotherapy Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Phisiotherapy Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Traumatology": {
        "Traumatology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Traumatology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Traumatology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Internal Medicine" : {
        "Internal Medicine Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Internal Medicine Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Internal Medicine Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    }
}
  
  
accounts = {
}

#creando db de citas:
appointments = {
}
  
def login(locked):
    attempts = 0
    if locked:
        print("Your account is locked. Please try again later.")
        return
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in accounts and accounts[username].verify(password) == True:
            print("Login successful!")
            break
        elif username not in accounts:
            print("Not username find in database.")
            print("Do you want to create an account?")
            decision = str(input("Enter yes or no: "))
            if decision == 'yes':
                create_account()
                break
            else:
                while attempts < 3:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    if username in accounts and accounts[username].verify(password) == True:
                        print("Login successful!")
                        break
                    else:
                        print("Invalid username or password. Please try again.")
                        attempts += 1
                else:
                    print("You have exceeded the maximum number of attempts. Your account will be locked temporarily.")
                    locked = True
                    break
        elif username in accounts and accounts[username] != password:
            print("Invalid password. Please try again.")
            attempts = 0
            while attempts < 3:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if username in accounts and accounts[username] == password:
                    print("Login successful!")
                    break
                else:
                    print("Invalid username or password. Please try again.")
                    attempts += 1
            else:
                print("You have exceeded the maximum number of attempts. Your account will be locked temporarily.")
                locked = True
                break
    return username

def create_account():
    while True:
        username = input("Enter your username: ")
        if username in accounts:
            print("Username already exists. Please choose a different username.")
        else:
            break
    password = input("Enter your password: ")
    password = set_security_password(password)
    accounts[username] = password
    appointments[username] = {}
    print("Account created successfully!")
    
def set_security_password(password):
    password = pwd_context.hash(password)
    return password
        
def verify_password(password):
    return pwd_context.verify(password, accounts[username])

def appointment(username):
    print("Welcome to the appointment booking system!")
    print("Please select a department:")
    departments_list = list(departments.keys())
    for i, department in enumerate(departments_list, start=1):
        print(f"{i}.{department}")
    
    choice = int(input("Enter the number: "))
    if choice < 1 or choice > len(departments_list):
        print("Invalid choice. Please try again.")
        return
    specialist = departments_list[choice - 1]
    
    if specialist not in appointments[username].keys():
        appointments[username][specialist] = {}
        doctor_for_specialist(specialist)
    else:
        print("You have already booked an appointment for this department.")
        print("Do you want to book an appointment for a different department?")
        decision = str(input("Enter yes or no: "))
        if decision == 'yes':
            appointment(username)
            doctor_for_specialist(specialist)
        
    
    
def doctor_for_specialist(specialist):
    print(f"Please select a doctor for {specialist} department:")
    doctor_list = list(departments[specialist].keys())
    for i, doctor in enumerate(doctor_list, start=1):
        print(f"{i}.{doctor}")
    
    choice = int(input("Enter the number: "))
    if choice < 1 or choice > len(doctor_list):
        print("Invalid choice. Please try again.")
        return
    doctor = doctor_list[choice - 1]
    
    if doctor not in appointments[username][specialist].values():
        appointments[username][specialist][doctor] = {}
        day_for_doctor(doctor, specialist)
    
    else:
        print("You have already booked an appointment for this doctor.")
        print("Do you want to book an appointment for a different doctor?")
        decision = str(input("Enter yes or no: "))
        if decision == 'yes':
            print(f"Please select a doctor for {specialist} department:")
            doctor_list = list(departments[specialist].keys())
            for i, doctor in enumerate(doctor_list, start=1):
                print(f"{i}.{doctor}")

            choice = int(input("Enter the number: "))
            doctor = doctor_list[choice - 1]
            appointments[username][specialist][doctor] = {}
            day_for_doctor(doctor,specialist)
    
def day_for_doctor(doctor,specialist):
    print(f"Please select a day for {doctor}:")
    day_list = list(departments[specialist][doctor].keys())
    for i, time_slot in enumerate(day_list, start=1):
        print(f"{i}.{time_slot}")
    
    choice = int(input("Enter the number: "))
    if choice < 1 or choice > len(day_list):
        print("Invalid choice. Please try again.")
        return
    day = day_list[choice - 1]
    appointments[username][specialist][doctor][day] = {}
    time_slot_for_day(day, doctor, specialist)
    
def time_slot_for_day(day, doctor, specialist):
    print(f"Please select a time slot for {day}:")
    time_slot_for_day = list(departments[specialist][doctor][day].keys())
    
    for i, time_slot in enumerate(time_slot_for_day, start=1):
        print(f"{i}.{time_slot}")
        
    choice = int(input("Enter the number: "))
    if choice < 1 or choice > len(time_slot_for_day):
        print("Invalid choice. Please try again.")
        return
    time = time_slot_for_day[choice - 1]
    appointments[username][specialist][doctor][day][time] = []
    hours_slot_for_time(day, doctor, specialist, time)

def hours_slot_for_time(day, doctor, specialist, time):
    print(f"Please select a time slot:")
    time_slot_list = list(departments[specialist][doctor][day][time])
    for i, hours_slot in enumerate(time_slot_list, start=1):
        print(f"{i}.{hours_slot}")
    choice = int(input("Enter the number: "))
    if choice < 1 or choice > len(time_slot_list):
        print("Invalid choice. Please try again.")
        return
    hours = time_slot_list[choice - 1]
    
    if hours not in appointments[username][specialist][doctor][day][time]:
        appointments[username][specialist][doctor][day][time] = hours
        print(f"Your appointment is scheduled for {day} at {time} at {hours} with {doctor}.")
        appointments[username]['number_of_appointments'] = appointments[username]['number_of_appointments'] + 1 
        print("Thank you for your appointment!")
    
    else:
        print("This time slot is already booked. Please choose a different time slot.")
        time_slot_for_day(day, doctor, specialist)
    
if __name__ == "__main__":
    locked = False
    username = login(locked)
    appointments[username]['number_of_appointments'] = 0
    appointment(username)
    while appointments[username]['number_of_appointments'] < 3:
        print("Do you want to make another appointment? ")
        decision = str(input("Enter yes or no: "))
        if decision == 'yes':
            appointment(username)
        else:   
            print("Thank you for using our appointment booking system!")