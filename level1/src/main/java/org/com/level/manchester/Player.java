package org.com.level.manchester;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public record Player (String name,
                      Integer goals,
                      Integer speed,
                      Integer assists,
                      Integer passingAccuracy,
                      Integer defensive,
                      Integer jerseyNumber)
{
    public static final Map<String, Comparator<Player>> COMPARATORS = Map.of(
            "goals", Comparator.comparingInt(Player :: speed),
            "speed", Comparator.comparingInt(Player :: speed),
            "assists", Comparator.comparingInt(Player :: assists),
            "passing", Comparator.comparingInt(Player :: passingAccuracy),
            "defensivePlayer", Comparator.comparingInt(Player :: passingAccuracy));

    static Map<String, Player> getComparativeFor(ArrayList<String> statistics,
                                                 Player player1, Player player2) {
        return statistics
                .stream()
                .map(comparePlayers(player1, player2))
                .collect(Collectors.toMap(Map.Entry :: getKey, Map.Entry :: getValue));
    }

    private static Function<String, Map.Entry<String, Player>> comparePlayers(Player player1, Player player2) {
        return st -> Map.entry(st, Stream.of(player1, player2).max(COMPARATORS.get(st)).get());
    }
}
