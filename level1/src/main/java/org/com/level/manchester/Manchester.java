package org.com.level.manchester;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Supplier;

import static org.com.level.manchester.Printer.printComparative;
import static org.com.level.manchester.Printer.printMenu;
import static org.com.level.manchester.Printer.print;
import static org.com.level.manchester.Printer.printTopPlayerByStatistic;

public class Manchester {
    private static final Scanner scanner = new Scanner(System.in);
    static final Map<Integer, Player> manchester = Map.of(
            8, new Player("Bruno Fernandes", 5, 6, 9, 10, 3, 8),
            11, new Player("Rasmus Hojlund", 12, 8, 2, 6, 2, 11),
            5, new Player("Harry Maguire", 1, 5, 1, 7, 9, 5),
            1, new Player("Alejandro Garnacho", 8, 7, 8, 6, 0, 17),
            7, new Player("Mason Mount", 2, 6, 14, 8, 1, 7)
    );

    public static void main(String[] args) {
        repeat(Manchester::statisticsProcess);
    }

    private static boolean statisticsProcess() {
        printMenu();
        switch (scanner.nextInt()) {
            case 1 -> {
                print("give the jersey number");
                print(getPlayer());
            }
            case 2 -> {
                var results = compareTwoPlayers();
                printComparative(results);
            }
            case 3 -> printTopPlayerByStatistic("speed");
            case 4 -> printTopPlayerByStatistic("goals");
            case 5 -> printTopPlayerByStatistic("assists");
            case 6 -> printTopPlayerByStatistic("passing");
            case 7 -> printTopPlayerByStatistic("defensivePlayer");
            case 9 -> {return false;}
        }
        return true;
    }

    private static Map<String, Player> compareTwoPlayers() {
        var selected = getRequireData();
        return Player
                .getComparativeFor(selected.statistics(),
                        selected.player1(),
                        selected.player2());
    }

    private static Player getPlayer() {
        return manchester.get(scanner.nextInt());
    }

    private static SubmitedData getRequireData() {
        var statistics = new ArrayList<String>();
        print("give the jersey number of player one");
        var player1 = getPlayer();
        print("give the jersey number of player two");
        var player2 = getPlayer();
        repeat(
                () -> {
                    print("Select player's statistic to compare. 'Q' to stop");
                    String next = scanner.next().toLowerCase(Locale.ROOT);
                    return (! next.equals("q")) && statistics.add(next);
                }
        );
        return new SubmitedData(statistics, player1, player2);
    }

    private static void repeat(Supplier<Boolean> fun) {
        var shouldContinue = true;
        while (shouldContinue) {
            shouldContinue = fun.get();
        }
    }

    private record SubmitedData(
            ArrayList<String> statistics, Player player1, Player player2
    ) {}
}
