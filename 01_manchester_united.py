import os
import sys

manchester_players = {
    'jersey_8': {
        "jersey": 8,
        "name": "Bruno Fernandes",
        "goals": 5,
        "points_in_speed": 6,
        "points_in_assists": 9,
        "points_in_passing": 10,
        "defensive_involvements": 3
    },
    'jersey_11': {
        "jersey": 11,
        "name": "Rasmus Hojlund",
        "goals": 12,
        "points_in_speed": 8,
        "points_in_assists": 2,
        "points_in_passing": 6,
        "defensive_involvements": 2
    },
    'jersey_5': {
        "jersey": 5,
        "name": "Harry Maguire",
        "goals": 1,
        "points_in_speed": 5,
        "points_in_assists": 1,
        "points_in_passing": 7,
        "defensive_involvements": 9
    },
    'jersey_17': {
        "jersey": 17,
        "name": "Alejandro Garnacho",
        "goals": 8,
        "points_in_speed": 7,
        "points_in_assists": 8,
        "points_in_passing": 6,
        "defensive_involvements": 0
    },
    'jersey_7': {
        "jersey": 7,
        "name": "Mason Mount",
        "goals": 2,
        "points_in_speed": 6,
        "points_in_assists": 4,
        "points_in_passing": 8,
        "defensive_involvements": 1
    },
}
#print(manchester_players[0]["name"])

login_attempts = 0
option = 0

def print_menu():
    os.system('clear')
    print("WELCOME TO MANCHESTER UNITED SYSTEM")
    print("===================================")
    print("1. Player Review")
    print("2. Compare two players")
    print("3. Fastest player")
    print("4. Top goal scorer")
    print("5. Player with the most assists")
    print("6. Player with highest passing accuracy")
    print("7. Player with the most defensive involvements")
    print("8. Exit")

def show_player_review(jersey):
    for key, player in manchester_players.items():
        if str(player["jersey"]) == jersey:
            print("")
            print("Player:", player["name"])
            print("Jersey:", player["jersey"])
            print("Goals:", player["goals"])
            print("Points in speed:", player["points_in_speed"])
            print("Points in assists:", player["points_in_assists"])
            print("Points in passing accuracy:", player["points_in_passing"])
            print("Defensive involvements:", player["defensive_involvements"])
            print("")
            return True
    return False

def compare_two_players(player1, player2):
    players_count = 0
    out_print = ""
    for key, player in manchester_players.items():
        if str(player["jersey"]) == player1:
            out_print += "\n"
            out_print += "PLAYER 1\n"
            out_print += "--------\n"
            out_print += "\n"
            out_print += "Player: " + player["name"] + "\n"
            out_print += "Jersey: " + str(player["jersey"]) + "\n"
            out_print += "Goals:" + str(player["goals"]) + "\n"
            out_print += "Points in speed:" + str(player["points_in_speed"]) + "\n"
            out_print += "Points in assists:" + str(player["points_in_assists"]) + "\n"
            out_print += "Points in passing accuracy:" + str(player["points_in_passing"]) + "\n"
            out_print += "Defensive involvements:" + str(player["defensive_involvements"]) + "\n"
            out_print += "\n"
            players_count += 1
        elif str(player["jersey"]) == player2:
            out_print += "\n"
            out_print += "PLAYER 2\n"
            out_print += "--------\n"
            out_print += "\n"
            out_print += "Player: " + player["name"] + "\n"
            out_print += "Jersey: " + str(player["jersey"]) + "\n"
            out_print += "Goals:" + str(player["goals"]) + "\n"
            out_print += "Points in speed:" + str(player["points_in_speed"]) + "\n"
            out_print += "Points in assists:" + str(player["points_in_assists"]) + "\n"
            out_print += "Points in passing accuracy:" + str(player["points_in_passing"]) + "\n"
            out_print += "Defensive involvements:" + str(player["defensive_involvements"]) + "\n"
            out_print += "\n"
            players_count += 1
        if players_count == 2:
            #TODO: show result in a comparation table
            print(out_print)
            return True
    return False

def find_fastest_player():
    fastest_name = ""
    points_in_speed = 0
    for key, player in manchester_players.items():
        if points_in_speed < player["points_in_speed"]:
            fastest_name = player["name"]
            points_in_speed = player["points_in_speed"]
    if points_in_speed > 0:
        print("Fastest player:", fastest_name)
        print("Points in speed:", points_in_speed)
        print("")
        return True
    return False

def find_top_goal_scorer():
    top_scorer_name = ""
    more_goals = 0
    for key, player in manchester_players.items():
        if more_goals < player["goals"]:
            top_scorer_name = player["name"]
            more_goals = player["goals"]
    if more_goals > 0:
        print("Top scorer player:", top_scorer_name)
        print("Goals:", more_goals)
        print("")
        return True
    return False

def find_player_with_most_assists():
    more_assist_name = ""
    more_assists = 0
    for key, player in manchester_players.items():
        if more_assists < player["points_in_assists"]:
            more_assist_name = player["name"]
            more_assists = player["points_in_assists"]
    if more_assists > 0:
        print("Player with the most assists:", more_assist_name)
        print("Points in assists:", more_assists)
        print("")
        return True
    return False

def find_player_highest_passing_accuracy():
    accuracy_name = ""
    accuracy = 0
    for key, player in manchester_players.items():
        if accuracy < player["points_in_passing"]:
            accuracy_name = player["name"]
            accuracy = player["points_in_passing"]
    if accuracy > 0:
        print("Player with the most accuracy:", accuracy_name)
        print("Points in assists:", accuracy)
        print("")
        return True
    return False

def find_player_most_defensive_involvements():
    print()

while option != 8:
    print_menu()

    option = int(input("Choose an option: "))
    if option == 1:
        player_number = input("Write a Jersey player number: ")
        result = show_player_review(player_number)
        if result == False:
            print("I couldn't find jersey number", player_number)
            print("Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 2:
        player1 = input("First jersey player number to compare: ")
        player2 = input("Second jersey player number to compare: ")
        result = compare_two_players(player1, player2)
        if result == False:
            print("\nI couldn't find a jersey number")
            print("Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 3:
        result = find_fastest_player()
        if result == False:
            print("\nUnknown error. Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 4:
        result = find_top_goal_scorer()
        if result == False:
            print("\nUnknown error. Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 5:
        result = find_player_with_most_assists()
        if result == False:
            print("\nUnknown error. Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 6:
        result = find_player_highest_passing_accuracy()
        if result == False:
            print("\nUnknown error. Please try again.")
            print("")
        input("Press ENTER to continue")
    elif option == 7:
        find_player_most_defensive_involvements()
        input("Press ENTER to continue")

print("Glory glory Man United!! See your soon!")
