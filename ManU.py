'''

1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists,
passing accuracy, and defensive involvements.
The system should also allow comparison between two players. Use the following player profiles:

Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
The program functions as follows: The coach accesses the system and encounters a menu with the following options:

Player Review: By entering the player's jersey number, they can access the player's characteristics.
Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
Identify the fastest player: Displays the player with the most points in speed.
Identify the top goal scorer: Displays the player with the most points in goals.
Identify the player with the most assists: Displays the player with the most points in assists.
Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
The system should also allow returning to the main menu.

'''


players = {'Bruno_Fernandes': [5,6,9,10,3], 'Rasmus_Hojlund': [12,8,2,6,2], 'Harry_Maguire': [1,5,1,7,9],
           'Alejandro_Garnacho':[8,7,8,6,0] ,'Mason_Mount': [2,6,4,8,1]}


def display_player(player_name):
    print(f'{player_name}')
    print(f'Goals: {players[player_name][0]}')
    print(f'Speed: {players[player_name][1]}')
    print(f'Assists: {players[player_name][2]}')
    print(f'Passing Accuracy: {players[player_name][3]}')
    print(f'Defensive involvements: {players[player_name][4]}')


def player_review():
    print('These are the jersey numbers of your favorite players:')
    print('Bruno Fernandes: 8')
    print('Rasmus Hojlund: 11')
    print('Harry Maguire: 5')
    print('Alejandro Garnacho: 17')
    print('Mason Mount: 7')

    while True:
        choice = input('Insert the jersey number of the player you want to check (or "exit" to return): ')
        if choice.lower() == 'exit':
            break
        player_name = None
        if choice == '8':
            player_name = 'Bruno_Fernandes'
        elif choice == '11':
            player_name = 'Rasmus_Hojlund'
        elif choice == '5':
            player_name = 'Harry_Maguire'
        elif choice == '17':
            player_name = 'Alejandro_Garnacho'
        elif choice == '7':
            player_name = 'Mason_Mount'

        if player_name:
            display_player(player_name)
        else:
            print('Invalid Player')

def compare_players():
    print('Enter the jersey numbers of the two players you want to compare:')
    player1 = input('Player 1: ')
    player2 = input('Player 2: ')

    if player1 in players and player2 in players:
        print(f'Comparison between {player1} and {player2}:')
        print(f'{player1}:')
        display_player(player1)
        print(f'{player2}:')
        display_player(player2)
    else:
        print('Invalid Players')


def identify_statistic(statistic):
    max_player = max(players, key=lambda x: players[x][statistic])
    print(f'The player with the highest {statistic}:')
    display_player(max_player)


def main():
    while True:
        print('What do you want to do?')
        print('a. Player Review')
        print('b. Compare two players')
        print('c. Identify the fastest player')
        print('d. Identify the top goal scorer')
        print('e. Identify the player with the most assists')
        print('f. Identify the player with the highest passing accuracy')
        print('g. Identify the player with the most defensive involvements')
        print('h. Exit')

        choice = input('Choose a, b, c, d, e, f, g, or h: ')

        if choice.lower() == 'a':
            player_review()
        elif choice.lower() == 'b':
            compare_players()
        elif choice.lower() == 'c':
            identify_statistic(1) 
        elif choice.lower() == 'd':
            identify_statistic(0)  
        elif choice.lower() == 'e':
            identify_statistic(2)  
        elif choice.lower() == 'f':
            identify_statistic(3)  
        elif choice.lower() == 'g':
            identify_statistic(4)  
        elif choice.lower() == 'h':
            break
        else:
            print('Invalid option. Please choose again.')

if __name__ == "__main__":
    main()
