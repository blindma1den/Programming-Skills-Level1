'''Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their 
fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
The system should also allow comparison between two players. Use the following player profiles:

Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive 
involvements. Corresponds to jersey number 8.
Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive 
involvements. Corresponds to jersey number 11.
Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive 
involvements. Corresponds to jersey number 5.
Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive
 involvements. Corresponds to jersey number 17.
Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive 
involvement. Corresponds to jersey number 7.
The program functions as follows: The coach accesses the system and encounters a menu with the following 
options:
Player Review: By entering the player's jersey number, they can access the player's characteristics.
Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
Identify the fastest player: Displays the player with the most points in speed.
Identify the top goal scorer: Displays the player with the most points in goals.
Identify the player with the most assists: Displays the player with the most points in assists.
Identify the player with the highest passing accuracy: Displays the player with the most points in passing 
accuracy.
Identify the player with the most defensive involvements: Displays the player with the most points in 
defensive involvements.
The system should also allow returning to the main menu.
'''

class Player:
    
    def __init__(self,name:str,goals:int, speed:int, assists:int, passaccuracy:int, defense:int) -> None:
        self.name=name
        self.goals=goals
        self.speed=speed
        self.assists=assists
        self.passaccuracy=passaccuracy
        self.defense=defense

    def __repr__(self) -> str:
        return f"name: {self.name}\n goals: {self.goals}\nspeed: {self.speed}\nassists: {self.assists}\npass accuracy: {self.passaccuracy}\ndefense: {self.defense}\n"
            

players = {
        8:Player("Bruno Fernandes", 5, 6, 9, 10, 3), 11:Player("Rasmus Hojlund", 12, 8, 2, 6, 2),
        5:Player("Harry Maguire", 1, 5, 1, 7, 9), 17:Player("Alejandro Garnacho", 8, 7, 8, 6, 0), 
        7:Player("Mason Mount", 2, 6, 4, 8, 1)
    }
def search_player(number:int)->bool:
    return True if number in players.keys() else False
def player_review(number:int)->Player:
    return players[number] if search_player(number) else "The player isn't listed or doesn't exist"

def comparison(player1:int,player2:int)->Player:
    if search_player(player1) and search_player(player2):return players[player1], players[player2]
    else: return print("The player isn't listed or doesn't exist")
    
def top_player_by(stat:str):
    if stat in ["goals", "speed", "assists", "passaccuracy", "defense"]:
        return max(players.values(), key=lambda item: getattr(item, stat))
    else: 
        print("Try again, maybe you had a Typo.")
        return top_player_by(stat)
    
def main():
    choice = int(input("choose between the following options:\n1. Player review.\n2. Compare two players of your choice.\n3. The top player by a stat of your choice.\n4. Exit.\n"))
    control = "y"
    def return_to_menu(control):
        control=input("do you want to return to the main menu? y/n")
        if control =="y":
                return main()
        else: print("Thank you for using the player system. Good bye!")

    match(choice):
        case 1:
            number = int(input("Type the player's number."))
            print(player_review(number))
            return_to_menu(control)
            
        case 2:
            player1= int(input("Type the first player's number."))
            player2= int(input("Type the second player's number."))
            print(comparison(player1,player2))
            return_to_menu(control)
        case 3:
            stat=input("Type the stat you want to review:\ngoals, speed, assists, passaccuracy, defense")
            print(top_player_by(stat))
            return_to_menu(control)
        case 4:
            print("Thank you for using the player system. Good bye!")
        case _: 
            print("incorrect option.")
            main()
if __name__ == "__main__":
    main()