using System.Diagnostics;

namespace Valencia_Hospital_Appointments;

class Program
{
    const string USER = "system";
    const string PASSWORD = "123456*";
    const string EXIT_OPTION = "E";
    const int MAX_ATTEMPTS = 3;
    const int DOCTORS_PER_SPECIALTY = 3;
    const int MAX_APPOINTMENT_LIMIT = 3;
    static string[] doctors_GeneralMedicine = ["Pedro Pérez", "Luisa López", "Valentina Ramírez"];
    static string[] doctors_EmergencyCare = ["Luis Brito","Angela Abad","John Hopkins"];
    static string[] doctors_ClinicalAnalysis = ["María Elena Franco","Aura Morales","Gabriel Bustamante"];
    static string[] doctors_Cardiology = ["Armando Bianco","Mailin Piñero","Juan Luque"];
    static string[] doctors_Neurology = ["Luis Torres","Marlene Odremán","Eliécer Urbina"];
    static string[] doctors_Nutrition = ["Héctor Machado","Maricarmen Rincones","Amada Ruiz"];
    static string[] doctors_Physiotherapy = ["Fabiola Luna","Andrés Zapata","Lorgelys Martínez"];
    static string[] doctors_Traumatology = ["Madis Siso","César Arveláez","Carolina Suárez"];
    static string[] doctors_InternalMedicine = ["Gerardo Vitale","Rubén Pereira","Katiuska Ramírez"];
    Dictionary<string,int> userAppointments = new Dictionary<string, int>();


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

        showMenu();
        string selectedOption = Console.ReadLine();

        switch (int.Parse(selectedOption))
        {
            case 1:
                break;
        }
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

    static void showMenu()
    {
        Console.WriteLine("Valencia Hospital Appointments");
        Console.WriteLine("------------------------------");
        Console.WriteLine("Choose specialty: ");
        Console.WriteLine("1. General Medicine");
        Console.WriteLine("2. Emergency Care");
        Console.WriteLine("3. Clinical Analysis");
        Console.WriteLine("4. Cardiology");
        Console.WriteLine("5. Neurology");
        Console.WriteLine("6. Nutrition");
        Console.WriteLine("7. Physiotherapy");
        Console.WriteLine("8. Traumatology");
        Console.WriteLine("9. Internal Medicine");
        Console.WriteLine("------------------------------");
        Console.WriteLine("Choose an option (Press E to exit): ");
    }
}