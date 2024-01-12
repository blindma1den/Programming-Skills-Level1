namespace RH_Hotels_Booking;

class Prices
{
    public int SingleRoom = 100;
    public int DoubleRoom = 200;
    public int GroupRoom = 350;
    public int VipSuite = 450;
    public int LuxurySuite = 550;
}

class Program
{
    static int MAX_ATTEMPTS = 3;
    // RH Hotels Localizations: Spain, France, Portugal, Italy, Germany
    const int EXIT_OPTION = 2;
    const string USER = "system";
    const string PASSWORD = "123456*";
    static int singlePrice = 100;
    static int doublePrice = 200;
    static int groupPrice = 350;
    static int vipPrice = 450;
    static int luxuryPrice = 550;

    static string[] SpainCities = ["MADRID","BARCELONA","VALENCIA"];
    static string[] GermanyCities = ["MUNICH","BERLIN"];
    static string[] ItalyCities = ["ROME","MILAN"];
    static string[] FranceCities = ["Paris","Marseille"];
    static string[] PortugalCities = ["Madeira","Lisbon","Porto"];

    static void Main(string[] args)
    {
        Console.WriteLine("Input username: ");
        string user = Console.ReadLine();
        Console.WriteLine("Input password");
        string password = Console.ReadLine();

        if (!loginSuccess(user,password))
        {
            Console.WriteLine("You are reaching max attempts allowed. Try again later");
            Console.WriteLine("");
            return;
        }
        
        int selectedOption = 0;

        while ( selectedOption != EXIT_OPTION )
        {
            showMenu();
            selectedOption = int.Parse(Console.ReadLine());

            switch (selectedOption)
            {
                case 1:
                    makeReservation();
                    break;
                default:
                    break;
            }
        }
    }

    static void showMenu()
    {
        Console.WriteLine("RH Hotels - Booking");
        Console.WriteLine("-------------------");
        Console.WriteLine("1. Make a reservation");
        Console.WriteLine("--------------------");
        Console.WriteLine("Select an option (press 2 to exit): ");
    }

    static bool loginSuccess(string user, string password)
        {
            int loginAttempts = 0;

            while (loginAttempts <= MAX_ATTEMPTS)
            {

                if (user == USER)
                {
                    if (password == PASSWORD) 
                    {
                        return true;
                    }
                    else
                    {
                        loginAttempts++;
                    } // (password == PASSWORD)
                }
                else
                {
                    Console.WriteLine("User does not exists. Try again");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();
                }

            }
            
            return false;
        }

    static void makeReservation()
    {
        Console.WriteLine("Select a country (SPAIN, FRANCE, PORTUGAL, ITALY, GERMANY): ");
        string selectedCountry = Console.ReadLine();
        showCitiesForCountrySelected(selectedCountry);
        string selectedCity = Console.ReadLine();
        Console.WriteLine("Select rooms quantity");
        Console.WriteLine("---------------------");
        Console.WriteLine("How many Single Rooms ($100)? (0 to continue):");
        int singleRoomsQuantity = int.Parse(Console.ReadLine());
        Console.WriteLine("How many Double Rooms ($200)? (0 to continue):");
        int doubleRoomsQuantity = int.Parse(Console.ReadLine());
        Console.WriteLine("How many Group Rooms ($350)? (0 to continue):");
        int groupRoomsQuantity = int.Parse(Console.ReadLine());
        Console.WriteLine("How many VIP Rooms ($450)? (0 to continue):");
        int vipRoomsQuantity = int.Parse(Console.ReadLine());
        Console.WriteLine("How many Luxury Suites ($550)? (0 to continue):");
        int luxuryRoomsQuantity = int.Parse(Console.ReadLine());

        Console.WriteLine("Are you confirming this transaction? (y/n):");
        string confirmation = Console.ReadLine();

        if ( confirmation == "n" )
        {
            return;
        }

        Console.WriteLine("Input your name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Input your surname: ");
        string surname = Console.ReadLine();
        Console.WriteLine("Input your ID / Passport number: ");
        string idNumber = Console.ReadLine();
        
        // making calculations
        
        int singleTotal = singleRoomsQuantity * singlePrice, doubleTotal = doubleRoomsQuantity * doublePrice; 
        int groupTotal = groupRoomsQuantity * groupPrice, vipTotal = vipRoomsQuantity * vipPrice, luxuryTotal = luxuryRoomsQuantity * luxuryPrice;
        int totalAmount = singleTotal + doubleTotal + groupTotal + vipTotal + luxuryTotal;

        Console.WriteLine("Reservation Information");
        Console.WriteLine("-----------------------");
        Console.WriteLine($"Name: {name}");
        Console.WriteLine($"Surname: {surname}");
        Console.WriteLine($"Identification Number: {idNumber}");
        Console.WriteLine("----------------------------------");
        Console.WriteLine("Reservation Details");
        Console.WriteLine("----------------------------------");

        if (singleRoomsQuantity > 0)
        {
            Console.WriteLine($"Single Rooms: {singleRoomsQuantity}");
            Console.WriteLine($"Total: {singleTotal}");
        }

        if (doubleRoomsQuantity > 0)
        {
            Console.WriteLine($"Double Rooms: {doubleRoomsQuantity}");
            Console.WriteLine($"Total: {doubleTotal}");
        }

        if (groupRoomsQuantity > 0)
        {
            Console.WriteLine($"Group Rooms: {groupRoomsQuantity}");
            Console.WriteLine($"Total: {groupTotal}");
        }

        if (vipRoomsQuantity > 0)
        {
            Console.WriteLine($"VIP Rooms: {vipRoomsQuantity}");
            Console.WriteLine($"Total: {vipTotal}");
        }

        if (luxuryRoomsQuantity > 0)
        {
            Console.WriteLine($"Luxury Suites: {luxuryRoomsQuantity}");
            Console.WriteLine($"Total: {luxuryTotal}");
        }

        Console.WriteLine($"Total amount: {totalAmount}");
        Console.WriteLine("----------------------------");
        Console.WriteLine("Press a key to continue...");
        Console.ReadLine();
    }

    static void showCitiesForCountrySelected(string country)
    {
        Console.WriteLine($"{country} Available Cities");
        Console.WriteLine("-------------------------");
        Console.WriteLine("");

        int menuOption = 1;
        switch (country)
        {
            case "SPAIN":
                
                foreach ( string city in SpainCities )
                {
                    Console.WriteLine($"{menuOption}. {city}");
                    menuOption++;
                }
                
                break;
            
            case "FRANCE":
                
                foreach ( string city in FranceCities )
                {
                    Console.WriteLine($"{menuOption}. {city}");
                    menuOption++;
                }
                
                break;
            
            case "PORTUGAL":
                
                foreach ( string city in PortugalCities )
                {
                    Console.WriteLine($"{menuOption}. {city}");
                    menuOption++;
                }
                
                break;

            case "ITALY":
                
                foreach ( string city in ItalyCities )
                {
                    Console.WriteLine($"{menuOption}. {city}");
                    menuOption++;
                }
                
                break;

            case "GERMANY":
                
                foreach ( string city in GermanyCities )
                {
                    Console.WriteLine($"{menuOption}. {city}");
                    menuOption++;
                }
                
                break;
        }

        Console.WriteLine("");
        Console.WriteLine("Select an option: ");
    }

    static void showPricelist()
    {

    }
}