package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 数位之和 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            count += str.charAt(i) - '0';
        }
        System.out.println(count);
    }
}
