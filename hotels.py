'''The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

Login; it should be locked after the third failed attempt.
The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.'''
from login import login, users

class Hotel:
    class Room:
        room_type:str
        price:int
        available:int
        def __init__(self, room_type, price, available) -> None:
            self.room_type=room_type
            self.price=price
            self.available=available
        def __str__(self) -> str:
            return f"room type: {self.room_type}, price: {self.price}, available: {self.available}"
    rooms = [Room("single", 100, 3), Room("double", 200, 6), Room("group", 350, 6), Room("vip", 450, 6), Room("luxury", 550, 3)]

    def __init__(self, country, city) -> None:
        self.country=country
        self.city=city
        self.rooms
    
    def __str__(self) -> str:
        return f"country: {self.country}, city: {self.city}, rooms: {[str(room) for room in self.rooms]}" 
    def reservation(self, country, city ):
        pass

hotels =[Hotel("Spain", "Madrid"),Hotel("Spain", "Barcelona"), Hotel("Spain", "Valencia"),]


def search_room(country:str, city:str)->Hotel | bool:
    '''
    hace una búsqueda del usuario en las credenciales almacenadas si el usuario existe.
    
    :param: country:str - ID proporcionado por el usuario.
    :return: object or error - objeto resultante contiene datos del usuario.

    ''' 
    try:
        hotel= filter(lambda hotel: hotel.country== country and hotel.city ==city, hotels)
        return list(hotel)[0]
    except:
        return False
    
def isvalid(country:str, city:str)->bool:
    '''
    valida que las credenciales pertenezcan al usuario.

    :param: country, password: str - ID y Password proporcionados por el usuario.
    :return: bool - son correctas ambas credenciales?
    '''
    hotel= search_room(country)
    if not hotel: return False
    if country == hotel.country and city == hotel.city: return True
def reservations(country,city, room_type):
    pass

def booking():
    pass
def main():
    pass

if __name__ == "__main__":
    print(search_room("Spain", "Madrid"))