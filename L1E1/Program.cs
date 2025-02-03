using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace L1E1
{
    //Blindma1den Discord Community - Programming Level 1, Exercise 1

    /*
     1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
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
     */
    internal class Program
    {
        static void Main(string[] args)
        {
            const int exitOption = 8;

            Player pl1 = new Player("Bruno Fernandez", 8, 5, 6, 9, 10, 3);
            Player pl2 = new Player("Rasmus Hojlund", 11, 12, 8, 2, 6, 2);
            Player pl3 = new Player("Harry Maguire", 5, 1, 5, 1, 7, 9);
            Player pl4 = new Player("Alejandro Garnacho", 17, 8, 7, 8, 6, 0);
            Player pl5 = new Player("Mason Mount", 7, 2, 6, 4, 8, 1);

            Player[] manchesterUnited = { pl1, pl2, pl3, pl4, pl5 };

            int menuOption = 0;
            
            while (menuOption != exitOption)
            {
                Console.Clear();
                ShowMainMenu();
                int.TryParse(Console.ReadLine(), out menuOption);

                switch (menuOption)
                {
                    case 1: //Review 1 Player
                        PlayerReview(manchesterUnited);
                        break;
                    case 2:
                        ComparePlayers(manchesterUnited);
                        break;
                    case 3:
                        FastestPlayer(manchesterUnited);
                        break;
                    case 4: 
                        TopGoalScorer(manchesterUnited);
                        break;
                    case 5:
                        MostAssistsPlayer(manchesterUnited);
                        break;
                    case 6:
                        HighestPassingPlayer(manchesterUnited);
                        break;
                    case 7:
                        MostDefensivePlayer(manchesterUnited);
                        break;
                    case 8:
                        Console.WriteLine("Thanks for using the MUFC Software!");
                        Console.WriteLine("Press any key to exit...");
                        Console.ReadKey();
                        Environment.Exit(0);
                        break;
                    default:
                        break;
                }

            }

        }

        static void ShowMainMenu()
        {
            Console.Clear();
            Console.WriteLine("--- MANCHESTER UNITED FC SOFTWARE ---");
            Console.WriteLine("Welcome to the Manchester United FC Official Software©.\nPlease, choose an option from the menu that is being displayed below:");
            Console.WriteLine(
                "\n ----------------------------------------------------------------------------------------------------------" +
                "\n1. REVIEW A PLAYER: This option allows you to see all the information that a Player has." +
                "\n2. COMPARE PLAYERS: This option allows you to compare 2 players" +
                "\n3. FASTEST PLAYER: This option allows you to see who is the fastest player." +
                "\n4. TOP GOAL SCOARER: This option allows you to see who is the Top Goal Scoarer of the team" +
                "\n5. MOST ASSISTS PLAYER: This option allows you to see which Player has the most assists in the team" +
                "\n6. HIGHEST PASSING ACCURACY: This option allows you to identify the Player with the highest passing accuracy" +
                "\n7. MOST DEFENSIVE PLAYER: This option allows you to see the Player with the most defensive involvements" +
                "\n----------------------------------------------------------------------------------------------------------" +
                "\nRemember: You can type '8' to exit the Software!");

        }
        static void PlayerReview(Player[] teamParameter)
        {
            int jerseyNumber;
            int confirmOption = 0;
            Console.Clear();
            Console.WriteLine("Welcome, this is the Player Review option.\nPlease, enter the player's jersey number to continue");
            int.TryParse(Console.ReadLine(), out jerseyNumber);

            foreach (var player in teamParameter)
            {
                if (player.number == jerseyNumber)
                {
                    PlayerInfo(player);
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadKey();
                }
            }
        }

        static void ComparePlayers(Player[] teamParameter)
        {
           int firstPlayer, secondPlayer;
           Console.Clear();
           Console.WriteLine("Please, enter the jersey number of the first player");
           int.TryParse(Console.ReadLine(), out firstPlayer);
            Console.WriteLine("Please, enter the jersey number of the first player");
            int.TryParse(Console.ReadLine(), out secondPlayer);

            foreach (var player in teamParameter)
            {
                if (player.number == firstPlayer)
                {
                    Console.WriteLine("First Player:");
                    PlayerInfo(player);
                }

                if (player.number == secondPlayer)
                {
                    Console.WriteLine("Second Player:");
                    PlayerInfo(player);
                }
            }

            Console.WriteLine("Press any key to continue...");
            Console.ReadKey();

        }

        static void FastestPlayer(Player[] teamParameter)
        {
            int maxSpeed = 0;
            Player fastestPlayer = null;

            foreach (var player in teamParameter)
            {
                if (player.speedPoints > maxSpeed)
                {
                    maxSpeed = player.speedPoints;
                    fastestPlayer = player;
                }
            }

            Console.WriteLine("Fastest Player: \n");
            PlayerInfo(fastestPlayer);
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
        }

        static void TopGoalScorer(Player[] teamParameter)
        {
            int maxGoals = 0;
            Player topGoalerPlayer = null;

            foreach (var player in teamParameter)
            {
                if (player.goals > maxGoals)
                {
                    maxGoals = player.goals;
                    topGoalerPlayer = player;
                }
            }
            Console.WriteLine("Top Goaler Player: \n");
            PlayerInfo(topGoalerPlayer);
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();

        }

        static void MostAssistsPlayer(Player[] teamParameter)
        {
            int maxAssists = 0;
            Player mostAssistsPlayer = null;

            foreach (var player in teamParameter)
            {
                if (player.assistsPoints > maxAssists)
                {
                    maxAssists = player.assistsPoints;
                    mostAssistsPlayer = player;
                }
            }
            Console.WriteLine("Most Assists Player: \n");
            PlayerInfo(mostAssistsPlayer);
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
        }

        static void HighestPassingPlayer(Player[] teamParameter)
        {
            int highestNumPassing = 0;
            Player highestPassingPlayer = null;

            foreach (var player in teamParameter)
            {
                if (player.passingPoints > highestNumPassing)
                {
                    highestNumPassing = player.passingPoints;
                    highestPassingPlayer = player;
                }
            }
            Console.WriteLine("Highest Passing Points Player: \n");
            PlayerInfo(highestPassingPlayer);
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
        }

        static void MostDefensivePlayer(Player[] teamParameter)
        {
            int mostDefense = 0;
            Player mostDefensivePlayer = null;

            foreach (var player in teamParameter)
            {
                if (player.defensePoints > mostDefense)
                {
                    mostDefense = player.defensePoints;
                    mostDefensivePlayer = player;
                }
            }
            Console.WriteLine("Most Defensive Player: \n");
            PlayerInfo(mostDefensivePlayer);
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
        }
        
        static void PlayerInfo(Player playerParameter)
        {
            Console.WriteLine("---------------------------");
            Console.WriteLine("--- PLAYER INFORMATION ---");
            Console.WriteLine($"Player's Jersey Number: {playerParameter.number}, Name: {playerParameter.name}");
            Console.WriteLine("STATISTICS");
            Console.WriteLine($"GOALS: {playerParameter.goals}" +
                $"\nSPEED: {playerParameter.speedPoints}" +
                $"\nASSISTS: {playerParameter.assistsPoints}" +
                $"\nPASSING ACC: {playerParameter.passingPoints}" +
                $"\nDEFENSE: {playerParameter.defensePoints}");
            Console.WriteLine("---------------------------");

        }
    }
}
