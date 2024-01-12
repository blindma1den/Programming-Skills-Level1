namespace Travel_Agency;

class Program
{
    const int WINTER_COST = 100;
    const int AUTUMN_COST = 200;
    const int SPRING_COST = 300;
    const int SUMMER_COST = 400;
    static int userBudget;
    static string selectedSeason;
    static string selectedActivity;
    static string selectedCountry;
    static int selectedCost;

    static void Main(string[] args)
    {
        Console.WriteLine("Input your budget: ");
        userBudget = int.Parse(Console.ReadLine());

        Console.WriteLine("Choose a Season (WINTER, AUTUMN, SPRING, SUMMER): ");
        selectedSeason = Console.ReadLine();

        Console.WriteLine("Now, you need choose your preference about activities: ");

        switch (selectedSeason)
        {
            case "WINTER":
                Console.WriteLine("1. Skiing Activities");
                Console.WriteLine("2. Tour of the Swiss Alps");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Select an option: ");
                int winter_Option = int.Parse(Console.ReadLine());

                if (winter_Option == 1) {
                    selectedActivity = "Skiing Activities";
                    selectedCountry = "ANDORRA";
                }
                else
                {
                    selectedActivity = "Tour of the Swiss Alps";
                    selectedCountry = "SWITZERLAND";
                }
                
                selectedCost = WINTER_COST;
                break;
            
            case "AUTUMN":
                Console.WriteLine("1. Hiking and Extreme Sports Activities");
                Console.WriteLine("2. Cultural and Historical Activities");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Select an option: ");
                int autumnOption = int.Parse(Console.ReadLine());

                if (autumnOption == 1) {
                    selectedActivity = "Skiing Activities";
                    selectedCountry = "BELGIUM";
                }
                else
                {
                    selectedActivity = "Tour of the Swiss Alps";
                    selectedCountry = "AUSTRIA";
                }
                selectedCost = AUTUMN_COST;
                break;

            case "SPRING":
                Console.WriteLine("1. Extreme Sports Activities");
                Console.WriteLine("2. Cultural and Historical Tour");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Select an option: ");
                int spring_option = int.Parse(Console.ReadLine());

                if (spring_option == 1) {
                    selectedActivity = "Extreme Sports Activities";
                    selectedCountry = "FRANCE";
                }
                else
                {
                    selectedActivity = "Cultural and Historical Tour";
                    selectedCountry = "ITALY";
                }
                selectedCost = SPRING_COST;
                break;

            case "SUMMER":
                Console.WriteLine("1. Hiking and Extreme Sports Activities");
                Console.WriteLine("2. Activities on Beaches");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Select an option: ");
                int summerOption = int.Parse(Console.ReadLine());

                if (summerOption == 1) {
                    selectedActivity = "Hiking and Extreme Sports Activities";
                    selectedCountry = "SPAIN";
                }
                else
                {
                    selectedActivity = "Activities on Beaches";
                    selectedCountry = "PORTUGAL";
                }
                selectedCost = SUMMER_COST;
                break;
            default:
                Console.WriteLine("Wrong option. Press a key to continue");
                Console.ReadLine();
                return;
        }

        Console.WriteLine("");
        Console.WriteLine($"Our recommendation to you for destination is {selectedCountry} in {selectedSeason}");
        Console.WriteLine("");
    }

}