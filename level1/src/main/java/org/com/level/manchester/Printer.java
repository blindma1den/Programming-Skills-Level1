package org.com.level.manchester;

import java.util.Map;

public class Printer {

    static void printMenu() {
        System.out.println("1) Show player characteristics by Jersey Number");
        System.out.println("2) Compare two players");
        System.out.println("3) Show the fastest player");
        System.out.println("4) Show the top goal scorer");
        System.out.println("5) Show the player with most assist");
        System.out.println("6) Show the highest passing accuracy");
        System.out.println("7) Show the better defense player");
        System.out.println("8) to exit...!");
    }

    static void printComparative(Map<String, Player> list) {
        list.forEach((key, player) -> System.out.println("Statistic: " + key + " Player" +
                                                         ":" + player.name()));
    }

    static void printTopPlayerByStatistic(String st) {
        Player player = Manchester.manchester.values().stream().max(Player.COMPARATORS.get(st)).get();
        System.out.println(player);
    }

    static <T> void print(T x) {
        System.out.println(x);
    }
}
