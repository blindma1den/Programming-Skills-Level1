import java.util.HashMap;
import java.util.Scanner;

public class Main {
    private static final HashMap<Integer, Player> players = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws InterruptedException {
        initializePlayers();

        while (true){
            switch (mainMenu()){
                case 1 -> {
                    playerReview();
                    Thread.sleep(2000);
                }
                case 2 -> {
                    playerCompare();
                    Thread.sleep(2000);
                }
                case 3 -> {
                    fastestPlayer();
                    Thread.sleep(2000);
                }
                case 4 -> {
                    topGoalPlayer();
                    Thread.sleep(2000);
                }
                case 5 -> {
                    mostAssistsPlayer();
                    Thread.sleep(2000);
                }
                case 6 -> {
                    highestPassingPlayer();
                    Thread.sleep(2000);
                }
                case 7 -> {
                    mostDefensivePlayer();
                    Thread.sleep(2000);
                }
                case 8 -> {
                    System.exit(0);
                }
                default -> {
                    System.out.println("Wrong Option!");
                }
            }
        }
    }

    private static void mostDefensivePlayer() {
        Player topDefensivePlayer = null;
        int defence = -1;

        for(Player player: players.values()){
            if (player.getDefence() > defence){
                topDefensivePlayer = player;
                defence = topDefensivePlayer.getDefence();
            }
        }

        System.out.println("The top Defensive Involvements is: "+ topDefensivePlayer.getNAME() + " and his/her attribute value is: "+ topDefensivePlayer.getDefence());
    }

    private static void highestPassingPlayer() {
        Player topPassingAccuracyPlayer = null;
        int passingAccuracy = -1;

        for(Player player: players.values()){
            if (player.getAccuracy() > passingAccuracy){
                topPassingAccuracyPlayer = player;
                passingAccuracy = topPassingAccuracyPlayer.getAccuracy();
            }
        }

        System.out.println("The top Passing Accuracy is: "+ topPassingAccuracyPlayer.getNAME() + " and his/her attribute value is: "+ topPassingAccuracyPlayer.getAccuracy());
    }

    private static void mostAssistsPlayer() {
        Player topPlayerAssistant = null;
        int assists = -1;

        for(Player player: players.values()){
            if (player.getAssists() > assists){
                topPlayerAssistant = player;
                assists = topPlayerAssistant.getAssists();
            }
        }

        System.out.println("The top Assistant is: "+ topPlayerAssistant.getNAME() + " and his/her attribute value is: " + topPlayerAssistant.getAssists());
    }

    private static void topGoalPlayer() {

        Player topScorerPlayer = null;
        int scorer = -1;

        for(Player player: players.values()){
            if (player.getGoals() > scorer){
                topScorerPlayer = player;
                scorer = topScorerPlayer.getGoals();
            }
        }

        System.out.println("The top Scorer is: "+ topScorerPlayer.getNAME() + " and his/her attribute value is: "+ topScorerPlayer.getGoals());

    }

    private static void fastestPlayer() {
        Player playerFastest = null;
        int fastest = -1;

        for(Player player: players.values()){
            if (player.getSpeed() > fastest){
                playerFastest = player;
                fastest = playerFastest.getSpeed();
            }
        }

        System.out.println("The Fastest player is: "+ playerFastest.getNAME() + " and his/her attribute value is: "+ playerFastest.getSpeed());
        
    }

    private static void playerCompare() {
        System.out.print("Introduce the first Jersey Number: ");
        int jerseyNumber1 = scanner.nextInt();
        System.out.print("Introduce the second Jersey Number: ");
        int jerseyNumber2 = scanner.nextInt();

        Player player1 = players.get(jerseyNumber1);
        Player player2 = players.get(jerseyNumber2);

        if(player1 != null && player2 != null){
            System.out.println("*------------Player Compare------------*");
            System.out.println("The Player with the Jersey number: " + jerseyNumber1 + " has the following statistics:");
            System.out.println(players.get(jerseyNumber1));
            System.out.println("The Player with the Jersey number: " + jerseyNumber2 + " has the following statistics:");
            System.out.println(players.get(jerseyNumber2));
        }else {
            System.out.println("Players not Found. Try again!");
        }
    }

    private static void playerReview() {
        System.out.print("Introduce the Jersey Number: ");
        int jerseyNumber = scanner.nextInt();

        if (players.get(jerseyNumber) != null){
            System.out.println("The Player with the Jersey number: " + jerseyNumber + " has the following statistics:");
            System.out.println(players.get(jerseyNumber));
        } else {
            System.out.println("Player not Found. Try again!");
        }
    }

    private static int mainMenu(){

        System.out.println("*------------Welcome to the statistic tool, chose your option------------*");
        System.out.println("1 - Player Review");
        System.out.println("2 - Players Comparation");
        System.out.println("3 - Fastest Player");
        System.out.println("4 - TopGoal Player");
        System.out.println("5 - TopAssistant Player");
        System.out.println("6 - TopPassing Player");
        System.out.println("7 - TopDefensive Player");
        System.out.println("8 - Exit");
        System.out.print("Select your option: ");

        return scanner.nextInt();
    }
    private static void initializePlayers(){
        players.put(8,new Player("Bruno Fernandes", 5, 6, 9,10,3));
        players.put(11,new Player("Rasmus Hojlund",12,8,2,6,2));
        players.put(5,new Player("Harry Maguire",1,5,1,7,9));
        players.put(17,new Player("Alejandro Garnacho",8,7,8,6,0));
        players.put(7,new Player("Mason Mount",2,6,4,8,1));
    }
    
    
}