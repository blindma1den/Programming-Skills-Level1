import java.util.*;

public class RetoTres {

    private static HashMap<Integer, String> generalMedicine = new HashMap<>();
    private static HashMap<Integer, String> emergencyCare = new HashMap<>();
    private static HashMap<Integer, String> clinicalAnalysis = new HashMap<>();
    private static HashMap<Integer, String> cardiology = new HashMap<>();
    private static HashMap<Integer, String> neurology = new HashMap<>();
    private static HashMap<Integer, String> nutrition = new HashMap<>();
    private static HashMap<Integer, String> physiotherapy = new HashMap<>();
    private static HashMap<Integer, String> traumatology = new HashMap<>();
    private static HashMap<Integer, String> internalMedicine = new HashMap<>();
    private static ArrayList<Appointment> appointmentsArray = new ArrayList<>();
    private static ArrayList<Appointment> appointmentsCompare = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in).useDelimiter("\n");
    private static Random random = new Random(System.currentTimeMillis());

    public static void main(String[] args) throws InterruptedException {

        boolean isValid = false;
        String savedUsername = "user1";
        String savedPass = "ripeadmin";

        boolean isLogged = login(savedUsername, savedPass, isValid, scanner);

        String specialtyName;

        if(isLogged) {
            while (true) {
                specialtyName = mainMenu();
                switch (specialtyName) {
                    case "general medicine" -> {
                        initializeGeneralMedicine();
                        String name = selectDoctorGM();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);

                    }
                    case "emergency care" -> {
                        initializeEmergencyCare();
                        String name = selectDoctorEC();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "clinical analysis" -> {
                        initializeClinicalAnalysis();
                        String name = selectDoctorCA();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "cardiology" -> {
                        initializeCardiology();
                        String name = selectDoctorCD();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "neurology" -> {
                        initializeNeurology();
                        String name = selectDoctorNE();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "nutrition" -> {
                        initializeNutrition();
                        String name = selectDoctorNU();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "physiotherapy" -> {
                        initializePhysiotherapy();
                        String name = selectDoctorPH();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);
                        ;

                        Thread.sleep(2000);
                    }
                    case "traumatology" -> {
                        initializeTraumatology();
                        String name = selectDoctorTR();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "internal medicine" -> {
                        initializeInternalMedicine();
                        String name = selectDoctorIM();
                        int date = selectHours();

                        if (date <= 0 && date >= 3) break;

                        if (date != 3) summary(name, date, specialtyName);

                        Thread.sleep(2000);
                    }
                    case "exit" -> {
                        appointmentsArray.forEach(System.out::println);
                        System.out.println("Have a nice day!");
                        System.exit(0);
                    }
                    default -> System.out.println("Error, not an specialty, try again");
                }
            }
        }
    }

    static boolean login(String savedUsername, String savedPass, boolean isValid, Scanner scanner) {
        int count = 0;
        System.out.println("Welcome to your Orange Parcel Service \n" +
                "Please sign in");

        while (count < 3) {
            System.out.print("Username: ");
            String username = scanner.next();
            System.out.print("Password: ");
            String password = scanner.next();
            if (username.equals(savedUsername) && password.equals(savedPass)) {
                return isValid = true;
            } else {
                count = count + 1;
                System.out.println("Pass or user is incorrect");
            }
        }

        return isValid;
    }

    private static void summary(String name, int date, String specialtyName) {

        if(name != null && appointmentsArray.isEmpty()){
            appointmentsArray.add(new Appointment(name, specialtyName, date));
            System.out.println("Appointment Confirmed!");
        } else if (appointmentsArray.size() > 0 && appointmentsArray.size()<=3) {
            appointmentsCompare.add(new Appointment(name, specialtyName, date));
            if(isValid()){
                appointmentsCompare.clear();
                System.out.println("There's a duplicate name or Specialty, please check and start over");
            }
            else {
                appointmentsArray.addAll(appointmentsCompare);
                appointmentsCompare.clear();
                System.out.println("Appointment Confirmed!");
                if(appointmentsArray.size()==3){
                    System.out.println("You've reached the maximum amount of dates allowed:");
                    appointmentsArray.forEach(System.out::println);
                    System.out.println("This will be emailed to you, have a nice day!");
                    System.exit(0);
                }
            }
        }

        if(specialtyName.equals("exit") && (appointmentsArray.isEmpty() || appointmentsArray.size()==1 || appointmentsArray.size() == 2)){
                appointmentsArray.forEach(System.out::println);
                System.out.println("This will be emailed to you, have a nice day!");
            }
        }

    private static boolean isValid() {
        for (int i = 0; i < appointmentsArray.size(); i++) {
            for (int j = 0; j < appointmentsCompare.size(); j++) {
                if (appointmentsArray.get(i).getName().equals(appointmentsCompare.get(j).getName())
                 || appointmentsArray.get(i).getSpeciality().equals(appointmentsCompare.get(j).getSpeciality())){
                    return true;
                }
            }
        }
        return false;
    }

    private static String mainMenu() {
        System.out.println("Choose the specialty you want to create an appointment: ");
        System.out.println("- General Medicine");
        System.out.println("- Emergency Care");
        System.out.println("- Clinical Analysis");
        System.out.println("- Cardiology");
        System.out.println("- Neurology");
        System.out.println("- Nutrition");
        System.out.println("- Physiotherapy");
        System.out.println("- Traumatology");
        System.out.println("- Internal Medicine");
        System.out.println("- Exit");
        System.out.println("Remember, you can maximum set 3 appoints, one per specialty and is not possible ");
        System.out.println("To be attended by the same doctor twice, even if it is in different specialties");
        System.out.print("Type your option: ");

        return scanner.next().toLowerCase();
    }

    private static int selectHours() {
        int min = 8;
        int max = 12;
        int min2 = 13;
        int max2 = 20;
        int randomNumber = random.nextInt(max + 1 - min) + min;
        int randomNumber2 = random.nextInt(max2 + 1 - min2) + min2;

        System.out.println("Select the appointment time you prefer: ");
        System.out.println("1. " + randomNumber+"h");
        System.out.println("2. " + randomNumber2+"h");
        System.out.println("3. This options does not work for me, bring me back to main menu");
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        if(option == 1){
            option = randomNumber;
        } else if(option == 2){
            option = randomNumber2;
        }

        random.setSeed(System.currentTimeMillis());

        return option;
    }

    private static String selectDoctorIM() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= internalMedicine.size(); i++) {
            System.out.println((i) + " " + internalMedicine.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return internalMedicine.get(option);
    }

    private static String selectDoctorTR() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= traumatology.size(); i++) {
            System.out.println((i) + " " + traumatology.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return traumatology.get(option);
    }

    private static String selectDoctorPH() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= physiotherapy.size(); i++) {
            System.out.println((i) + " " + physiotherapy.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return physiotherapy.get(option);
    }

    private static String selectDoctorNU() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= nutrition.size(); i++) {
            System.out.println((i) + " " + nutrition.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return nutrition.get(option);
    }

    private static String selectDoctorNE() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= neurology.size(); i++) {
            System.out.println((i) + " " + neurology.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return neurology.get(option);
    }

    private static String selectDoctorCD() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= cardiology.size(); i++) {
            System.out.println((i) + " " + cardiology.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return cardiology.get(option);
    }

    private static String selectDoctorCA() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= clinicalAnalysis.size(); i++) {
            System.out.println((i) + " " + clinicalAnalysis.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return clinicalAnalysis.get(option);
    }



    private static String selectDoctorEC() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= emergencyCare.size(); i++) {
            System.out.println((i) + " " + emergencyCare.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return emergencyCare.get(option);
    }

    private static String selectDoctorGM() {
        System.out.println("Select your Doctor!");
        for (int i = 1; i <= generalMedicine.size(); i++) {
            System.out.println((i) + " " + generalMedicine.get(i));
        }
        System.out.print("Type your option: ");
        int option = scanner.nextInt();

        return generalMedicine.get(option);
    }

    private static void initializeInternalMedicine() {
        internalMedicine.put(1, "Torres");
        internalMedicine.put(2, "Neville");
        internalMedicine.put(3, "Potter");
    }

    private static void initializeTraumatology() {
        traumatology.put(1, "Venture");
        traumatology.put(2, "Kelsier");
        traumatology.put(3, "Vin");
    }

    private static void initializePhysiotherapy() {
        physiotherapy.put(1, "Potter");
        physiotherapy.put(2, "Weasley");
        physiotherapy.put(3, "Malfoy");
    }

    private static void initializeNutrition() {
        nutrition.put(1, "Neville");
        nutrition.put(2, "Baroch");
        nutrition.put(3, "Torres");
    }

    private static void initializeNeurology() {
        neurology.put(1, "Ryal");
        neurology.put(2, "Baroch");
        neurology.put(3, "Kenen");
    }

    private static void initializeCardiology() {
        cardiology.put(1, "Ryal");
        cardiology.put(2, "Lorenzo");
        cardiology.put(3, "Holmes");
    }

    private static void initializeClinicalAnalysis() {
        clinicalAnalysis.put(1, "Ryal");
        clinicalAnalysis.put(2, "Matisse");
        clinicalAnalysis.put(3, "Holmes");
    }

    private static void initializeEmergencyCare() {
        emergencyCare.put(1, "Kennen");
        emergencyCare.put(2, "Gonzalez");
        emergencyCare.put(3, "Smith");
    }

    private static void initializeGeneralMedicine() {
        generalMedicine.put(1, "Miller");
        generalMedicine.put(2, "Gonzalez");
        generalMedicine.put(3, "Smith");
    }
}


