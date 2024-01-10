package org.com.level;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Manchester {
    public static final Map<String, Comparator<Player>> COMPARATOR = Map.of(
            "goals", Comparator.comparingInt(Player :: goals),
            "speed", Comparator.comparingInt(Player :: speed),
            "assists", Comparator.comparingInt(Player :: assists),
            "passing", Comparator.comparingInt(Player :: passingAccuracy),
            "defensivePlayer",
            Comparator.comparingInt(Player :: passingAccuracy)
    );
    private static Scanner scanner = new Scanner(System.in);
    private static Map<Integer, Player> manchester = Map.of(
            8, new Player("Bruno Fernandes", 5, 6, 9, 10, 3, 8),
            11, new Player("Rasmus Hojlund", 12, 8, 2, 6, 2, 11),
            5, new Player("Harry Maguire", 1, 5, 1, 7, 9, 5),
            1, new Player("Alejandro Garnacho", 8, 7, 8, 6, 0, 17),
            7, new Player("Mason Mount", 2, 6, 14, 8, 1, 7)
    );

    public static void main(String[] args) {
        var shouldContinue = true;
        while (shouldContinue) {
            printMenu();
            switch (scanner.nextInt()) {
                case 1 -> {
                    System.out.println("give the jersey number");
                    System.out.println(manchester.get(scanner.nextInt()));
                }
                case 2 -> {
                    requireData result = getRequireData();
                    var playerMap = getComparationMap(
                            result.statistics(),
                            result.player1(),
                            result.player2(),
                            COMPARATOR);
                    printComparation(playerMap);
                }
                case 3 -> printTopPlayerByStatistic("speed");
                case 4 -> printTopPlayerByStatistic("goals");
                case 5 -> printTopPlayerByStatistic("assists");
                case 6 -> printTopPlayerByStatistic("passing");
                case 7 -> printTopPlayerByStatistic("defensivePlayer");
                case 9 -> shouldContinue = false;
            }
        }
    }

    private static void printTopPlayerByStatistic(String st) {
        System.out.println(manchester.values().stream().max(COMPARATOR.get(st)).get());
    }

    private static requireData getRequireData() {
        var statistics = new ArrayList<String>();
        System.out.println("give the jersey number of player one");
        var player1 = manchester.get(scanner.nextInt());
        System.out.println("give the jersey number of player two");
        var player2 = manchester.get(scanner.nextInt());

        var shouldAksStatistic = true;
        while (shouldAksStatistic) {
            System.out.println("Select player's statistic to compare. 'Q' to stop");
            String next = scanner.next().toLowerCase(Locale.ROOT);
            shouldAksStatistic = (! next.equals("q")) && statistics.add(next);
        }
        return new requireData(statistics, player1, player2);
    }

    private record requireData(
            ArrayList<String> statistics, Player player1, Player player2
    ) {}

    private static Map<String, Player> getComparationMap(ArrayList<String> statistics,
                                                         Player player1, Player player2
            , Map<String, Comparator<Player>> comparator) {
        return statistics
                .stream()
                .map(comparatorFromStatisticToStaAndPlayer(player1, player2, comparator))
                .collect(makeAMap());
    }

    private static void printComparation(Map<String, Player> list) {
        list.forEach((key, player) -> System.out.println("Statistic: " + key + " Player" +
                                                         ":" + player.name()));
    }

    private static Collector<Map.Entry<String, Player>, ?, Map<String, Player>> makeAMap() {
        return Collectors.toMap(Map.Entry :: getKey, Map.Entry :: getValue);
    }

    private static Function<String, Map.Entry<String, Player>> comparatorFromStatisticToStaAndPlayer(Player player1, Player player2, Map<String, Comparator<Player>> comparator) {
        return st -> Map.entry(st,
                Stream.of(player1, player2).max(comparator.get(st)).get());
    }

    private static void printMenu() {
        System.out.println("1) Show player characteristics by Jersey Number");
        System.out.println("2) Compare two players");
        System.out.println("3) Show the fastest player");
        System.out.println("4) Show the top goal scorer");
        System.out.println("5) Show the player with most assist");
        System.out.println("6) Show the highest passing accuracy");
        System.out.println("7) Show the better defense player");
        System.out.println("8) to exit...!");
    }

    public static Player searchBy(String characteristic, int comparator) {
        Map<String, Predicate<Player>> playerMap = Map.of(
                "goals", player -> player.goals().equals(comparator),
                "speed", player -> player.speed().equals(comparator),
                "assists", player -> player.assists().equals(comparator),
                "accurate", player -> player.passingAccuracy().equals(comparator),
                "defensivePlayer", player -> player.defensive().equals(comparator)
        );
        return manchester
                .values()
                .stream()
                .filter(playerMap.get(characteristic))
                .findFirst()
                .orElseGet(() -> new Player("", 0, 0, 0, 0, 0, 0));
    }
}
