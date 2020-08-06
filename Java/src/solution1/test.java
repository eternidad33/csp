package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        if (str.contains("A")) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
