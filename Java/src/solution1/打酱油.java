package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-05
 */
public class 打酱油 {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int a=n/50;
        int b=(n-a*50)/30;
        int c=(n-a*50-b*30)/10;
        System.out.println(a*7+b*4+c);
    }
}
