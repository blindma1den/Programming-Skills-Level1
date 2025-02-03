using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Security.Cryptography;

namespace L1E5
{
    internal class TravelPlan
    {
        public string origin { get; set; }
        public string destination { get; set; }
        public string date { get; set; }
        public int hour { get; set; }
        public int condition { get; set; }
        public string meal { get; set; }
        public bool additionalLuggage { get; set; }

        public TravelPlan(string originCountry, string destinationCountry, string flightDate, int flightHour, int flightCondition, string preferredMeal, bool additionalLuggage)
        {
            this.origin = originCountry;
            this.destination = destinationCountry;
            this.date = flightDate;
            this.condition = flightCondition;
            this.meal = preferredMeal;
            this.additionalLuggage = additionalLuggage;
            this.hour = flightHour;
        }

    }

    internal class Program
    {

        /*
        5. 
        
Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. 
        
Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked.

The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
The user can choose their preferred meal: Regular, Vegetarian, Kosher.
The user must choose if they want to check an additional piece of luggage into the hold.
Hand luggage is free of charge.

The user must purchase both the outbound and return tickets.

The program must collect the following data: Name, country of origin, passport, and destination country.
Upon completing the process, the system will display everything the user has previously chosen along with their information. 
The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu. 
         

         */

        const string username = "system";
        const string password = "123";
        static int attempts = 3;

        static string[] countriesArray = {"Turkey", "Greece", "Lebanon", "Spain", "Portugal"};

        
        

        static string userFullName, userOgCountry, userPassport, userDestination, userFlightDate, userPreferredMeal;
        static int userFlightHour, userCondition, userExtraLuggage;
        static bool extraLuggage;

        static void Main(string[] args)
        {
            if (Login())
            {
                Menu();
            }
        }

        static bool Login()
        {
            bool grantedAccess = false;
            int logAttempts = 1;

            do
            {
                Console.Clear();
                Console.WriteLine("[--- LOG-IN ---]");
                Console.Write("Please, type your username: ");
                string typedUsername = Console.ReadLine();
                Console.Write("Please, type the password: ");
                string typedPassword = Console.ReadLine();

                if (typedUsername == username)
                {
                    if (typedPassword == password)
                    {
                        Console.WriteLine($"Welcome {username}! Press any key to continue to the system...");
                        grantedAccess = true;
                        Console.ReadKey();
                        break;
                    }
                    else
                    {
                        logAttempts++;
                        attempts--;
                        //Se muestra "loginAttempts-1" para no contar el intento que está por realizar.
                        Console.WriteLine($"Invalid! You typed the wrong password. Login Attempt: {logAttempts - 1}, Login Attempts Left: {attempts}");
                        Console.ReadKey();
                    }
                }
                else
                {
                    Console.WriteLine("The username typed does not exist! Try again.");
                    Console.WriteLine("Press any key to continue...");
                    Console.ReadKey();

                }


            } while (attempts > 0);

            if (attempts <= 0)
            {
                grantedAccess = false;
                Console.WriteLine("The system has been blocked due to too many attempts. Try again later...\n3 seconds to exit...");
                Thread.Sleep(3000);
            }





            return grantedAccess;
        }

        static void Menu()
        {
            int menuOption;

            Console.Clear();
            Console.WriteLine("Welcome to the Turkish Airlines Traveling System * !");
            Console.WriteLine("What do you want to do?");

            do
            {
                
                Console.WriteLine("1. Make a Flight Reservation" + "\n2. Exit the system");

                int.TryParse(Console.ReadLine(), out menuOption);

                if (menuOption == 1)
                {
                    FlightReservation();
                }
                else if (menuOption == 2)
                {
                    Console.WriteLine("Thanks for using our system! \n3 seconds to exit...");
                    Thread.Sleep(3000);
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid option. Please type a valid option from the menu");
                }

            } while ((menuOption <= 0) || menuOption >= 3);


        }

        static void FlightReservation()
        {
            Random random = new Random();
            float ticketsPrice = random.Next(110, 350);
            string confirmation;

            Console.Clear();
            Console.WriteLine(" ---- MAKE A RESERVATION ----");

            Console.WriteLine("AVAILABLE ORIGIN COUNTRIES: ");
            foreach (var countrie in countriesArray)
            {
                Console.WriteLine($"* {countrie}");
            }

            Console.Write("Please, enter the origin country: ");
            userOgCountry = Console.ReadLine();
            do
            {
                Console.Write("Now, enter the destination country: ");
                userDestination = Console.ReadLine();

                if (userDestination == userOgCountry)
                {
                    Console.WriteLine("You can't pick the same country as the origin and the destination.");
                    Console.WriteLine("Try again typing another country...");
                }
            } while (userDestination == userOgCountry);

            Console.Write("Enter the flight date (dd/mm/yy) (EXAMPLE: 11/03/2027): ");
            userFlightDate = Console.ReadLine();

            do
            {
                Console.Write("Enter the flight hour (24h) (EXAMPLE: 1600 = 04:00pm): ");
                int.TryParse(Console.ReadLine(), out userFlightHour);

                if (userFlightHour <= 0 || userFlightHour > 2400)
                {
                    Console.WriteLine("INVALID. Please enter a valid hour. Examples: 1600, 0800, 0400...");
                }

            } while (userFlightHour < 0 || userFlightHour > 2400);

            do
            {
                Console.WriteLine("Now, choose a condition (enter the number)" +
                "\n1. Economy" +
                "\n2. First Class");
                int.TryParse(Console.ReadLine(), out userCondition);

                if (userCondition <= 0 || userCondition >= 3)
                {
                    Console.WriteLine("INVALID. Please enter a valid option between 1 or 2.");
                }

            } while (userCondition <= 0 || userCondition >= 3);

            Console.Write("Enter now your preferred meal in letters (Regular, Vegetarian, Kosher): ");
            userPreferredMeal = Console.ReadLine();
            Console.WriteLine("\nDo you need extra luggage? Is free of charge" +
                "\n1. Yes " +
                "\n2. No");
            int.TryParse(Console.ReadLine(), out userExtraLuggage);

            if (userExtraLuggage == 1)
            {
                extraLuggage = true;
            }
            else
            {
                extraLuggage = false;
            }




            Console.WriteLine($"With the data received from you, the outbound ticket and the return ticket will cost: {ticketsPrice}");


            do
            {
                Console.WriteLine("Do you want to confirm the reservation? (y/n)");
                confirmation = Console.ReadLine();
                if (confirmation == "n")
                {
                    Menu();
                    break;
                }
                else if (confirmation == "y")
                {
                    Console.Write("Please enter your full name: ");
                    userFullName = Console.ReadLine();
                    Console.Write("Now, enter your Passport ID: ");
                    userPassport = Console.ReadLine();

                    TravelPlan r1 = new TravelPlan(userOgCountry, userDestination, userFlightDate, userFlightHour, userCondition, userPreferredMeal, extraLuggage);
                    ReservationDetails(r1, userFullName, userPassport, ticketsPrice);
                    break;
                }

            } while (confirmation != "y" || confirmation != "n");
            
            
            
            


            

            

        }
        
        static void ReservationDetails(TravelPlan reservation, string name, string passport, float totalCost)
        {
            Console.Clear();
            Console.WriteLine(" ---- RESERVATION DETAILS ----");
            Console.WriteLine($"Username: {username}" +
                $"\nFull name: {name}" +
                $"\nPassport ID: {passport}" +
                $"\nOrigin Country {reservation.origin.ToUpper()}" +
                $"\nDestination Country {reservation.destination.ToUpper()}" +
                $"\nFlight Date: {reservation.date}" +
                $"\nFlight Hour: {reservation.hour}");
            if (reservation.condition == 1)
            {
                Console.WriteLine("Condition: Economy");
            }
            else
            {
                Console.WriteLine("Condition: First Class");
            }
            Console.WriteLine($"Preferred Meal: {reservation.meal}");
            if (reservation.additionalLuggage == true)
            {
                Console.WriteLine("Extra Luggage: YES");
            }
            else
            {
                Console.WriteLine("Extra Luggage: NO");
            }
            Console.WriteLine("------------------");
            Console.WriteLine($"Total Cost: {totalCost}");

            Console.WriteLine("\nPROCESS COMPLETED... Press any key to continue...");
            Console.ReadKey();
            Menu();
            
            
        }

    }
}
