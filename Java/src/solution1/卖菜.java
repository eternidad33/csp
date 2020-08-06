package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class 卖菜 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        int[] newList = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                newList[i] = (l[0] + l[1]) / 2;
            } else if (i == n - 1) {
                newList[i] = (l[n - 1] + l[n - 2]) / 2;
            } else {
                newList[i] = (l[i - 1] + l[i] + l[i + 1]) / 3;
            }
        }
        for (int num : newList) {
            System.out.print(num + " ");
        }
    }
}
