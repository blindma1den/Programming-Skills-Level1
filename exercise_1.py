#1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, 
#assists, passing accuracy, and defensive involvements.
#The system should also allow comparison between two players. Use the following player profiles:
#
#Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
#Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
#Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
#Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
#Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
#The program functions as follows: The coach accesses the system and encounters a menu with the following options:
#
#Player Review: By entering the player's jersey number, they can access the player's characteristics.
#Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
#Identify the fastest player: Displays the player with the most points in speed.
#Identify the top goal scorer: Displays the player with the most points in goals.
#Identify the player with the most assists: Displays the player with the most points in assists.
#Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
#Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
#The system should also allow returning to the main menu.

#building data dictionari

profiles = {
    8: {
        'name': 'Bruno Fernandes',
        'goals': 5,
        'speed': 6,
        'assists': 9,
        'passing accuracy': 10,
        'defensive involvements': 3
    },
    11: {
        'name': 'Rasmus Hojlund',
        'goals': 12,
        'speed': 8,
        'assists': 2,
        'passing accuracy': 6,
        'defensive involvements': 2
    },
    5: {
        'name': 'Harry Maguire',
        'goals': 1,
        'speed': 5,
        'assists': 1,
        'passing accuracy': 7,
        'defensive involvements': 9
    },
    17: {
        'name': 'Alejandro Garnacho',
        'goals': 8,
        'speed': 7,
        'assists': 8,
        'passing accuracy': 6,
        'defensive involvements': 0
    },
    7: {
        'name': 'Mason Mount',
        'goals': 2,
        'speed': 6,
        'assists': 4,
        'passing accuracy': 8,
        'defensive involvements': 1
    }
}

#function to display the menu
def display_menu():
    print("Welcome to the Manchester United FC player review system.")
    print("Please select an option:")
    print("1. Player Review")
    print("2. Compare two players")
    print("3. Identify the fastest player")
    print("4. Identify the top goal scorer")
    print("5. Identify the player with the most assists")
    print("6. Identify the player with the highest passing accuracy")
    print("7. Identify the player with the most defensive involvements")
    print("8. Return to the main menu")

while True:
    display_menu()
    option = input("Enter your option: ")

    if option == "1":
        #Player Review
        jersey_number = int(input("Enter the player's jersey number: "))
        player_profile = profiles.get(jersey_number)
        if player_profile:
            print("**********************************************************************")
            print("Player Profile:")
            print("Name:", player_profile['name'])
            print("Goals:", player_profile['goals'])
            print("Speed:", player_profile['speed'])
            print("Assists:", player_profile['assists'])
            print("Passing Accuracy:", player_profile['passing accuracy'])
            print("Defensive Involvements:", player_profile['defensive involvements'])
            print("**********************************************************************")
        else:
            print("Player not found.")
    elif option == "2":
        #Compare two players
        jersey_number1 = int(input("Enter the first player's jersey number: "))
        player_profile1 = profiles.get(jersey_number1)
        jersey_number2 = int(input("Enter the second player's jersey number: "))
        player_profile2 = profiles.get(jersey_number2)
        if player_profile1 and player_profile2:
            print("**********************************************************************")
            print("Player Profile 1:")
            print("Name:", player_profile1['name'])
            print("Goals:", player_profile1['goals'])
            print("Speed:", player_profile1['speed'])
            print("Assists:", player_profile1['assists'])
            print("Passing Accuracy:", player_profile1['passing accuracy'])
            print("Defensive Involvements:", player_profile1['defensive involvements'])
            print("Player Profile 2:")
            print("Name:", player_profile2['name'])
            print("Goals:", player_profile2['goals'])
            print("Speed:", player_profile2['speed'])
            print("Assists:", player_profile2['assists'])
            print("Passing Accuracy:", player_profile2['passing accuracy'])
            print("Defensive Involvements:", player_profile2['defensive involvements'])
            print("**********************************************************************")
        else:
            print("One or both players not found.")
    elif option == "3":
        #Identify the fastest player
        fastest_player = max(profiles, key=lambda x: profiles[x]['speed'])
        print("**********************************************************************")
        print("The fastest player is", profiles[fastest_player]['name'], "with", profiles[fastest_player]['speed'], "points in speed.")
        print("**********************************************************************")
    elif option == "4":
        #Identify the top goal scorer
        top_scorer = max(profiles, key=lambda x: profiles[x]['goals'])
        print("**********************************************************************")
        print("The top goal scorer is", profiles[top_scorer]['name'], "with", profiles[top_scorer]['goals'], "goals.")
        print("**********************************************************************")
    elif option == "5":
        #Identify the player with the most assists
        most_assists = max(profiles, key=lambda x: profiles[x]['assists'])
        print("**********************************************************************")
        print("The player with the most assists is", profiles[most_assists]['name'], "with", profiles[most_assists]['assists'], "assists.")
        print("**********************************************************************")
    elif option == "6":
        #Identify the player with the highest passing accuracy
        highest_passing_accuracy = max(profiles, key=lambda x: profiles[x]['passing accuracy'])
        print("**********************************************************************")
        print("The player with the highest passing accuracy is", profiles[highest_passing_accuracy]['name'], "with a passing accuracy of", profiles[highest_passing_accuracy]['passing accuracy'], "points.")
        print("**********************************************************************")
    elif option == "7":
        #Identify the player with the most defensive involvements
        most_defensive_involvements = max(profiles, key=lambda x: profiles[x]['defensive involvements'])
        print("**********************************************************************")
        print("The player with the most defensive involvements is", profiles[most_defensive_involvements]['name'], "with", profiles[most_defensive_involvements]['defensive involvements'], "defensive involvements.")
        print("**********************************************************************")
    else:
        print("Invalid option. Please try again.")
        
        
