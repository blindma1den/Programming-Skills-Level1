package org.com.level.agency;

import java.util.Map;

public class Print {
    static void printMapTravelRepetition(Map<Integer, Long> integerLongMap) {
        System.out.println(
                "::::Option::::");
        integerLongMap.forEach(
                (integer, aLong) ->
                        System.out.println(
                                "You would got tickets: " + aLong + " for: " + Agency.options.get(integer))
        );
    }
}
