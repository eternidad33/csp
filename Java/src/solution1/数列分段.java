package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 数列分段 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        int count = 1;
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
            if (i != 0 && l[i] != l[i - 1]) {
                count++;
            }
        }
        System.out.println(count);
    }
}
