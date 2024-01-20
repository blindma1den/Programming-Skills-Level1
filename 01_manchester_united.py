import os
import sys

manchester_players = [
    {
        "jersey": 8,
        "name": "Bruno Fernandes",
        "goals": 5,
        "points_in_speed": 6,
        "points_in_assists": 9,
        "points_in_passing": 10,
        "defensive_involvements": 3
    },
    {
        "jersey": 11,
        "name": "Rasmus Hojlund",
        "goals": 12,
        "points_in_speed": 8,
        "points_in_assists": 2,
        "points_in_passing": 6,
        "defensive_involvements": 2
    },
    {
        "jersey": 5,
        "name": "Harry Maguire",
        "goals": 1,
        "points_in_speed": 5,
        "points_in_assists": 1,
        "points_in_passing": 7,
        "defensive_involvements": 9
    },
    {
        "jersey": 17,
        "name": "Alejandro Garnacho",
        "goals": 8,
        "points_in_speed": 7,
        "points_in_assists": 8,
        "points_in_passing": 6,
        "defensive_involvements": 0
    },
    {
        "jersey": 7,
        "name": "Mason Mount",
        "goals": 2,
        "points_in_speed": 6,
        "points_in_assists": 4,
        "points_in_passing": 8,
        "defensive_involvements": 1
    },
    ]
#print(manchester_players[0]["name"])

login_attempts = 0

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
    print()

while option != 8:
    print_menu()

    option = int(input("Choose an option: "))
    if option == 1:
        player_number = int(input("Jersey player number:"))
        show_player_review(player_number)
        input("Press ENTER to continue")
