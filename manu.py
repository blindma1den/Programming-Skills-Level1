# Manchester United FC
while True:

    items = str("Player     Goals  Points in speed  Point in assists  Points in passing accuracy  Defensive involvements")
    Maguire = str("Maguire     1            5              1                      7                     9")
    Mount = str("Mount         2            6              4                      8                     1")
    Fernandes = str("Fernandes    5            6              9                      10                    3")
    Hojlund = str("Hojlund      12            8              2                      6                    2")
    Garnacho = str("Garnacho     8            7              8                      6                    0")

    players = {
    Maguire, Mount, Fernandes, Hojlund, Garnacho
    }

    speed = {
    'Maguire': int(Maguire.split()[2]),
    'Mount': int(Mount.split()[2]),
    'Fernandes': int(Fernandes.split()[2]),
    'Hojlund': int(Hojlund.split()[2]),
    'Garnacho': int(Garnacho.split()[2])
    }
    def fastest_player(speed):
        fastest = max(speed, key=speed.get)
        print(f"The fastest player is {fastest} with {speed[fastest]} points in speed.")

    goals = {
    'Maguire': int(Maguire.split()[1]),
    'Mount': int(Mount.split()[1]),
    'Fernandes': int(Fernandes.split()[1]),
    'Hojlund': int(Hojlund.split()[1]),
    'Garnacho': int(Garnacho.split()[1])
    }
    def scorer_player(goals):
        scorer = max(goals, key=goals.get)
        print(f"The scorer player is {scorer} with {goals[scorer]} goals.")

    assists = {
    'Maguire': int(Maguire.split()[3]),
    'Mount': int(Mount.split()[3]),
    'Fernandes': int(Fernandes.split()[3]),
    'Hojlund': int(Hojlund.split()[3]),
    'Garnacho': int(Garnacho.split()[3])
    }
    def assistant_player(assists):
        assistant = max(assists, key=assists.get)
        print(f"The most assistant player is {assistant} with {assists[assistant]} assists.")
   
    accuracy = {
    'Maguire': int(Maguire.split()[4]),
    'Mount': int(Mount.split()[4]),
    'Fernandes': int(Fernandes.split()[4]),
    'Hojlund': int(Hojlund.split()[4]),
    'Garnacho': int(Garnacho.split()[4])
    }
    def accurate_player(accuracy):
        accurate = max(accuracy, key=accuracy.get)
        print(f"The most accurate player is {accurate} with {accuracy[accurate]} points in passing accuracy.")

    defense = {
    'Maguire': int(Maguire.split()[5]),
    'Mount': int(Mount.split()[5]),
    'Fernandes': int(Fernandes.split()[5]),
    'Hojlund': int(Hojlund.split()[5]),
    'Garnacho': int(Garnacho.split()[5])
    }
    def defensive_player(defense):
        defensive = max(defense, key=defense.get)
        print(f"The most assistant player is {defensive} with {defense[defensive]} points in defensive involvements.")

    print("Welcome to Manchester United System")
    print("What would you like to do?")
    print("1. Player Review")
    print("2. Compare two players")
    print("3. Identify the fastest player")
    print("4. Identify the top goal scorer")
    print("5. Identify the player with the most assists")
    print("6. Identify the player with the highest passing accuracy")
    print("7. Identify the player with the most defensive involvements")
    option = input("Enter an option: ")

    if option == "1":
        print("1. Player Review: ")
        nplayer = input("Enter the player's jersey number: ")
        
        if nplayer == "5":
            print("Harry Maguire. Jersey number 5")
            print(items)
            print(Maguire)
        elif nplayer == "7":
            print("Mason Mount. Jersey number 7")
            print(items)
            print(Mount)
        elif nplayer == "8":
            print("Bruno Fernandes. Jersey number 8")
            print(items)
            print(Fernandes)
        elif nplayer == "11":
            print("Rasmus Hojlund. Jersey number 11")
            print(items)
            print(Hojlund)
        elif nplayer == "17":
            print("Alejandro Garnacho. Jersey number 17")
            print(items)
            print(Garnacho)
        else: 
            print("Jersey number not found. Try again")
            
        continuar = input('Do you want to return to the main menu? Y / N :')

        if continuar.lower() in ["no", "n"]:
            break

    if option == "2":
        print("2. Compare two players: ")
        nplayer = input("Enter the first player's jersey number: ")
        nplayer2 = input("Enter the second player's jersey number: ")
        if nplayer == "5":
            nameplayer = Maguire
        elif nplayer == "7":
            nameplayer = Mount
        elif nplayer == "8":
            nameplayer = Fernandes
        elif nplayer == "11":
            nameplayer = Hojlund
        elif nplayer == "17":
            nameplayer = Garnacho
        else:
            nameplayer = "First player's jersey number not found"
            
        if nplayer2 == "5":
            nameplayer2 = Maguire
        
        elif nplayer2 == "7":
            nameplayer2 = Mount
        elif nplayer2 == "8":
            nameplayer2 = Fernandes
        elif nplayer2 == "11":
            nameplayer2 = Hojlund
        elif nplayer2 == "17":
            nameplayer2 = Garnacho 
        else:
            nameplayer2 = "Second player's jersey number not found"
        
        print(items)
        print(nameplayer)
        print(nameplayer2)  
                
        continuar = input('Do you want to return to the main menu? Y / N :')

        if continuar.lower() in ["no", "n"]:
            break

    if option == "3":
        print("3. Identify the fastest player: ")
        fastest_player(speed)
    
    if option == "4":
        print("4. Identify the top goal scorer: ")
        scorer_player(goals)
    
    if option == "5":
        print("5. Identify the player with the most assists: ")
        assistant_player(assists)

    if option == "6":
        print("6. Identify the player with the highest passing accuracy: ")
        accurate_player(accuracy)

    if option == "7":
        print("7. Identify the player with the most defensive involvements: ")
        defensive_player(defense)