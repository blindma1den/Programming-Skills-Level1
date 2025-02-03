using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace L1E4
{
    /*
    * Login; it should be locked after the third failed attempt.
    * 
    * 
       The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
       Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.

       All hotels have 24 rooms each: 3 single rooms, 6 double rooms, 6 group rooms, 6 VIP suites and 3 luxury suites.
       The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
       Single rooms are priced at $100 per night
       Double rooms at $200 per night
       Group rooms at $350 per night
       VIP suites at $450 per night
       Luxury suites at $550 per night ---> applicable at any time of the year.

       The algorithm functions as follows: 
        Login, choose country, choose city, choose room type, select the number of nights, 
        collect user data (name, surname, ID/passport), print the total cost, and if the user agrees, 
        print a confirmation message for the reservation. If not, return to the main menu.
     
     */

    class Prices
    {
        public int SingleRoom = 100;
        public int DoubleRoom = 200;
        public int GroupRoom = 350;
        public int VipSuite = 450;
        public int LuxurySuite = 550;

    }

    internal class Program
    {

        //Login variables
        static int attempts = 3;
        const string username = "admin";
        const string password = "123";


        //menu exit option
        const int exitSystem = 2;

        //prices
        static float SingleRoomPrice = 100;
        static float DoubleRoomPrice = 200;
        static float GroupRoomPrice = 350;
        static float VipSuitePrice = 450;
        static float LuxurySuitePrice = 550;


        //UserPreferences



        //cities arrays
        static string[] countries = {"Spain","Germany","Italy", "France", "Portugal"}; 
        
        static string[] SpainCities = { "Madrid", "Bacerlona", "Valencia" };
        static string[] GermanyCities = { "Munich", "Berlin" };
        static string[] ItalyCities = { "Rome", "Milan" };
        static string[] FranceCities = { "Paris", "Marseille" };
        static string[] PortugalCities = { "Madeira", "Lisboa", "Porto" };

        static void Main(string[] args)
        {


            if (Login())
            {
                Menu();
            }



        }

        static void Menu()
        {
            int optionChosed;

            Console.Clear();
            Console.WriteLine("Welcome to RH Hotel Reservations System.");
            Console.WriteLine("1. Make a Reservation \n2. Exit the System");
            do
            {
                Console.WriteLine("\nPlease, choose an option from the menu...");
                int.TryParse(Console.ReadLine(), out optionChosed);

            } while (optionChosed <=0 || optionChosed >=3);

            if (optionChosed == exitSystem)
            {
                Console.WriteLine("Thanks for using our system.");
                Console.WriteLine("Closing...");
                Thread.Sleep(3000);
            }
            else if (optionChosed == 1)
            {
                Reservation();
            }
        }

        static bool Login()
        {
            bool grantedAccess = false;
            int loginAttempts = 0;
            //string typedUsername, typedPassword;
            

            do
            {
                Console.Clear();

                Console.WriteLine(" --- RH HOTELS ---");
                Console.WriteLine("*** Login ***");
                Console.Write("Type your username: ");
                string typedUsername = Console.ReadLine();
                Console.Write("Type your password: ");
                string typedPassword = Console.ReadLine();

                if (typedUsername == username)
                {
                    if (typedPassword == password)
                    {
                        
                        Console.WriteLine($"Granted Access. Welcome: {username}. Press any key to continue...");
                        grantedAccess = true;
                        Console.ReadKey();
                        break;
                    }
                    else
                    {
                        loginAttempts++;
                        attempts--;
                        Console.WriteLine($"Wrong Password. Try Again. LOGIN ATTEMPT N°{loginAttempts} - ATTEMPTS LEFT: {attempts}");
                        Console.WriteLine("Press any key to try again...");
                        Console.ReadKey();
                    }
                }
                else
                {

                        Console.WriteLine("User typed does not exist. Try again.\nPress any key to continue...");
                        Console.ReadKey();
                    
                }



            } while (attempts > 0);
          
                
                if (attempts  <= 0)
                {
                    grantedAccess = false;
                    Console.WriteLine("The system has been blocked due to too many attempts. Try again later...\nPress any key to exit...");
                    Console.ReadKey();
                    Environment.Exit(0);
                }
            
            
            return grantedAccess;

        }

        static void Reservation()
        {
            string countryChosed, cityChosed;

            int singleRoomsQuantity, doubleRoomsQuantity, groupRoomsQuantity, vipRoomsQuantity, luxuryRoomsQuantity;


            Console.Clear();
            Console.WriteLine(" --- RESERVATION MENU --- ");
            Console.WriteLine("Please, type the name of the country to select a country from above: ");
            for (int i = 0; i < countries.Length; i++)
            {
                Console.WriteLine($"* {countries[i]}");
            }
            countryChosed = Console.ReadLine();

            ShowCities(countryChosed);

            cityChosed = Console.ReadLine();

            Console.WriteLine("ROOMS QUANTITY");
            Console.Write("Single Rooms Quantity ($100 each Single Room - ENTER 0 TO SKIP/CONTINUE): ");
            int.TryParse(Console.ReadLine(), out singleRoomsQuantity);
            Console.Write("Double Rooms Quantity ($200 each Single Room - ENTER 0 TO SKIP/CONTINUE): ");
            int.TryParse(Console.ReadLine(), out doubleRoomsQuantity);
            Console.Write("Group Rooms Quantity ($350 each Single Room - ENTER 0 TO SKIP/CONTINUE): ");
            int.TryParse(Console.ReadLine(), out groupRoomsQuantity);
            Console.Write("VIP Rooms Quantity ($450 each Single Room - ENTER 0 TO SKIP/CONTINUE): ");
            int.TryParse(Console.ReadLine(), out vipRoomsQuantity);
            Console.Write("Luxury Rooms Quantity ($550 each Single Room - ENTER 0 TO SKIP/CONTINUE): ");
            int.TryParse(Console.ReadLine(), out luxuryRoomsQuantity);


            Console.WriteLine("Do you confirm the operation? (y/n):");
            string confirmation = Console.ReadLine();

            if (confirmation == "n")
            {
                Menu();
            }

            Console.WriteLine("Input your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Input your surname: ");
            string surname = Console.ReadLine();
            Console.WriteLine("Input your ID / Passport number: ");
            string idNumber = Console.ReadLine();


            //calculations

            float singleRoomsTotal = singleRoomsQuantity * SingleRoomPrice;
            float doubleRoomsTotal = doubleRoomsQuantity * DoubleRoomPrice;
            float groupRoomsTotal = groupRoomsQuantity * GroupRoomPrice;
            float vipRoomsTotal = vipRoomsQuantity * VipSuitePrice;
            float luxuryRoomsTotal = luxuryRoomsQuantity * LuxurySuitePrice;
            float total = singleRoomsTotal + doubleRoomsTotal + groupRoomsTotal + vipRoomsTotal + luxuryRoomsTotal;

            ShowDetails(name, surname, idNumber, singleRoomsQuantity, singleRoomsTotal, doubleRoomsQuantity, doubleRoomsTotal, groupRoomsQuantity, groupRoomsTotal, vipRoomsQuantity, vipRoomsTotal, luxuryRoomsQuantity, luxuryRoomsTotal, total);

        }

        static void ShowCities(string countryParameter)
        {
            Console.WriteLine($"\n{countryParameter} cities");
            Console.WriteLine("**************************");

            switch (countryParameter.ToUpper())
            {
                case "SPAIN":

                    foreach (var ciudad in SpainCities)
                    {
                        Console.WriteLine($"{0+1}. {ciudad}");
                    }

                break;

                case "FRANCE":
                    foreach (var ciudad in FranceCities)
                    {
                        Console.WriteLine($"{0 + 1}. {ciudad}");
                    }
                    break;

                case "PORTUGAL":
                    foreach (var ciudad in PortugalCities)
                    {
                        Console.WriteLine($"{0 + 1}. {ciudad}");
                    }
                    break;


                case "ITALY":
                    foreach (var ciudad in ItalyCities)
                    {
                        Console.WriteLine($"{0 + 1}. {ciudad}");
                    }
                    break;

                case "GERMANY":
                    foreach (var ciudad in GermanyCities)
                    {
                        Console.WriteLine($"{0 + 1}. {ciudad}");
                    }
                    break;

                default:
                    Console.WriteLine("DEFAULT OPTION");
                    break;
            }

            Console.Write("\nChoose your preferred city: ");

        }

        static void ShowDetails(string nameP, string surnameP, string idP, int singles, float singlesTotal, int doubles, float doublesTotal,  int groups, float groupsTotal,  int vips, float vipsTotal, int luxurys, float luxurysTotal, float totalP)
        {
            Console.Clear();

            Console.WriteLine("Reservation Information");
            Console.WriteLine("-----------------------");
            Console.WriteLine($"Name: {nameP}");
            Console.WriteLine($"Surname: {surnameP}");
            Console.WriteLine($"Identification Number: {idP}");
            Console.WriteLine("----------------------------------");
            Console.WriteLine("Reservation Details");
            Console.WriteLine("----------------------------------");

            if (singles > 0)
            {
                Console.WriteLine($"Single Rooms: {singles}");
                Console.WriteLine($"Total: {singlesTotal}");
            }

            if (doubles > 0)
            {
                Console.WriteLine($"Double Rooms: {doubles}");
                Console.WriteLine($"Total: {doublesTotal}");
            }

            if (groups > 0)
            {
                Console.WriteLine($"Group Rooms: {groups}");
                Console.WriteLine($"Total: {groupsTotal}");
            }

            if (vips > 0)
            {
                Console.WriteLine($"VIP Rooms: {vips}");
                Console.WriteLine($"Total: {vipsTotal}");
            }

            if (luxurys > 0)
            {
                Console.WriteLine($"Luxury Suites: {luxurys}");
                Console.WriteLine($"Total: {luxurysTotal}");
            }

            Console.WriteLine($"Total amount: {totalP}");
            Console.WriteLine("----------------------------");
            Console.WriteLine("Press a key to continue...");
            Console.ReadLine();
            Menu();
        }


    }
}
