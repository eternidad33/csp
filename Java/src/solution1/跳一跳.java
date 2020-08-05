package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 跳一跳 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x;
        int temp = 0;
        int sum = 0;
        while ((x = in.nextInt()) != 0) {
            // TODO 获取逐个输入
            if (x == 1) {
                sum = sum + 1;
                temp = 0;
            } else {
                temp = temp + 2;
                sum = sum + temp;
            }
        }
        System.out.println(sum);
    }
}
