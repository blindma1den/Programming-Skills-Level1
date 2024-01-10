import java.util.HashMap;

public class Main {

    private static final HashMap<Integer, Player> players = new HashMap<>();
    public static void main(String[] args) {

        players.put(8,new Player("Fernando", 1, 1, 10, 20,50));

        System.out.println(players);
    }
}