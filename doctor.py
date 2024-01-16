'''

3. 

The Valencia Hospital is developing an application to manage appointments.
Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt,
it should be locked.

The user can schedule an appointment for: General Medicine, Emergency Care,
Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.

The user can only book one appointment per specialist.
An error message should be displayed if the user tries to choose two
appointments with the same doctor or the same specialty. As a developer,
you can choose the doctors' names.

The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a
morning or afternoon appointment and show available hours. As a developer,
you can choose the hours.

Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor ->
Choose timeslot.

'''



users= {}
specialities = {'General Medicine': ['García', 'Martinez', 'Segovia'], 'Emergency Care': ['Marquez', 'Rodriguez', 'Vega'],'Clinical Analysis': ['García', 'Vega', 'Segovia'],
                'Cardiology': ['Rodriguez', 'Marquez', 'Fernandez'], 'Neurology': ['Ibañez', 'Hagen', 'Pinilla'], 'Nutrition': ['Castañ', 'Barbosa', 'Carrión'],
                'Physiotherapy': ['Ross', 'Herrera', 'Aparicio'], 'Traumatology': ['Lopez', 'Lamarca', 'Sevilla'], 'Internal Medicine': ['Ross', 'Hagen', 'Barbosa']}
hours = {'morning': ['7h', '8h', '10h'], 'afternoon': ['15h', '16h', '17h']}
appointments = {}


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
        return False, None


def appointment():
    nuevo_usuario = user()
    usuario_existente = login()

    logic = True

    while logic:
        if usuario_existente:
            print(specialities.keys())
            choose = input('What is the appointment for? ')
            if choose in specialities:
                doctors = specialities[choose]
                print(f' Doctors available for {choose}: {doctors}')

                doctor_choice= input('Who do you want to book the appointment with? ')

                logic2 = True

                while logic2:
                    if doctor_choice in doctors:
                        print(f'Choose an hour: {hours}')
                        time = input('Write the hour here: ')

                        if time in hours['morning'] or time in hours['afternoon']:
                            whole_appointment = f'{choose}_{doctor_choice}_{time}'
                            if whole_appointment not in appointments:
                                appointments[whole_appointment] = usuario_existente
                                print(f'Appointment booked successfully with {doctor_choice} for {choose} at {time} time.')
                                logic = False
                                logic2 = False
                            else:
                                print('You already have an appointment at this time. Please choose another time.')
                                logic2 = True
                        else:
                            print('Invalid time choice. Please choose from the available hours.')
                            logic2 = True
                    else:
                        print('Invalid doctor choice. Please choose a doctor from the available options.')
                        logic2 = True
            else:
                print('Invalid specialty choice. Please choose a specialty from the available options.')
                logic = True


if __name__ == "__main__":
    appointment()
                        
                
        
    

              
    
