import java.util.Scanner;

public class RetoDos {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        String season;

        while (true) {
            switch (findBucket()) {
                case 1 -> {
                    System.out.println("According to your budget, your only option is to travel during Winter");
                    defineDestination("winter");
                    System.exit(0);
                }
                case 2 -> {
                    System.out.println("In which season do you prefer to travel?");
                    System.out.println("-> Winter");
                    System.out.println("-> Autumn");
                    System.out.print("Introduce the season: ");
                    season = scanner.next();
                    defineDestination(season.toLowerCase());
                    System.exit(0);
                }
                case 3 -> {
                    System.out.println("In which season do you prefer to travel?");
                    System.out.println("-> Winter");
                    System.out.println("-> Autumn");
                    System.out.println("-> Spring");
                    System.out.print("Introduce the season: ");
                    season = scanner.next();
                    defineDestination(season.toLowerCase());
                    System.exit(0);
                }
                case 4 -> {
                    System.out.println("In which season do you prefer to travel?");
                    System.out.println("-> Winter");
                    System.out.println("-> Autumn");
                    System.out.println("-> Spring");
                    System.out.println("-> Summer");
                    System.out.print("Introduce the season: ");
                    season = scanner.next();
                    defineDestination(season.toLowerCase());
                    System.exit(0);
                }
                default -> System.out.println("YOU DID SOMETHING WRONG! TRY AGAIN!");
            }
        }

        }

        private static void defineDestination(String season){
            int option = 0;
            switch (season) {
                case "winter" -> {
                    System.out.println("1- Do you prefer skiing activities");
                    System.out.println("2- or mountain hiking");
                    System.out.print("Select your option: ");
                    option = scanner.nextInt();

                    if (option == 1) {
                        System.out.println("According to your budget and preferences, your best option is: Andorra");
                    } else if (option == 2) {
                        System.out.println("According to your budget and preferences, your best option is: Switzerland");
                    } else {
                        System.out.println("Wrong option!");
                        defineDestination(season);
                    }
                }
                case "summer" -> {
                    System.out.println("1- Do you prefer to do hiking and practice extreme sport activities");
                    System.out.println("2- or do activities on the beach?");
                    System.out.print("Select your option: ");
                    option = scanner.nextInt();

                    if (option == 1) {
                        System.out.println("According to your budget and preferences, your best option is: Spain");
                    } else if (option == 2) {
                        System.out.println("According to your budget and preferences, your best option is: Portugal");
                    } else {
                        System.out.println("Wrong option!");
                        defineDestination(season);
                    }
                }
                case "spring" -> {
                    System.out.println("1- Do you prefer to do extreme sport activities");
                    System.out.println("2- or do cultural and historical tours?");
                    System.out.print("Select your option: ");
                    option = scanner.nextInt();

                    if (option == 1) {
                        System.out.println("According to your budget and preferences, your best option is: France");
                    } else if (option == 2) {
                        System.out.println("According to your budget and preferences, your best option is: Italy");
                    } else {
                        System.out.println("Wrong option!");
                        defineDestination(season);
                    }
                }
                case "autumn" -> {
                    System.out.println("1- Do you prefer skiing activities");
                    System.out.println("2- or cultural and historical activities");
                    System.out.print("Select your option: ");
                    option = scanner.nextInt();

                    if (option == 1) {
                        System.out.println("According to your budget and preferences, your best option is: Belgium");
                    } else if (option == 2) {
                        System.out.println("According to your budget and preferences, your best option is: Austria");
                    } else {
                        System.out.println("Wrong option!");
                        defineDestination(season);
                    }
                }
            }
        }

        private static int findBucket(){
            System.out.println("Welcome to our holidays planning application!");
            System.out.print("How much money are you willing to spend (remember, minimum amount is 100$): ");
            int optionBucket = scanner.nextInt();

            if (optionBucket >= 100 && optionBucket <=199){
                optionBucket = 1;
            } else if (optionBucket >= 199 && optionBucket <= 299) {
                optionBucket = 2;
            } else if (optionBucket >= 299 && optionBucket <=399) {
                optionBucket = 3;
            } else if (optionBucket >= 399){
                optionBucket = 4;
            }

            return optionBucket;
        }
    }

