package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 折点计数 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int count = 0;
        for (int i = 1; i < n - 1; i++) {
            if (l[i] > l[i - 1]) {
                count += l[i] > l[i + 1] ? 1 : 0;
            } else {
                count += l[i] < l[i + 1] ? 1 : 0;
            }
        }
        System.out.println(count);
    }
}
