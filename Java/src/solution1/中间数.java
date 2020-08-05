package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 中间数 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] l = new int[n];
        Boolean flag = false;
        for (int i = 0; i < n; i++) {
            l[i] = scanner.nextInt();
        }
        for (int i = 0; i < n; i++) {
            int minCount = 0, maxCount = 0;
            for (int j = 0; j < n; j++) {
                if (l[i] > l[j]) {
                    minCount++;
                } else if (l[i] < l[j]) {
                    maxCount++;
                }
            }
            if (minCount == maxCount) {
                System.out.println(l[i]);
                flag = true;
                break;
            }
        }
        if (!flag){
            System.out.println(-1);
        }
    }
}
