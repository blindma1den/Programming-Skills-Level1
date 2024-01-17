
package org.com.level.hospital;

import java.util.Scanner;
import java.util.function.BiPredicate;


public class Authenticator {
    private Scanner scanner = new Scanner(System.in);
    public Boolean isLogged = false;

    void shouldLogOut() {
        System.out.println("Do you want to continue? ");
        String next = scanner.next();
        if (next.equalsIgnoreCase("no")) {
            Main.authenticator.isLogged = false;
        }
    }

    private void printMessage(String x) {
        System.out.println(x);
    }

    public void authProcessFor(int tries,
                               User user) {
        var isLoged = false;
        while (! isLoged && tries > 0) {
            isLoged = authLogic().test(user.password(), user.name());
            if(!isLoged){
                printMessage("you still have " + (tries - 1) + " tries left");
                tries--;
            }
        }
        isLogged = isLoged;
        authMessage();
    }


    private BiPredicate<String, String> authLogic() {
        return (passwordP, userNameP) -> {
            printMessage("Enter User Name");
            var userName = scanner.next();
            printMessage("Enter Password");
            var password = scanner.next();
            return userName.equals(userNameP) && password.equals(passwordP);
        };
    }

    private void authMessage() {
        if (! isLogged) {
            printMessage("Sorry, max try possible");
        } else {
            printMessage("Welcome ");
        }
    }
}
