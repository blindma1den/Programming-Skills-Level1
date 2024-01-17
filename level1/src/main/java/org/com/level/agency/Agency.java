package org.com.level.agency;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Agency {
    static Scanner scanner = new Scanner(System.in);
    static Map<Integer, String> options = Map.of(100, "Winter", 200, "Summer", 500,
                                                 "Spring", 1000, "Autumn");
    static List<Integer> priceTravels = options.keySet().stream().sorted().toList();

    public static void main(String[] args) {
        System.out.println("write your budget..");
        var budget = scanner.nextInt();
        System.out.println("Possible Travel for budget: ");
        findPossiblesCombinations(new HashSet<>(), priceTravels, budget)
                .stream()
                .map(Agency :: getMapPriceAndRepetitions)
                .forEach(Print :: printMapTravelRepetition);
    }

    private static Map<Integer, Long> getMapPriceAndRepetitions(List<Integer> integers) {
        return integers.stream()
                       .distinct()
                       .collect(Collectors.toMap(
                               integer -> integer,
                               integer -> integers.stream()
                                                  .filter(integer1 -> integer1.equals(integer))
                                                  .count()
                       ));
    }

    public static HashSet<List<Integer>> findPossiblesCombinations(HashSet<List<Integer>> results,
                                                                   List<Integer> optionsCopy,
                                                                   Integer budget) {
        if (optionsCopy.isEmpty()) {return results;}
        results.add(getOptionsFor(budget, optionsCopy, new ArrayList<>()));
        return findPossiblesCombinations(results,
                                         optionsCopy.subList(0, optionsCopy.size() - 1),
                                         budget);

    }

    public static List<Integer> getOptionsFor(Integer budget,
                                              List<Integer> optionsPrices,
                                              List<Integer> possibleTravels) {
        Integer lastTravelPrice = optionsPrices.getLast();
        if (budget >= 0 && budget < optionsPrices.getFirst()) {
            return possibleTravels;
        } else if (budget - lastTravelPrice >= 0) {
            possibleTravels.add(lastTravelPrice);
            return getOptionsFor(budget - lastTravelPrice,
                                 optionsPrices,
                                 possibleTravels);
        } else {
            return getOptionsFor(budget,
                                 optionsPrices.stream()
                                              .filter(integer -> ! integer.equals(lastTravelPrice))
                                              .toList(),
                                 possibleTravels);
        }
    }
}
