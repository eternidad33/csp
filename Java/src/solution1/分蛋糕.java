package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 分蛋糕 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int[] l = new int[n];
        int count = 0, weight = 0;
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
            weight += l[i];
            if (weight >= k) {
                count++;
                weight = 0;
            }
        }
        if (weight != 0) {
            count++;
        }
        System.out.println(count);
    }
}
