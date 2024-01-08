# 1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
# The system should also allow comparison between two players. Use the following player profiles:

# Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
# Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
# Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
# Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
# Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
# The program functions as follows: The coach accesses the system and encounters a menu with the following options:

# Player Review: By entering the player's jersey number, they can access the player's characteristics.
# Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
# Identify the fastest player: Displays the player with the most points in speed.
# Identify the top goal scorer: Displays the player with the most points in goals.
# Identify the player with the most assists: Displays the player with the most points in assists.
# Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
# Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
# The system should also allow returning to the main menu.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PLAYERS = [
  {
    'name': 'Bruno Fernandes',
    'jersey': 8,
    'goals': 5,
    'speed': 6,
    'assists': 9,
    'passing accuracy': 10,
    'defensive involvements': 3
  },
  {
    'name': 'Rasmus Hojlund',
    'jersey': 11,
    'goals': 12,
    'speed': 8,
    'assists': 2,
    'passing accuracy': 6,
    'defensive involvements': 2
  },
  {
    'name': 'Harry Maguire',
    'jersey': 5,
    'goals': 1,
    'speed': 5,
    'assists': 1,
    'passing accuracy': 7,
    'defensive involvements': 9
  },
  {
    'name': 'Alejandro Garnacho',
    'jersey': 17,
    'goals': 8,
    'speed': 7,
    'assists': 8,
    'passing accuracy': 6,
    'defensive involvements': 0
  },
  {
    'name': 'Mason Mount',
    'jersey': 7,
    'goals': 2,
    'speed': 6,
    'assists': 4,
    'passing accuracy': 8,
    'defensive involvements': 1
  }
]

def main():
  while True:
    choice = showMenu()
    if choice == 8:
      exit()
    elif choice == 1:
      player = getJerseyNumber()
      if player != None:
        reviewPlayer(player)
        continue
    elif choice == 2:
      print("First Player --------")
      player1 = getJerseyNumber()
      if player1 != None:
        print("Second Player --------")
        player2 = getJerseyNumber()
        if player2 != None:
          comparePlayers(player1, player2)
        else:
          continue
      else:
        continue
    elif choice == 3:
      fastestPlayer()
      pass
    elif choice == 4:
      topGoalScorer()
      pass
    elif choice == 5:
      mostAssists()
      pass
    elif choice == 6:
      highestPassingAccuracy()
      pass
    elif choice == 7:
      mostDefensiveInvolvements()
      pass

def mostDefensiveInvolvements():
  for player in PLAYERS:
    if player['defensive involvements'] == max(player['defensive involvements'] for player in PLAYERS):
      print(f"\nThe player with the most defensive involvements is {player.get('name')} with {player.get('defensive involvements')} defensive involvements\n")

def highestPassingAccuracy():
  for player in PLAYERS:
    if player['passing accuracy'] == max(player['passing accuracy'] for player in PLAYERS):
      print(f"\nThe player with the highest passing accuracy is {player.get('name')} with {player.get('passing accuracy')} passing accuracy\n")

def mostAssists():
  for player in PLAYERS:
    if player['assists'] == max(player['assists'] for player in PLAYERS):
      print(f"\nThe player with the most assists is {player.get('name')} with {player.get('assists')} assists\n")

def topGoalScorer():
  for player in PLAYERS:
    if player['goals'] == max(player['goals'] for player in PLAYERS):
      print(f"\nThe top goal scorer is {player.get('name')} with {player.get('goals')} goals\n")

def fastestPlayer():
  for player in PLAYERS:
    if player['speed'] == max(player['speed'] for player in PLAYERS):
      print(f"\nThe fastest player is {player.get('name')} with {player.get('speed')} speed points\n")

def comparePlayers(player1, player2):
  print("\n\t\tPlayer Comparison")
  print(f"{player1.get('name')} | {player2.get('name')}\n")
  print(f"Jersey Number: {player1.get('jersey')} | {player2.get('jersey')}")
  print(f"Goals: {player1.get('goals')} | {player2.get('goals')}")
  print(f"Speed Points: {player1.get('speed')} | {player2.get('speed')}")
  print(f"Assists: {player1.get('assists')} | {player2.get('assists')}")
  print(f"Passing Accuracy: {player1.get('passing accuracy')} | {player2.get('passing accuracy')}")
  print(f"Defensive Involvements: {player1.get('defensive involvements')} | {player2.get('defensive involvements')}")

def getJerseyNumber():
  try:
    number = int(input("Enter the player's jersey number: "))
    for player in PLAYERS:
      if player['jersey'] == number:
        return player
      else:
        continue
    print(f"There is no player with the jersey number {number}\n") 
  except:
    print("Invalid input\n")

def reviewPlayer(player):
  print(f"\nName: {player.get('name')}\n")
  print(f"Jersey Number: {player.get('jersey')}\n")
  print(f"Goals: {player.get('goals')}\n")
  print(f"Speed Points: {player.get('speed')}\n")
  print(f"Assists: {player.get('assists')}\n")
  print(f"Passing Accuracy: {player.get('passing accuracy')}\n")
  print(f"Defensive Involvements: {player.get('defensive involvements')}\n\n")

def showMenu():
  print("\t\tWelcome to the Player's System\n\n")
  print("1. Player Review\n")
  print("2. Compare two players\n")
  print("3. Identify the fastest player\n")
  print("4. Identify the top goal scorer\n")
  print("5. Identify the player with the most assists\n")
  print("6. Identify the player with the highest passing accuracy\n")
  print("7. Identify the player with the most defensive involvements\n")
  print("8. Exit\n")
  try:
    choice = int(input(">> "))
    if choice < 1 or choice > 8:
      print("Invalid input\n")
    else:
      return choice if type(choice) == int else print("Invalid input\n")
  except:
    print("Invalid input\n")

if __name__ == "__main__":
  main()