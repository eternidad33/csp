package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-07-25
 */
public class 相邻数对 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int count = 0;
        for (int i : l) {
            for (int j : l) {
                if (i - j == 1) {
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
