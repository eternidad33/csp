package solution1;

import java.util.Scanner;

/**
 * 出现次数最多的数
 * @author Vigilr
 * @since 2020-07-18
 */
public class 出现次数最多的数 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        final int N = 10001;
        int[] arr1 = new int[N];
        int[] arr2 = new int[n];
        for (int i = 0; i < n; i++) {
            arr2[i] = sc.nextInt();
            arr1[arr2[i]] += 1;
        }
        int[] maxNum = {0, 0};
        for (int i = 0; i < N; i++) {
            if (arr1[i] > maxNum[1]) {
                maxNum[0] = i;
                maxNum[1] = arr1[i];
            }
        }
        System.out.println(maxNum[0]);
    }
}
