package solution1;

import java.util.Scanner;

/**
 * @author Vigilr
 * @since 2020-08-06
 */
public class 线性分类器 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        //data存储坐标，type存取对应的类型
        int[][] data = new int[n][2];
        char[] type = new char[n];
        for (int i = 0; i < n; i++) {
            data[i][0] = scanner.nextInt();
            data[i][1] = scanner.nextInt();
            type[i] = scanner.next().charAt(0);
        }

        //line存取直线上的每个参数，results存取直线是否满足条件
        int[] line = new int[3];
        boolean[] results = new boolean[m];

        //up是指A类型是否在直线上方
        boolean up = true;

        for (int i = 0; i < m; i++) {
            //获取每条直线三个参数的输入
            for (int j = 0; j < 3; j++) {
                line[j] = scanner.nextInt();
            }

            //判断第一个点在直线的位置
            int result = line[0] + (line[1] * data[0][0]) + (line[2] * data[0][1]);
            if (type[0] == 'A' && result > 0) {
                up = true;
            } else if (type[0] == 'B' && result < 0) {
                up = true;
            } else {
                up = false;
            }

            //从第二个点开始判断
            for (int k = 1; k < n; k++) {
                result = line[0] + (line[1] * data[k][0]) + (line[2] * data[k][1]);
                if (up) {
                    if (type[k] == 'A' && result > 0) {
                        results[i] = true;
                    } else if (type[k] == 'A' && result < 0) {
                        results[i] = false;
                        break;
                    } else if (type[k] == 'B' && result > 0) {
                        results[i] = false;
                        break;
                    } else if (type[k] == 'B' && result < 0) {
                        results[i] = true;
                    }
                } else {
                    if (type[k] == 'A' && result > 0) {
                        results[i] = false;
                        break;
                    } else if (type[k] == 'A' && result < 0) {
                        results[i] = true;
                    } else if (type[k] == 'B' && result > 0) {
                        results[i] = true;
                    } else if (type[k] == 'B' && result < 0) {
                        results[i] = false;
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < m; i++) {
            if (results[i]) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}

//9 3
//1 1 A
//1 0 A
//1 -1 A
//2 2 B
//2 3 B
//0 1 A
//3 1 B
//1 3 B
//2 0 A
//0 2 -3
//-3 0 2
//-3 1 1

class Main {
    public static void main(String[] args) {
        //1.1  接收数据 n和m
        int n, m;
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        //System.out.println(n);

        //1.2 接收点的坐标数据 和 对应分类
        int[][] datas = new int[n][2];
        char[] types = new char[n];
        for (int i = 0; i < n; i++) {
            datas[i][0] = scan.nextInt();    //横坐标
            datas[i][1] = scan.nextInt();    //纵坐标
            types[i] = scan.next().charAt(0);    //types
        }
        //1.3 创建theta[]，保存每次直线的参数
        int[] theta = new int[3];

        //1.4 创建outcome[], 保存分类的结果
        boolean[] outcome = new boolean[m];

        //2. 不断接收参数，然后计算 --> 判断 --> 分类 --> 设置结果
        boolean AisUp = true;    //标签为A的点通过计算结果是否大于0
        for (int i = 0; i < m; i++) {
            //2.1 接收这次分类的直线数据
            for (int j = 0; j < 3; j++) {
                theta[j] = scan.nextInt();
            }

            //2.2 使用这条直线对n个点进行分类
            //2.2.1  先对第一个点进行计算，判断A、B标签应该在直线哪一侧
            int result = theta[0] + (theta[1] * datas[0][0]) + (theta[2] * datas[0][1]);
            //2.2.2 依据 结果 和 type 对 A 、 B 进行分侧
            if (types[0] == 'A') {
                if (result > 0) {
                    AisUp = true;    //A标签的点结果大于0
                } else {
                    AisUp = false;    //A标签的点结果小于0
                }
            } else if (types[0] == 'B') {
                if (result > 0) {
                    AisUp = false;    //B标签的点结果大于0
                } else {
                    AisUp = true;    //B标签的点结果小于0
                }
            }
            //2.2.3 从第二个点开始处理
            for (int k = 1; k < n; k++) {
                //2.2.3.1 将点的坐标代入直线方程，计算结果
                result = theta[0] + (theta[1] * datas[k][0]) + (theta[2] * datas[k][1]);
                //2.2.3.2 判断是否分类正确
                if (AisUp) {    //A标签的数据>0
                    if ((types[k] == 'A') && (result > 0)) {
                        //则分类正确
                        outcome[i] = true;    //设置为true
                    } else if ((types[k] == 'A') && (result < 0)) {
                        //分类错误
                        outcome[i] = false;    //设置为false
                        break;    //已经分类错误了，不用再去计算剩余数据
                    } else if ((types[k] == 'B') && (result > 0)) {
                        //分类错误
                        outcome[i] = false;
                        break;
                    } else if ((types[k] == 'B') && (result < 0)) {
                        //分类正确
                        outcome[i] = true;
                    }
                } else {    //A标签的数据<0
                    if ((types[k] == 'A') && (result > 0)) {
                        //则分类错误
                        outcome[i] = false;    //设置为false
                        break;    //已经分类错误了，不用再去计算剩余数据
                    } else if ((types[k] == 'A') && (result < 0)) {
                        //分类正确
                        outcome[i] = true;    //设置为true
                    } else if ((types[k] == 'B') && (result > 0)) {
                        //分类正确
                        outcome[i] = true;
                    } else if ((types[k] == 'B') && (result < 0)) {
                        //分类错误
                        outcome[i] = false;
                        break;
                    }
                }
            }
        }

        //3. 输出结果
        for (int i = 0; i < m; i++) {
            if (outcome[i]) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}
