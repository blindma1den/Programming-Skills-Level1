from login import login


'''The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

Login; it should be locked after the third failed attempt.
The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.'''

rooms={"single":3, "vip":6, "double":6, "group":6, "luxury":3}

hotels={
    "Spain":{"Madrid":rooms, "Barcelona":rooms, "Valencia": rooms},
    "France":{"Paris":rooms,"Marseille":rooms},
    "Portugal":{"Lisbon":rooms, "Madeira":rooms, "Porto":rooms},
    "Italy":{"Rome":rooms, "Milan":rooms},
    "Germany":{"Munich":rooms, "Berlin":rooms}}

def isavailable(country:str, city:str, room:str)->bool:
    return hotels[country][city][room]>0

def reservation(country:str, city:str, room:str)->bool:
        if isavailable(country, city, room):
            hotels[country][city][room]-=1
            return True

        return False
    
    

def main():
    username=input("Please insert your username. ")
    password=input("Please insert your password. ")
    control="y"
    if login(username,password):
        while control=="y":
            country=input(f"type the country of your preference {list(hotels.keys())}").capitalize()
            city=input(f"type the city of your preference {list(hotels[country].keys())}").capitalize()
            room=input(f"type the room of your preference{list(hotels[country][city].keys())}")

            if reservation(country, city, room):
                print("Success!")
            else: 
                print("Sorry")
            control=input("Do you want to continue? y/n").lower()
    

if __name__ == "__main__":
    main()