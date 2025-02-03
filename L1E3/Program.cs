using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace L1E3
{
    internal class Program
    {

        /*The Valencia Hospital is developing an application to manage appointments. 
         * Design an algorithm for this application with the following features:

        DONE
        - It must have a login and validate the data; after the third failed attempt, it should be locked.


        TO DO
        - The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, 
        Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
        - There are 3 doctors for each specialty.
        - The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
        - The maximum limit for appointments, in general, is 3.
        - Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
        - Display available specialists.
        - The user can choose their preferred specialist.
        - The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.*/

        const string username = "admin";
        const string password = "123456";
        static int attempts = 3;
        static int maxAppointments = 0;

        static int optionChosed;

        static int timeSlotOption;
        static int confirmApp;

        

        static string[] generalMedicineDocs = { "Elizabeth Olsen", "Chris Pratt", "Tom Holland" };
        static string[] emergencyCareDocs = { "Laurence Fishburne", "Carrie Ann Moss", "Hugo Weaving" };
        static string[] clinicalAnalysisDocs = { "Ruben Doblas Gundersen", "Samuel de Luque", "Guillermo Diaz Ibáñez" };
        static string[] cardiologyDocs = { "Daarick Leeroy Lujan", "Anthony Bullón Gonzales", "Laura Malagon" };
        static string[] neurologyDocs = { "Barry Allen", "Bruce Wayne", "Clark Kent" };
        static string[] nutritionDocs = { "Tyson Diggs", "Zac Efron", "Peter Parker" };
        static string[] physiotherapyDocs = { "Scott Adkins", "Matt Mullins", "Michael J. White" };
        static string[] traumatologyDocs = { "Tony Stark", "Steve Rogers", "Johnny Storm" };
        static string[] internalMedicineDocs = { "Keanu Reeves", "Christian Bale", "Ryan Gosling" };

        static string[] morningHours = { "08:00", "09:30", "11:00" };
        static string[] afternoonHours = { "13:00", "15:30", "17:20" };
        static bool[] alreadyAppointment = { false, false, false, false, false, false, false, false, false };

        static string[] especialidades = {"General Medicine", "Emergency Care", "Clinical Analysis", "Cardiology", "Neurology",
        "Nutrition", "Physiotherapy", "Traumatology", "Internal Medicine"};


        static int doctorChosed, hourSlotChosed;

        static List<string[]> specialities = new List<string[]>()
        {
            generalMedicineDocs, emergencyCareDocs, clinicalAnalysisDocs, cardiologyDocs, neurologyDocs, nutritionDocs, physiotherapyDocs,
            traumatologyDocs, internalMedicineDocs
        };

        static List<string[]> slots = new List<string[]>()
        {
            morningHours, afternoonHours
        };


        

        // Accede dinámicamente a los horarios según el horario seleccionado
        //static string[] selectedTimeSlot = slots[hourSlotChosed - 1];

        

        static void Main(string[] args)
        {
            Random random = new Random();
            int randomDoctor = random.Next(1, 3);

            Console.WriteLine("Welcome to the Official Valencia Hospital Appointments System.");

            if (Login())
            {
                MainMenu();
            }

            while (optionChosed != 10)
            {
                MainMenu();
                do
                {
                    Console.WriteLine("Type a number to choose an option. (Enter '10' to exit the program)");
                    int.TryParse(Console.ReadLine(), out optionChosed);

                } while ((optionChosed <= 0) || (optionChosed >= 11));

                if (maxAppointments == 3)
                {
                    Console.WriteLine("You have reached the limit of appointments. You can't make another one.");
                    Console.WriteLine("Quitting the system... Press Any Key to exit..");
                    Console.ReadKey();
                    Environment.Exit(0);
                }

                if (optionChosed == 10)
                {
                    Console.Clear();
                    Console.WriteLine("Thanks for using our system.\nPress any key to exit...");
                    Console.ReadKey();
                    Environment.Exit(0);
                }


                if (optionChosed >=1 || optionChosed <=9)
                {
                    if (alreadyAppointment[optionChosed - 1] != true)
                    {
                        Appointment(randomDoctor);
                    }
                    else
                    {
                        Console.WriteLine($"You already have one appointment in this specific speciality.");
                        Console.WriteLine("Press any key to return to menu");
                        Console.ReadKey();
                        MainMenu();
                    }
                }
                    
            }

        }

        static bool Login()
        {

            //Declaro 2 strings que reciben el usuario y contraseña
            string logUser, logPass;
            //Declaro una variable de los intentos de logeo. Desde el inicio el primer intento de logeo se cuenta
            int loginAttempts = 1;
            //Declaro un booleano que confirma si pude acceder o no. si = true, no = false
            bool grantedAccess = false;


            //Un bucle dowhile que: 
            //Haga el proceso de Login y validación MIENTRAS QUE los 3 intentos de logeo inicial no sean menores o igual a 0
            do
            {
                Console.Clear();
                Console.WriteLine("---LOG-IN---");
                Console.WriteLine("Type your username...");
                logUser = Console.ReadLine();
                Console.WriteLine("Type your password...");
                logPass = Console.ReadLine();

                if (logUser == username) // Si coincide con el usuario, pasa a validar contraseña
                {
                    if (logPass == password) // Si coincide con la contra, le permite el acceso
                    {
                        Console.WriteLine($"Welcome! {username}");
                        grantedAccess = true; //permitimos acceso
                        Console.ReadKey();
                        break;
                        
                    }
                    else
                    {
                        //En caso de no coincidir la contraseña, se suman los intentos del logeo desde el usuario
                        //Y SE RESTA 1 intento de los intentos generales
                        loginAttempts++;
                        attempts--;
                        //Se muestra "loginAttempts-1" para no contar el intento que está por realizar.
                        Console.WriteLine($"Invalid! You typed the wrong password. Login Attempt: {loginAttempts-1}, Login Attempts Left: {attempts}");
                        Console.ReadKey();
                    }
                }
                else
                {
                    Console.WriteLine("User does not exists. Try again");
                    Console.WriteLine("Press a key to continue...");
                    Console.ReadLine();

                }

            } while (attempts > 0);

            if (attempts <= 0) // si los intentos generales son igual o menor que 0, se bloquea el sistema
            {
                grantedAccess = false; //NO Permitimos acceso
                Console.WriteLine("The system has been blocked due to too many attempts. Try again later...\nPress any key to exit...");
                Console.ReadKey();
                Environment.Exit(0);
            }

            return grantedAccess;
        }

        static void MainMenu()
        {
            Console.Clear();
            Console.WriteLine("----- MAIN MENU -----");
            Console.WriteLine("- Appointment System -");
            Console.WriteLine("Please, choose an speciality from below according to your needs");
             Console.WriteLine("--------------------------------------------" +
                "\n1. General Medicine" +
                "\n2. Emergency Care" +
                "\n3. Clinical Analysis" +
                "\n4. Cardiology" +
                "\n5. Neurology" +
                "\n6. Nutrition" +
                "\n7. Physiotherapy" +
                "\n8. Traumatology" +
                "\n9. Internal Medicine" +
                "\n---------------------------------------------" +
                $"\nAPPOINTMENTS MADE: {maxAppointments}");

        }
        static void Appointment(int randomNumberParameter)
        {
            Console.Clear();
            Console.WriteLine($"---- {especialidades[optionChosed-1]} Appointment ----");
            Console.WriteLine("Select your preferred time slot.");
            Console.WriteLine("1. Morning \n2. Afternoon");
            int.TryParse(Console.ReadLine(), out timeSlotOption);


            // Accede dinámicamente a los doctores según la especialidad seleccionada
            string[] selectedSpecialityDoctors = specialities[optionChosed - 1];

            if (timeSlotOption == 1) // TURNO DE LA MAÑANA --------------
            {
                Console.WriteLine("DOCTORS FOR MORNING APPOINTMENTS:");
                for (int i = 0; i < randomNumberParameter; i++)
                {
                    //Console.WriteLine($"{i+1} Doctors name: {generalMedicineDocs[i]}");
                    Console.WriteLine($"{i + 1} Doctors name: {selectedSpecialityDoctors[i]}");
                }
                foreach (var hours in morningHours)
                {
                    Console.WriteLine($"Morning available hours: {hours}");
                }

                Console.WriteLine("Select a Doctor");
                int.TryParse(Console.ReadLine(), out doctorChosed);
                Console.WriteLine("Select a Time Slot");
                int.TryParse(Console.ReadLine(), out hourSlotChosed);

            }
            else // TURNO DE LA TARDE -------------------
            {
                Console.WriteLine("DOCTORS FOR MORNING APPOINTMENTS:");
                for (int i = 0; i < randomNumberParameter; i++)
                {
                    Console.WriteLine($"{i + 1} Doctors name: {selectedSpecialityDoctors[i]}");
                }
                foreach (var hours in afternoonHours)
                {
                    Console.WriteLine($"Morning available hours: {hours}");
                }

                Console.WriteLine("Select a Doctor");
                int.TryParse(Console.ReadLine(), out doctorChosed);
                Console.WriteLine("Select a Time Slot");
                int.TryParse(Console.ReadLine(), out hourSlotChosed);

            }


            //CONFIRMAR CITA

            Console.WriteLine("Confirm Appointment: 1. YES - 2. NO");
            int.TryParse(Console.ReadLine(), out confirmApp);

            if (confirmApp == 1)
            {
                alreadyAppointment[optionChosed-1] = true;
                maxAppointments++;
                Console.WriteLine("APPOINTMENT CONFIRMED. Going back... Press any key to continue");
                Console.ReadKey();
                MainMenu();

            }
            else
            {
                alreadyAppointment[optionChosed-1] = false;
                Console.WriteLine("Appointment CANCELED. Going back... Press any key to continue");
                Console.ReadKey();
                MainMenu();
            }

        }
    }
}
