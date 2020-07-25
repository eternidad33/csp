package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-07-25
 */
public class 门禁系统 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int count;
        for (int i = 0; i < n; i++) {
            count = 1;
            for (int j = 0; j < i; j++) {
                if (l[j] == l[i]) {
                    count++;
                }
            }
            System.out.print(count + " ");
        }
    }
}
