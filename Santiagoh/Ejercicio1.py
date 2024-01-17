import sys



players = {
             8: {"name": "Bruno Fernandes", "goals": 5, "speed": 6, "assists": 9, "pass accuracy": 10, "defensive participations": 3},
             11: {"name": "Rasmus Hojlund", "goals": 12, "speed": 8, "assists": 2, "pass accuracy": 6, "defensive participations": 2},
             5: {"name": "Harry Maguire", "goals": 1, "speed": 5, "assists": 1, "pass accuracy": 7, "defensive participations": 9},
             17: {"name": "Alejandro Garnacho", "goals": 8, "speed": 7, "assists": 8, "pass accuracy": 6, "defensive participations": 0},
             7: {"name": "Mason Mount", "goals": 2, "speed": 6, "assists": 4, "pass accuracy": 8, "defensive participations": 1}
         }


class menu:

    def select(self):
    
        print("1. Review player")
        print("2. Compare two players")
        print("3. Identify the fastest player")
        print("4. Identify the top scorer")
        print("5. Identify the player with the most assists")
        print("6. Identify the player with the highest passing accuracy")
        print("7. Identify the player with the most defensive participations")
        print("8. Exit")
    
    
    
        self.opcion = int(input(f"Enter option: "))
        return self.opcion
    

class actions(menu):

    def identify_best(self, category, players):
        best_player = max(players.values(), key=lambda x: x[category])
        print(f"The player with the highest{category} is {best_player['name']} with {best_player[category]} points")

    def review_player(self):
        
        number = int(input("Enter the jersey number: "))
        player = players.get(number)
        
        if player:
            print(f"Player: {player['name']}")
            print(f"Goals: {player['goals']}")
            print(f"Speed: {player['speed']}")
            print(f"Assists: {player['assists']}")
            print(f"Pass accuracy: {player['pass accuracy']}")
            print(f"Defensive participations: {player['defensive participations']}")
        else:
            print("Player not found")

    def compare_players(self):
        number1 = int(input("Enter the jersey number: "))
        number2 = int(input("Enter the jersey number: "))
        player1 = players.get(number1)
        player2 = players.get(number2)
        if player1 and player2:
            print(f"player 1: {player1['name']}, player 2: {player2['name']}")
            print(f"Goals: {player1['goals']} vs {player2['goals']}")
            print(f"Speed: {player1['speed']} vs {player2['speed']}")
            print(f"assists: {player1['assists']} vs {player2['assists']}")
            print(f"pass accuracy: {player1['pass accuracy']} vs {player2['pass accuracy']}")
            print(f"defensive participations: {player1['defensive participations']} vs {player2['defensive participations']}")
            
        else:
            print("players not found")

   


        



    


    def numbers(self, opcion):
        if opcion == 1:
            self.review_player()
        elif opcion == 2:
            self.compare_players()
        elif opcion == 3:
            self.identify_best("speed", players)
        elif opcion == 4:
            self.identify_best("goals", players)
        elif opcion == 5:
            self.identify_best("assists", players)
        elif opcion == 6:
            self.identify_best("pass accuracy", players)
        elif opcion == 7:
            self.identify_best("defensive participations", players)
        elif opcion == 8:
            sys.exit()
        else:
            print("Invalid option")



if __name__ == "__main__":
    menu_instance = menu()
    
    actions_instance = actions()

    while True:
        opcion = menu_instance.select()
        actions_instance.numbers(opcion)