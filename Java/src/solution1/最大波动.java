package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 最大波动 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int max = 0;
        for (int i = 1; i < n; i++) {
            max = Math.max(Math.abs(l[i - 1] - l[i]), max);
        }
        System.out.println(max);
    }
}
