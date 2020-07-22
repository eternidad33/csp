package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-07-22
 */
public class 相反数 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = 0;
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = sc.nextInt();
            for (int j = 0; j < i; j++) {
                if (l[j] + l[i] == 0) {
                    s += 1;
                }
            }
        }
        System.out.println(s / 2);
    }
}
