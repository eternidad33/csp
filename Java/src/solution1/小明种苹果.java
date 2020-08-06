package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class 小明种苹果 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int max = -1, T = 0, k = 0, P = 0;
        int[][] a = new int[N][M + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M + 1; j++) {
                a[i][j] = scanner.nextInt();
                T += a[i][j];
            }
        }
        for (int i = 0; i < N; i++) {
            int sum = 0;
            //从每一行的第二个开始加
            for (int j = 1; j < M + 1; j++) {
                sum += Math.abs(a[i][j]);
                //如果一行的蔬果数大于最大数，把值赋给最大数
                if (sum > max) {
                    max = sum;
                    P = max;
                    //最大蔬果数的行数加一
                    k = i + 1;
                }
            }
        }
        System.out.println(T + " " + k + " " + P);
    }
}
