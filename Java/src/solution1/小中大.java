package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class 小中大 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int max, min;
        double middle = 0.0;
        if (l[n - 1] > l[0]) {
            max = l[n - 1];
            min = l[0];
        } else {
            max = l[0];
            min = l[n - 1];
        }
        if (n % 2 != 0) {
            middle = l[(n - 1) / 2];
            System.out.print(max + " " + (int) middle + " " + min);
        } else {
            double sum = 0.0;
            sum = l[n / 2] + l[n / 2 - 1];
            middle = sum / 2;
            if ((middle - (int) middle) == 0) {
                System.out.print(max + " " + (int) middle + " " + min);
            } else {
                System.out.print(max + " " + middle + " " + min);
            }
        }
    }
}
