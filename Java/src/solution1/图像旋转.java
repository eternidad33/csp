package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-07-26
 */
public class 图像旋转 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] l = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                l[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(l[j][m - 1 - i] + " ");
            }
            System.out.println();
        }
    }
}
