using System.Numerics;
using System.Security.Cryptography;

namespace Manchester_United_Players_Analysis;

class Player
{
    public int JerseyNumber { get; set; }
    public string Name { get; set; }
    public int Goals { get; set; }
    public int Speed { get; set; }
    public int Assists { get; set; }
    public int Passing { get; set; }
    public int Defensive { get; set; }

    public Player(string name, int jerseyNumber, int goals, int speed, int assists, int passing, int defensive)
    {
        this.Name = name;
        this.JerseyNumber = jerseyNumber;
        this.Goals = goals;
        this.Speed = speed;
        this.Assists = assists;
        this.Passing = passing;
        this.Defensive = defensive;
    }
}

class Program
{

    const int EXIT_OPTION = 8;

    // Players Data Charge

    static void Main(string[] args)
    {
        Player BrunoFernandes = new Player("Bruno Fernandes",8,5,6,9,10,3);
        Player RasmusHojlund = new Player("Rasmus Hojlund",11,12,8,2,6,2);
        Player HarryMaguire = new Player("Harry Maguire",5,1,5,1,7,9);
        Player AlejandroGarnacho = new Player("Alejandro Garnacho",17,2,6,4,8,1);
        Player MasonMount = new Player("Mason Mount",7,2,6,4,8,1);

        Player[] team = [BrunoFernandes,RasmusHojlund,HarryMaguire,AlejandroGarnacho,MasonMount];

        int selectedOption = 0;
        while (selectedOption != EXIT_OPTION)
        {
            Console.Clear();
            showMenu();
            selectedOption = int.Parse(Console.ReadLine());

            switch (selectedOption)
            {
                case 1: // Player review
                    playerReview(team);
                    break;
                case 2: // Compare two players
                    comparePlayers(team);
                    break;
                case 3: // Fastest player
                    fastestPlayer(team);
                    break;
                case 4: // Top goal
                    topGoalScorer(team);
                    break;
                case 5: // Assists
                    mostAssistPlayer(team);
                    break;
                case 6: // Passing
                    highestPassingAccuracyPlayer(team);
                    break;
                case 7: // Defensive
                    mostDefensiveInvolvementsPlayer(team);
                    break;
            }
        }
    }

    static void showMenu()
    {
        Console.WriteLine("Manchester United FC");
        Console.WriteLine("--------------------");
        Console.WriteLine("1. Player review");
        Console.WriteLine("2. Compare two players");
        Console.WriteLine("3. Identify the fastest player");
        Console.WriteLine("4. Identify the top goal scorer");
        Console.WriteLine("5. Identify the player with the most assists");
        Console.WriteLine("6. Identify the player with the highest passing accuracy");
        Console.WriteLine("7. Identify the player with the most defensive involvements");
        Console.WriteLine("-----------------------------------------------------------");
        Console.WriteLine("Select an option (Press 8 to exit): ");
    }

    static void playerReview(Player[] team)
    {
        Console.Clear();
        Console.WriteLine("Enter player's jersey number: ");
        int jerseyNumber = int.Parse(Console.ReadLine());

        foreach (var player in team)
        {
            if (player.JerseyNumber == jerseyNumber)
            {
                showPlayerInfo(player);
                Console.WriteLine("Press a key to continue...");
                Console.ReadLine();
            }
        }
    }

    static void comparePlayers(Player[] team)
    {
        Console.Clear();
        Console.WriteLine("Enter player's 1 jersey number: ");
        int firstJerseyNumber = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter player's 2 jersey number: ");
        int secondJerseyNumber = int.Parse(Console.ReadLine());
        
        foreach (var player in team)
        {
            if (player.JerseyNumber == firstJerseyNumber)
            {
                Console.WriteLine("First Selected Player");
                showPlayerInfo(player);
            }

            if (player.JerseyNumber == secondJerseyNumber)
            {
                Console.WriteLine("Second Selected Player");
                showPlayerInfo(player);
            }
        }
        
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void fastestPlayer(Player[] team)
    {
        int majorSpeed = 0;
        Player fastestPlayer = null;

        foreach (var player in team)
        {
            if (player.Speed > majorSpeed)
            {
                majorSpeed = player.Speed;
                fastestPlayer = player;
            }
        }

        Console.WriteLine("Fastest Player");
        showPlayerInfo(fastestPlayer);
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void topGoalScorer(Player[] team)
    {
        int topGoals = 0;
        Player topScorerPlayer = null;

        foreach (var player in team)
        {
            if (player.Goals > topGoals)
            {
                topGoals = player.Goals;
                topScorerPlayer = player;
            }
        }

        Console.WriteLine("Top Scorer Player");
        showPlayerInfo(topScorerPlayer);
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void mostAssistPlayer(Player[] team)
    {
        int topAssists = 0;
        Player topAssistsPlayer = null;

        foreach (var player in team)
        {
            if (player.Goals > topAssists)
            {
                topAssists = player.Assists;
                topAssistsPlayer = player;
            }
        }

        Console.WriteLine("Top Assist Player");
        showPlayerInfo(topAssistsPlayer);
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void highestPassingAccuracyPlayer(Player[] team)
    {
        int numberPassing = 0;
        Player highestPassingPlayer = null;

        foreach (var player in team)
        {
            if (player.Passing > numberPassing)
            {
                numberPassing = player.Passing;
                highestPassingPlayer = player;
            }
        }

        Console.WriteLine("Highest Passing Accuracy Player");
        showPlayerInfo(highestPassingPlayer);
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void mostDefensiveInvolvementsPlayer(Player[] team)
    {
        int defensivePoints = 0;
        Player mostDefensivePlayer = null;

        foreach (var player in team)
        {
            if (player.Defensive > defensivePoints)
            {
                defensivePoints = player.Defensive;
                mostDefensivePlayer = player;
            }
        }

        Console.WriteLine("Most Defensive Player");
        showPlayerInfo(mostDefensivePlayer);
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void showPlayerInfo(Player player)
    {
        Console.WriteLine("");
        Console.WriteLine("Selected Player Data");
        Console.WriteLine("--------------------");
        Console.WriteLine($"({player.JerseyNumber}) Name: {player.Name}");
        Console.WriteLine("--------------------");
        Console.WriteLine("");
        Console.WriteLine("Stats");
        Console.WriteLine("--------------------");
        Console.WriteLine($"Goals: {player.Goals}");
        Console.WriteLine($"Speed: {player.Speed}");
        Console.WriteLine($"Assists: {player.Assists}");
        Console.WriteLine($"Passing: {player.Passing}");
        Console.WriteLine($"Defensive: {player.Defensive}");
        Console.WriteLine("");
    }
}
