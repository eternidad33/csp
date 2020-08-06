package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class 报数 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] l = new int[4];
        int i = 0;
        //记录非跳过的次数
        int counter = 0;
        //判断输入次数与记录次数是否相等
        while (counter != num) {
            i++;
            if (i % 7 == 0 || Integer.toString(i).contains("7")) {
                //甲报到的数除以4余1，乙余2，丙余3，丁没有余数
                int b = i % 4;
                l[b]++;
            } else {
                counter++;
            }
        }
        System.out.println(l[1]);
        System.out.println(l[2]);
        System.out.println(l[3]);
        System.out.println(l[0]);
    }
}
