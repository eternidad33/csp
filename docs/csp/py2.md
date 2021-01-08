[![Jupyter Notebook预览](https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/upyter%E9%A2%84%E8%A7%88.png)](https://nbviewer.jupyter.org/github/eternidad33/csp/blob/master/Python/题解汇总/第2题题解汇总.ipynb)

# 目录

- [ISBN号码](#ISBN号码)
- [窗口](#窗口)
- [画图](#画图)
- [Z字形扫描](#Z字形扫描)
- [数字排序](#数字排序)
- [日期计算](#日期计算)
- [消除类游戏](#消除类游戏)
- [俄罗斯方块](#俄罗斯方块)
- [火车购票](#火车购票)
- [工资计算](#工资计算)
- [学生排队](#学生排队)
- [公共钥匙盒](#公共钥匙盒)
- [游戏](#游戏)
- [碰撞的小球](#碰撞的小球)
- [买菜](#买菜)
- [小明放学](#小明放学)
- [二十四点](#二十四点)
- [小明种苹果续](#小明种苹果续)
- [回收站选址](#回收站选址)
- [稀疏向量](#稀疏向量)
- [风险人群筛查](#风险人群筛查)

## ISBN号码

试题编号：	201312-2  
试题名称：	ISBN号码

[返回目录](#目录)


```python
def backlist(s):
    '''将字符串提取为整型数组'''
    rlist = []
    for i in s:
        if i.isdigit():
            rlist.append(int(i))
    return rlist


# s = input()
s= "0-670-82162-4"
l = backlist(s)
sum = 0
for i in range(9):
    sum += l[i] * (i + 1)
code = sum % 11
if s[-1] == str(code) or (s[-1] == 'X' and code == 10):
    print("Right")
else:
    if code == 10:
        s = s[:-1] + 'X'
    else:
        s = s[:-1] + str(code)
    print(s)
```

    Right
    

## 窗口

试题编号：	201403-2  
试题名称：	窗口

[返回目录](#目录)


```python
def chuangkou(window, point_x, point_y):
    """识别窗口"""
    global i, j
    find = False
    for i, s in reversed(list(enumerate(window))):
        if s[0] <= point_x <= s[2] and s[1] <= point_y <= s[3]:
            print(s[4])
            last = window[i]
            for j in range(i, len(window) - 1):
                window[j] = window[j + 1]
            window[-1] = last
            find = True
            break
    if not find:
        print('IGNORED')


# 录入数据
# n, m = map(int, input().split())
# w = []
# for i in range(n):
#     w.append(list(map(int, input().split())))
#     w[i].append(i + 1)
# for j in range(m):
#     x, y = list(map(int, input().split()))
#     chuangkou(w, x, y)
```

## 画图

试题编号：	201409-2  
试题名称：	画图

[返回目录](#目录)


```python
def huaTu():
    n = int(input())
    pnum = [[0] * 100 for _ in range(100)]
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                # 将被覆盖的区域置为1
                pnum[x][y] = 1
    area = 0
    for i in range(100):
        area += sum(pnum[i])
    print(area)


# huaTu()
```

## Z字形扫描

试题编号：	201412-2  
试题名称：	Z字形扫描

[返回目录](#目录)


```python
def z(m, num):
    # up用于存储是否向上遍历，默认向上遍历
    up = True
    line = []
    i, j = 0, 0
    for _ in range(m * m):
        line.append(num[i][j])
        # 处理向上移动
        if up:
            # 处理碰到右边界，下移
            if j == m - 1:
                i += 1
                up = False
            # 处理碰到上边界，右移
            elif i == 0:
                j += 1
                up = False
            # 其他情况，右上
            else:
                j += 1
                i -= 1
        else:
            if i == m - 1:
                j += 1
                up = True
            elif j == 0:
                i += 1
                up = True
            else:
                j -= 1
                i += 1
    print(" ".join(map(str, line)))


# n = int(input())
# pnum = []
# for i in range(n):
#     pnum.append(list(map(int, input().split())))
# z(n, pnum)
```

## 数字排序

试题编号：	201503-2  
试题名称：	数字排序

[返回目录](#目录)


```python
def shuZiPaiXu(nums):
    nums.sort()
    a = {}
    for i in nums:
        a[i] = nums.count(i)
    # 排序
    a = sorted(a.items(), key=lambda item: item[1], reverse=True)
    for j in a:
        print(j[0], j[1])


# n = int(input())
# ls = list(map(int, input().split()))
# shuZiPaiXu(ls)
```

## 日期计算

试题编号：	201509-2  
试题名称：	日期计算

[返回目录](#目录)


```python
def riQiJiSuan(year, day):
    mon = 0
    md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 判断闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        md[2] = 29
    for i in md:
        if day - i > 0:
            day -= i
            mon += 1
        else:
            break
    print(mon)
    print(day)


# y = int(input())
# d = int(input())
# riQiJiSuan(y, d)
```

## 消除类游戏

试题编号：	201512-2  
试题名称：	消除类游戏

[返回目录](#目录)


```python
def xiaoChuLeiYouXi(A, n, m):
    # B中元素为1，代表在A中连续
    B = [[0] * m for _ in range(n)]
    global i
    for i in range(n):
        for j in range(m):
            # 竖排三个相同
            if 0 < i < n - 1 and A[i - 1][j] == A[i][j] and A[i][j] == A[i + 1][j]:
                B[i - 1][j] = 1
                B[i][j] = 1
                B[i + 1][j] = 1
            # 横排三个相同
            if 0 < j < m - 1 and A[i][j - 1] == A[i][j] and A[i][j] == A[i][j + 1]:
                B[i][j - 1] = 1
                B[i][j] = 1
                B[i][j + 1] = 1
    for i in range(n):
        for j in range(m):
            if B[i][j] == 1:
                A[i][j] = 0
            print(A[i][j], end=" ")
        print()


# n, m = map(int, input().split())
# lm = []
# for i in range(n):
#     lm.append(list(map(int, input().split())))
# xiaoChuLeiYouXi(lm, n, m)
```

## 俄罗斯方块

试题编号：	201604-2  
试题名称：	俄罗斯方块

[返回目录](#目录)


```python
def eLuoSiFangKuai(tmap, shape, x):
    global i, j
    # 将形状转换为4行10列
    for i in range(4):
        shape[i] = [0] * (x - 1) + shape[i] + [0] * (6 - (x - 1))
    # 图形第一行最终落到的方格图对应的行数
    row1 = 0
    find = False
    for i in range(3):
        tmap.append([1] * 10)
    for i in range(15):
        for j in range(4):
            newline = [a + b for a, b in zip(tmap[i + j], shape[j])]
            if 2 in newline:
                row1 = i - 1
                find = True
                break
        if find:
            break
        if i == 14:
            row1 = 14
    # 拼接数据
    for i in range(4):
        tmap[row1 + i] = [a + b for a, b in zip(tmap[row1 + i], shape[i])]
    # 输出数据
    for i in range(15):
        print(' '.join(map(str, tmap[i])))


# # 录入数据
# tmap, shape = [], []
# for i in range(15):
#     temp_a = list(map(int, input().split()))
#     tmap.append(temp_a)
# for j in range(4):
#     temp_b = list(map(int, input().split()))
#     shape.append(temp_b)
# x = int(input())
# eLuoSiFangKuai(tmap, shape, x)
```

## 火车购票

试题编号：	201609-2  
试题名称：	火车购票

[返回目录](#目录)


```python
def huoCheGouPiao(count, l):
    """火车购票

    思路：开辟一个二维数组存取剩余座位号
    """
    num = []  # 存座位号
    # 为num编号
    for i in range(20):
        temp = []
        for j in range(5):
            temp.append(i * 5 + j + 1)
        num.append(temp)

    seats = [5 for i in range(20)]  # 每一行的剩余座位
    p = -1  # 哪一行的座位数够用
    res = [[] for i in range(count)]  # 存取最后结果
    a = 0  # res的下标
    for i in l:
        for j in range(20):
            if seats[j] >= i:
                p = j
                break
        if p != -1:
            for k in range(5):
                if i == 0:
                    break
                if num[p][k] != 0:
                    res[a].append(num[p][k])
                    num[p][k] = 0
                    seats[p] -= 1
                    i -= 1
            a += 1
        else:
            # 找不到行数，则应该安排在编号最小的几个空座位中（不考虑是否相邻）
            for j in range(20):
                for k in range(5):
                    if i == 0:
                        a += 1
                        break
                    if num[j][k] != 0:
                        res[a].append(num[j][k])
                        num[j][k] = 0
                        seats[j] -= 1
                        i -= 1
                if i == 0:
                    break
        p = -1
    for i in res:
        for j in i:
            print(j, end=' ')
        print()


# n = int(input())
# m = list(map(int, input().split()))
# huoCheGouPiao(n, m)
```

## 工资计算

试题编号：	201612-2  
试题名称：	工资计算

[返回目录](#目录)


```python
t = 9255
# t = int(input())
rate = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
sA = [0, 1500, 4500, 9000, 35000, 55000, 80000, 100000]
afterTax = [3500]  # 税后工资
sum0 = 0
for i in range(1, len(sA)):
    sum0 += int((sA[i] - sA[i - 1]) * (1 - rate[i]))
    afterTax.append(sum0 + 3500)
if t <= 3500:
    s = t
else:
    for i in range(len(afterTax)):
        if afterTax[i] < t <= afterTax[i + 1]:
            s = 3500 + sA[i]
            s += int((t - afterTax[i]) / (1 - rate[i + 1]))
            # 保证小明的税前工资为一个整百的数
            s = 100 * (round(s / 100))
            break
print(s)
```

    10000
    

## 学生排队

试题编号：	201703-2  
试题名称：	学生排队

[返回目录](#目录)


```python
def 学生排队():
    n = int(input())
    q = list(range(1, n + 1))
    m = int(input())
    for i in range(m):
        k, t = map(int, input().split())
        after = q.index(k) + t  # 移动后的索引
        q.remove(k)  # 删除
        q.insert(after, k)  # 插入
    print(' '.join(map(str, q)))


# 学生排队()
```

## 公共钥匙盒

试题编号：	201709-2  
试题名称：	公共钥匙盒

[返回目录](#目录)


```python
def return_lend_key(key_info, times, time):
    """time在times借用或者归还的钥匙"""
    RL_key = []
    for i in range(len(times)):
        if times[i] == time:
            RL_key.append(key_info[i][0])
    return RL_key


def 公共钥匙盒(key_len, key_info):
    global i
    key = list(range(1, key_len + 1))
    # 分别存储开始使用时间和归还时间
    start_time = [i[1] for i in key_info]
    end_time = [i[1] + i[2] for i in key_info]
    for t in range(1, max(end_time) + 1):
        # 先还后借
        # t时刻为归还时间
        if t in end_time:
            return_key = return_lend_key(key_info, end_time, t)
            return_key.sort()
            for r in return_key:
                for i in range(key_len):
                    if key[i] == 0:
                        key[i] = r
                        break
        # t时刻为借用时间
        if t in start_time:
            lend_key = return_lend_key(key_info, start_time, t)
            for r in lend_key:
                for i in range(key_len):
                    if key[i] == r:
                        key[i] = 0
    print(' '.join(map(str, key)))


# n, k = map(int, input().split())
# info = []
# for i in range(k):
#     info.append(list(map(int, input().split())))
# 公共钥匙盒(n, info)
```

## 游戏

试题编号：	201712-2  
试题名称：	游戏

[返回目录](#目录)


```python
n, k = 5, 2
# n, k = map(int, input().split())
a = list(range(1, n + 1))
num = 1
while len(a) > 0:
    key_del = []
    # key_del存储要删除元素的索引
    for key, value in enumerate(a):
        # key存储的是a的索引
        if num % k == 0 or num % 10 == k:
            key_del.append(key)
        num += 1
    ac = 0
    # 由于删除元素列表的索引会跟随变化
    # ac存储的是删除元素的个数
    for key in key_del:
        del a[key - ac]
        ac += 1
        if len(a) == 1:
            print(a[0])
```

    3
    

## 碰撞的小球

试题编号：	201803-2  
试题名称：	碰撞的小球

[返回目录](#目录)


```python
def 碰撞的小球(count, axis_len, time, position):
    dire = [1] * count  # 存储运动方向
    for ti in range(time):
        for p in range(count):
            if position[p] == axis_len:
                dire[p] = -1
            if position[p] == 0:
                dire[p] = 1
            position[p] += dire[p]
        # 查看小球是否相撞
        for p in range(count):
            for q in range(p + 1, count):
                if position[p] == position[q]:
                    dire[p] = -dire[p]
                    dire[q] = -dire[q]
    print(" ".join(str(i) for i in position))

# n, L, t = map(int, input().split())
# POS = list(map(int, input().split()))  # 存储每个小球位置
# 碰撞的小球(n, L, t, POS)
```

## 买菜

试题编号：	201809-2  
试题名称：	买菜

[返回目录](#目录)


```python
def 买菜():
    n = int(input())
    H, W = [], []
    for i in range(n):
        H.append(list(map(int, input().split())))
    for i in range(n):
        W.append(list(map(int, input().split())))
    tlen = max(H[-1][-1], W[-1][-1])
    # 初始化时间轴
    timeLine = [0] * tlen
    for s, e in H:
        for i in range(s, e):
            timeLine[i] += 1
    for s, e in W:
        for i in range(s, e):
            timeLine[i] += 1
    print(timeLine.count(2))


# 买菜()
```

## 小明放学

试题编号：	201812-2  
试题名称：	小明放学

[返回目录](#目录)


```python
def 小明放学():
    r, y, g = map(int, input().split())
    n = int(input())
    tsum = 0
    for i in range(n):
        k, t = map(int, input().split())
        if k == 0:
            tsum += t
            continue
        if k == 1:
            t += g
        if k == 2:
            t += (r + g)
        nowtime = (t - tsum) % (r + y + g)
        # (t-tsum)为倒计时绝对时间取余一次循环时间得出当前循环距绿灯结束的时间
        if nowtime > g:
            tsum += (nowtime - g)
    print(tsum)


# 小明放学()
```

## 二十四点

试题编号：	201903-2  
试题名称：	二十四点

[返回目录](#目录)


```python
def 二十四点(s0):
    for a in s0:
        a = a.replace("x", "*")
        a = a.replace("/", "//")
        sum_a = eval(a)
        if sum_a == 24:
            print("Yes")
        else:
            print("No")


# # 录入数据
# n = int(input())
# s = []
# for i in range(n):
#     s.append(input())
# 二十四点(s)
```

## 小明种苹果续

试题编号：	201909-2  
试题名称：	小明种苹果（续）

[返回目录](#目录)


```python
def 小明种苹果续():
    n = int(input())
    T, D, E = 0, 0, 0
    lost_index = []
    for i in range(n):
        s = list(map(int, input().split()))
        a0, am = s[0], s[1:]
        b = False
        temp = am[0]
        for j in am:
            if j > 0:
                if j != temp:
                    temp = j
                    b = True
            else:
                temp += j
        if b:
            lost_index.append(i)
            D += 1
        T += temp
    t = [0] * n
    for i in lost_index:
        t[i] = 1
    if t[-2] == t[-1] == t[0] == 1:
        E += 1
    if t[-1] == t[0] == t[1] == 1:
        E += 1
    for i in range(1, n - 1):
        if t[i - 1] == t[i] == t[i + 1] == 1:
            E += 1
    print(T, D, E)


# 小明种苹果续()
```

## 回收站选址

试题编号：	201912-2  
试题名称：	回收站选址

[返回目录](#目录)


```python
def 回收站选址():
    n = int(input())
    points, re = [], []
    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    for p in points:
        if ([p[0] - 1, p[1]] in points) and ([p[0] + 1, p[1]] in points) and ([p[0], p[1] + 1] in points) and (
                [p[0], p[1] - 1] in points):
            re.append(p)
    sc = [0, 0, 0, 0, 0]
    for r in re:
        score = 0
        if [r[0] - 1, r[1] - 1] in points:
            score += 1
        if [r[0] - 1, r[1] + 1] in points:
            score += 1
        if [r[0] + 1, r[1] - 1] in points:
            score += 1
        if [r[0] + 1, r[1] + 1] in points:
            score += 1
        sc[score] += 1
    for i in range(5):
        print(sc[i])


# 回收站选址()
```

## 稀疏向量

试题编号：	202006-2  
试题名称：	稀疏向量

[返回目录](#目录)


```python
def 稀疏向量():
    # # 方法1，使用列表，运行超时，60分
    # n, p, q = map(int, input().split())
    # u = [0 for _ in range(n)]
    # v = [0 for _ in range(n)]
    # for i in range(p):
    #     index, value = map(int, input().split())
    #     u[index - 1] = value
    # for j in range(q):
    #     index, value = map(int, input().split())
    #     v[index - 1] = value
    # uv = 0  # 内积
    # for k in range(n):
    #     uv += u[k] * v[k]
    # print(uv)
    
    # 方法2，使用字典，运行超时，60分
    n, p, q = map(int, input().split())
    u = {}  # 字典存储u向量索引对应的值
    for i in range(p):
        index, value = map(int, input().split())
        u[index] = value
    uv = 0  # 内积
    for j in range(q):
        index, value = map(int, input().split())
        if index in u.keys():
            uv += value * u[index]
    print(uv)


# 稀疏向量()
```

**Python一直超时，下面是一个满分的Java代码**

> Java使用Scanner读取数据也容易出现超时，具体设计步骤可看文章[《使用Java语言刷OJ经常超时的解决办法》](https://blog.csdn.net/richenyunqi/article/details/84350768)  
> 代码参考文章[《CCF计算机软件能力认证试题练习：202006-2 稀疏向量 java100分代码》](https://blog.csdn.net/a598853372/article/details/108178485)


```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args){
        int n=0, a=0, b=0;
        try {
            n = Reader.nextInt();
            a = Reader.nextInt();
            b = Reader.nextInt();
        } catch (IOException e) {
            e.printStackTrace();
        }
        HashMap<Integer,Integer> arr=new HashMap<>();


        long sum=0;

        int k=0,g=0;
        for(int i=0;i<a;i++)
        {
            try {
                k = Reader.nextInt();
                g = Reader.nextInt();

            } catch (IOException e) {
                e.printStackTrace();
            }
            arr.put(k,g);
        }
        for(int i=0;i<b;i++)
        {
            try {
                k = Reader.nextInt();
                g = Reader.nextInt();

            } catch (IOException e) {
                e.printStackTrace();
            }
            if(arr.containsKey(k))
            {
                sum+=arr.get(k)*g;
            }

        }
        System.out.println(sum);
   
    }
}
class Reader {
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokenizer = new StringTokenizer("");
    static String nextLine() throws IOException{// 读取下一行字符串
        return reader.readLine();
    }
    static String next() throws IOException {// 读取下一个字符串
        while (!tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {// 读取下一个int型数值
        return Integer.parseInt(next());
    }

    static double nextDouble() throws IOException {// 读取下一个double型数值
        return Double.parseDouble(next());
    }
}
```


## 风险人群筛查

试题编号：	202009-2  
试题名称：	风险人群筛查

[返回目录](#目录)


```python
def trans(l):
    w = []
    i = 0
    while i < len(l):
        w.append([l[i], l[i + 1]])
        i += 2
    return w


def 风险人群筛查():
    global count
    n, k, t, xl, yd, xr, yu = map(int, input().split())
    l = []
    for i in range(n):
        l0 = list(map(int, input().split()))
        l.append(trans(l0))
    pc, dc = 0, 0
    # pc：经过，dc：逗留
    for li in l:
        # 遍历每个人
        count = 0
        a = False
        flag = False
        lc = []
        for i in range(t):
            if xl <= li[i][0] <= xr and yd <= li[i][1] <= yu:
                count += 1
                a = True
                flag = True
                if count >= k:
                    dc += 1
                    break
            else:
                count = 0
                flag = False
        if a:
            pc += 1
    print(pc)
    print(dc)


# 风险人群筛查()
```
