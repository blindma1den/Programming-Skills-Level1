'''Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked. -> listo
The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
The user must choose if they want to check an additional piece of luggage into the hold. -> listo.
Hand luggage is free of charge.
The user must purchase both the outbound and return tickets.
The user can choose their preferred meal: Regular, Vegetarian, Kosher. ->listo.
The program must collect the following data: Name, country of origin, passport, and destination country. -> listo
Upon completing the process, the system will display everything the user has previously chosen along with their information. -> listo
The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.'''
from login import login

meals = {1:"Regular", 2:"Vegetarian", 3: "Kosher"}
destination = ["Turkey", "Greece", "Lebanon", "Spain", "Portugal"]
flight_schedule = {1:"monday 22/02",2:"friday 25/02",3:"thursday 04/03",4:"wednesday 10/03",5:"saturday 13/03", 6:"monday 15/03"}
logs={}
def purchase():
    pass

def userdata(name:str, origin:str, destination:str, passport:int, flight_class: str, outbound_date:str, return_date:str, additional:bool):
    user_data={"Name":name, "Country of Origin": origin, "Destination":destination, "Passport": passport}
    flight_data={"class": flight_class, "luggage": "hand | additional: "+additional, "flight date": ["outbound: "+outbound_date, "return: "+return_date]}

    return f"Your data: {user_data}, your flight information: {flight_data}"

def main():
    username=input("Please insert your username. ")
    password=input("Please insert your password. ")
    if login(username, password):
        name=input("insert your Name")
        passport=input("insert your passport")
        origin = input("type country of origin ")
        destination=input(f"choose your destination {destination} ")
        outbound_date=input(f"choose outbound date: {flight_schedule}")
        return_date=input("choose return date: ")
        flight_class=input("choose the class: ")
        additional=input("do you want to carry aditional luggage? y/n").upper()
        details=userdata(name, origin, destination, passport, flight_class, outbound_date, return_date, additional)
        print(details)

        purchase= input("do you want to confirm this transaction? y/n").lower()
        if purchase == 'y':
            logs[username]=details
            print(logs)
        else: print("thank you, come again!")

main()

    