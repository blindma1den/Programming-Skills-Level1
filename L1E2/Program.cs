using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace L1E2
{
    internal class Program
    {

        /*
         
        2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget
         */


        static int selectedSeason;
        static int selectedActivity;
        static string selectedCountry;
        static string seasonName;
        static float leftOver;
        static float initialBudget;
        static float selectedSeasonCost;

        static bool canGo;

        const float winterCost = 100;
        const float autumnCost = 200;
        const float springCost = 300;
        const float summerCost = 400;



        static void Main(string[] args)
        {
            Console.WriteLine(" --- TRAVEL AGENCY ---");
            Console.WriteLine("Welcome to our Travel Agency. Please, enter your budget so we can adjust a plan for you.");
            float.TryParse(Console.ReadLine(), out initialBudget);

            Console.WriteLine("Great!\nNow, please, choose your prefered season of the year from the following options:");
            Console.WriteLine(" --[SEASONS]-- " +
                "\n1. WINTER" +
                "\n2. AUTUMN" +
                "\n3. SPRING" +
                "\n4. SUMMER");


            Console.WriteLine("Enter the number of your prefered season.");
            do
            {

                int.TryParse(Console.ReadLine(), out selectedSeason);

                if ((selectedSeason <= 0) || (selectedSeason >= 5))
                {
                    Console.WriteLine("INVALID. You must enter a number between 1 and 4, as is shown in the list of options.");
                }

            } while ((selectedSeason <= 0) || (selectedSeason >= 5));

            if (selectedSeason == 1)
            {
                seasonName = "Winter";
            }
            else if (selectedSeason == 2)
            {
                seasonName = "Autumn";
            }
            else if (selectedSeason == 3)
            {
                seasonName = "Spring";
            }
            else
            {
                seasonName = "Summer";
            }


            switch (selectedSeason)
            {
                case 1://WINTER
                    Winter();
                    AgencyRecomendation();
                    break;
                case 2:
                    Autumn();
                    AgencyRecomendation();
                    break;
                case 3:
                    Spring();
                    AgencyRecomendation();
                    break;
                case 4:
                    Summer();
                    AgencyRecomendation();
                    break;
                default:
                    Console.WriteLine("DEFAULT CASE. Try Again.");
                    break;
            }

            

        }

        static void Winter()
        {
            selectedSeasonCost = winterCost;
            leftOver = initialBudget - winterCost;
            if (initialBudget < winterCost)
            {
                canGo = false;
            }
            else
            {
                canGo = true;
            }
            Console.WriteLine(" ---[ WINTER ]--- ");
            Console.WriteLine("You chose WINTER as your prefered season.");
            Console.WriteLine("In Winter, we have different kind of activities to enjoy!");
            Console.WriteLine("---" +
                "\n1. Skiing" +
                "\n2. Tour of the Swiss Alps" +
                "\nPlease, choose one from above...");

            do
            {
                int.TryParse(Console.ReadLine(), out selectedActivity);
                if ((selectedActivity <= 0) || (selectedActivity >= 3))
                {
                    Console.WriteLine("INVALID. You must enter a number between 1 and 2, as is shown in the list of activities.");
                }

            } while ((selectedActivity <= 0) || (selectedActivity >= 3));

            if (selectedActivity == 1)
            {
                Console.WriteLine("You chose SKIING as your preferred activity");
                selectedCountry = "Andorra";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("You chose the Tour of the Swiss Alps");
                selectedCountry = "Switzerland";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
        }

        static void Autumn()
        {
            selectedSeasonCost = autumnCost;
            leftOver = initialBudget - autumnCost;
            if (initialBudget < autumnCost)
            {
                canGo = false;
            }
            else
            {
                canGo = true;
            }//hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
            Console.WriteLine(" ---[ AUTUMN ]--- ");
            Console.WriteLine("You chose AUTUMN as your prefered season.");
            Console.WriteLine("In Autumn, we have different kind of activities to enjoy!");
            Console.WriteLine("---" +
                "\n1. Hiking and Extreme Sports" +
                "\n2. Cultural and Historical Activities" +
                "\nPlease, choose one from above...");

            do
            {
                int.TryParse(Console.ReadLine(), out selectedActivity);
                if ((selectedActivity <= 0) || (selectedActivity >= 3))
                {
                    Console.WriteLine("INVALID. You must enter a number between 1 and 2, as is shown in the list of activities.");
                }

            } while ((selectedActivity <= 0) || (selectedActivity >= 3));

            if (selectedActivity == 1)
            {
                Console.WriteLine("You chose Hiking and Extreme Sports as your preferred activity");
                selectedCountry = "Belgium";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("Cultural and Historical Activities");
                selectedCountry = "Austria";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
        }

        static void Spring()
        {
            selectedSeasonCost = springCost;
            leftOver = initialBudget - springCost;
            if (initialBudget < springCost)
            {
                canGo = false;
            }
            else
            {
                canGo = true;
            }//France extreme sports activities, and in Italy, there's a cultural and historical tour
            Console.WriteLine(" ---[ SPRING ]--- ");
            Console.WriteLine("You chose SPRING as your prefered season.");
            Console.WriteLine("In Srping, we have different kind of activities to enjoy!");
            Console.WriteLine("---" +
                "\n1. Extreme Sports" +
                "\n2. Cultural and Historical Tour" +
                "\nPlease, choose one from above...");

            do
            {
                int.TryParse(Console.ReadLine(), out selectedActivity);
                if ((selectedActivity <= 0) || (selectedActivity >= 3))
                {
                    Console.WriteLine("INVALID. You must enter a number between 1 and 2, as is shown in the list of activities.");
                }

            } while ((selectedActivity <= 0) || (selectedActivity >= 3));

            if (selectedActivity == 1)
            {
                Console.WriteLine("You chose Extreme Sports as your preferred activity");
                selectedCountry = "France";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("Cultural and Historical Tour");
                selectedCountry = "Italy";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }

        }

        static void Summer()
        {
            selectedSeasonCost = summerCost;
            leftOver = initialBudget - summerCost;
            if (initialBudget < summerCost)
            {
                canGo = false;
            }
            else
            {
                canGo = true;
            }//Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
            Console.WriteLine(" ---[ SUMMER ]--- ");
            Console.WriteLine("You chose SUMMER as your prefered season.");
            Console.WriteLine("In Summer, we have different kind of activities to enjoy!");
            Console.WriteLine("---" +
                "\n1. Hiking and Extreme Sports" +
                "\n2. Beach activities." +
                "\nPlease, choose one from above...");

            do
            {
                int.TryParse(Console.ReadLine(), out selectedActivity);
                if ((selectedActivity <= 0) || (selectedActivity >= 3))
                {
                    Console.WriteLine("INVALID. You must enter a number between 1 and 2, as is shown in the list of activities.");
                }

            } while ((selectedActivity <= 0) || (selectedActivity >= 3));

            if (selectedActivity == 1)
            {
                Console.WriteLine("You chose Hiking and Extreme Sports as your preferred activity");
                selectedCountry = "Spain";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("Beach Activities");
                selectedCountry = "Portugal";

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
        }
        static void AgencyRecomendation()
        {

            if (canGo == true)
            {
                Console.WriteLine("\nBased on your budget and the cost of the season, we got this: ");
                Console.WriteLine("---- [ RECEIPT ] ----" +
                    "\nStatus: You CAN travel." +
                    $"\nInitial Budget: {initialBudget}" +
                    $"\nSeason Cost: {selectedSeasonCost}" +
                    $"\nLeftover: {leftOver}");
                Console.WriteLine($"Our recommendation to you for destination is {selectedCountry} in {seasonName}");
                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
            else
            {
                Console.WriteLine("\nBased on your budget and the cost of the season, we got this: ");
                Console.WriteLine("---- [ RECEIPT ] ----" +
                    "\nStatus: You CANNOT travel!!!" +
                    "\nYour budget is under the required minimum to pay for the Season and Activity you choose for." +
                    $"\nInitial Budget: {initialBudget}" +
                    $"\nSeason Cost: {selectedSeasonCost}" +
                    $"\nLeftover: {leftOver}");
                Console.WriteLine($"Our recommendation to you for destination is {selectedCountry} in {seasonName}");
                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
        }
    }
}
