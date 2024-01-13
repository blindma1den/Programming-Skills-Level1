package org.com.level.hospital;

import java.util.List;

public class Printer {
    static <T> int printOptions(List<T> options) {
        var repeat = true;
        var optionNumber = - 1;
        while (repeat) {
            for (int i = 0; i < options.size(); i++) {
                System.out.println(i + ") para " + options.get(i));
            }
            optionNumber = Main.scanner.nextInt();
            repeat = ! (optionNumber >= 0 && optionNumber <= options.size());
            if (repeat) {
                System.out.println("Elegiste una option invalida intentalo de nuevo");
            }
        }
        return optionNumber;
    }
}
