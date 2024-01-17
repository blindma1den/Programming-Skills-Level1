class User:
    budget:int
    reservation:list
    def __init__(self, name:str, id:int, password:str, passport:int, budget=600,reservation=[]) -> None:
        self.name = name
        self.id = id
        self.password = password
        self.passport = passport
        self.budget =budget
        self.reservation=reservation

users=[User(name="Mayber", id=1126785, password="pass", passport=122345, reservation=[]), 
       User(name="Tony", id=34657212, password="reto1", passport=126345, reservation=[])]

def search_user(userid:int)->User | bool:
    '''
    hace una búsqueda del usuario en las credenciales almacenadas si el usuario existe.
    
    :param: userid:str - ID proporcionado por el usuario.
    :return: object or error - objeto resultante contiene datos del usuario.

    '''
    user= filter(lambda user: user.id == userid, users)
    try:
        return list(user)[0]
    except:
        return False
    
def isvalid(userid:int, password:str)->bool:
    '''
    valida que las credenciales pertenezcan al usuario.

    :param: userid, password: str - ID y Password proporcionados por el usuario.
    :return: bool - son correctas ambas credenciales?
    '''
    user= search_user(userid)
    if not user: return False
    if userid == user.userid and password == user.password: return True 

def login(userid:str, password:str):
    for i in range(3):
        if i == 3:
            print("You're blocked.")
            break
        elif isvalid(userid, password):
            print("logged in successfully")
            break
        else:
            print(f"you have {i} tries left")