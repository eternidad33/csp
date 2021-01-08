[![Jupyter Notebook预览](https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/upyter%E9%A2%84%E8%A7%88.png)](https://nbviewer.jupyter.org/github/eternidad33/csp/blob/master/Python/题解汇总/第1题题解汇总.ipynb)

# 目录

- [出现次数最多的数](#出现次数最多的数)
- [相反数](#相反数)
- [相邻数对](#相邻数对)
- [门禁系统](#门禁系统)
- [图像旋转](#图像旋转)
- [数列分段](#数列分段)
- [数位之和](#数位之和)
- [折点计数](#折点计数)
- [最大波动](#最大波动)
- [中间数](#中间数)
- [分蛋糕](#分蛋糕)
- [打酱油](#打酱油)
- [最小差值](#最小差值)
- [跳一跳](#跳一跳)
- [卖菜](#卖菜)
- [小明上学](#小明上学)
- [小中大](#小中大)
- [小明种苹果](#小明种苹果)
- [报数](#报数)
- [线性分类器](#线性分类器)
- [称检测点查询](#称检测点查询)

## 出现次数最多的数

试题编号：	201312-1  
试题名称：	出现次数最多的数

[返回目录](#目录)


```python
n=6
l=[10, 1, 10, 20, 30, 20]
# n = int(input())
# l = list(map(int, input().split()))
# 先将数据转成集合，然后再转成列表
s = list(set(l))
# t用于记录s中元素在l出现的次数
t = []
for x in s:
    t.append(l.count(x))
# t中最大值对应的索引即为所求
print(s[t.index(max(t))])
```

    10
    

## 相反数

试题编号：	201403-1  
试题名称：	相反数

[返回目录](#目录)


```python
# n = int(input())
n = 5
s=[1,2,3,-1,-2]
# s = input().split()
num = []
for i in range(n):
    s[i] = int(s[i])
    if s[i] not in num:
        num.append(s[i])
count = 0
for i in num:
    for j in num:
        if i + j == 0:
            count += 1
print(int(count / 2))

```

    2
    

## 相邻数对

试题编号：	201409-1  
试题名称：	相邻数对

[返回目录](#目录)


```python
# n = int(input())
n=6
s=[10,2,6,3,7,8]
# s = input().split()
num = []
for i in range(n):
    s[i] = int(s[i])
    if s[i] not in num:
        num.append(s[i])
count = 0
for i in num:
    for j in num:
        if i - j == 1:
            count += 1
print(count)
```

    3
    

## 门禁系统

试题编号：	201412-1  
试题名称：	门禁系统

[返回目录](#目录)


```python
n=5
s=[1, 2, 1, 1, 3]
# n = int(input())
# s = input().split()
a = []
for i in range(n):
    s[i] = int(s[i])
    a.append(s[i])
c = []
for j in range(len(a)):
    count = 1
    for k in range(j):
        if a[j] == a[k]:
            count += 1
    c.append(count)
for t in c:
    print(t, end=" ")

```

    1 1 2 3 1 

## 图像旋转

试题编号：	201503-1  
试题名称：	图像旋转

[返回目录](#目录)


```python
def tuxiangxuanzhuan(row, col):
    img = []
    for i in range(row):
        a = list(map(int, input().split()))
        img.append(a)
    for i in range(col):
        for j in range(row):
            print(img[j][col - 1 - i], end=" ")
        print()
```

## 数列分段

试题编号：	201509-1  
试题名称：	数列分段

[返回目录](#目录)


```python
n=8
a=[8, 8, 8, 0, 12, 12, 8, 0]
# n = int(input())
# a = list(map(int, input().split()))
count = 1
for i in range(1, n):
    if a[i] != a[i - 1]:
        count += 1
print(count)
```

    5
    

## 数位之和

试题编号：	201512-1  
试题名称：	数位之和

[返回目录](#目录)


```python
# n = input()
n="20151220"
sum_n = 0
for i in n:
    i = int(i)
    sum_n += i
print(sum_n)
```

    13
    

## 折点计数

试题编号：	201604-1  
试题名称：	折点计数

[返回目录](#目录)


```python
n=7
a=[5,4,1,2,3,6,4]
# n = int(input())
# a = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if a[i - 1] > a[i] and a[i + 1] > a[i]:
        count += 1
    elif a[i - 1] < a[i] and a[i + 1] < a[i]:
        count += 1
    else:
        pass
print(count)

```

    2
    

## 最大波动

试题编号：	201609-1  
试题名称：	最大波动

[返回目录](#目录)


```python
n=6
a=[2, 5, 5, 7, 3, 5]
# n = int(input())
# a = list(map(int, input().split()))
b = 0
for i in range(n - 1):
    temp = abs(a[i] - a[i + 1])
    if temp > b:
        b = temp
print(b)
```

    4
    

## 中间数

试题编号：	201612-1  
试题名称：	中间数

[返回目录](#目录)


```python
n=6
a=[2, 6, 5, 6, 3, 5]
# n = int(input())
# a = list(map(int, input().split()))
t = False
for i in a:
    max_num, min_num = 0, 0
    for j in a:
        if j < i:
            min_num += 1
        if j > i:
            max_num += 1
    if min_num == max_num:
        print(i)
        t = True
        break
if not t:
    print(-1)
```

    5
    

## 分蛋糕

试题编号：	201703-1  
试题名称：	分蛋糕

[返回目录](#目录)


```python
n,k=6,9
a=[2, 6, 5, 6, 3, 5]
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
count = 0
t = 0
for i in a:
    t += i
    if t >= k:
        count += 1
        t = 0
if t != 0:
    count += 1
print(count)
```

    3
    

## 打酱油

试题编号：	201709-1  
试题名称：	打酱油

[返回目录](#目录)


```python
# n = int(input())
n=40
n1 = n // 50
n2 = (n % 50) // 30
n3 = (n - (50 * n1 + 30 * n2)) / 10
n4 = 7 * n1 + 4 * n2 + n3
print(int(n4))
```

    5
    

## 最小差值

试题编号：	201712-1  
试题名称：	最小差值

[返回目录](#目录)


```python
n=5
a=[1, 5, 4, 8, 20]
# n = int(input())
# a = list(map(int, input().split()))
minn = abs(a[1] - a[0])
for i in range(n):
    for j in range(n):
        if i != j:
            temp = abs(a[i] - a[j])
            if temp < minn:
                minn = temp
print(minn)

```

    1
    

## 跳一跳

试题编号：	201803-1  
试题名称：	跳一跳

[返回目录](#目录)


```python
a=[1, 1, 2, 2, 2, 1, 1, 2, 2, 0]
# a = list(map(int, input().split()))
n = len(a)
score, temp = 0, 2
for i in range(n):
    if a[i] == 0:
        break
    elif a[i] == 1:
        score += 1
        temp = 2
    else:
        if a[i - 1] == 1 or i == 0:
            score += 2
            temp += 2
        else:
            score += temp
            temp += 2
print(score)

```

    22
    

## 卖菜

试题编号：	201809-1  
试题名称：	卖菜

[返回目录](#目录)


```python
n=8
a=[4, 1, 3, 1, 6, 5, 17, 9]
# n = int(input())
# a = list(map(int, input().split()))
b = []
for i in range(n):
    if i == 0:
        temp = (a[i] + a[i + 1]) // 2
        b.append(temp)
    elif i == n - 1:
        temp = (a[i] + a[i - 1]) // 2
        b.append(temp)
    else:
        temp = (a[i - 1] + a[i] + a[i + 1]) // 3
        b.append(temp)
for i in b:
    print(i, end=" ")
```

    2 2 1 3 4 9 10 13 

## 小明上学

试题编号：	201812-1  
试题名称：	小明上学

[返回目录](#目录)


```python
def xiaomingshangxue():
    r, y, g = list(map(int, input().split()))
    n = int(input())
    second = 0
    for i in range(n):
        k, t = list(map(int, input().split()))
        if k == 0 or k == 1:
            second += t
        elif k == 2:
            second += (t + r)
        else:
            pass
    print(second)


# xiaomingshangxue()
```

## 小中大

试题编号：	201903-1  
试题名称：	小中大

[返回目录](#目录)


```python
n=3
a=[-1,2,4]

# n = int(input())
# a = list(map(int, input().split()))

mid = (a[(n - 1) // 2] + a[n // 2]) / 2
if int(mid) == mid:
    mid = int(mid)

print("{} {} {}".format(max(a), round(mid, 1), min(a)))
```

    4 2 -1
    

## 小明种苹果

试题编号：	201909-1  
试题名称：	小明种苹果

[返回目录](#目录)


```python
def xiaoMingZhongPingGuo():
    N, M = map(int, input().split())
    T, k, P = 0, 0, 0
    for i in range(N):
        s = list(map(int, input().split()))
        a0, am = s[0], s[1:]
        T += a0
        am = map(abs, am)
        p = sum(am)
        T -= p
        if p > P:
            P = p
            k = i + 1
    print(T, k, P)


# xiaoMingZhongPingGuo()
```

## 报数

试题编号：	201912-1  
试题名称：	报数

[返回目录](#目录)


```python
n=20
# n = int(input())
count = 0
i = 0
l = [0, 0, 0, 0]
while count != n:
    i += 1
    if i % 7 == 0 or str(i).__contains__('7'):
        b = i % 4
        l[b] += 1
    else:
        count += 1
print(l[1])
print(l[2])
print(l[3])
print(l[0])
```

    2
    1
    1
    0
    

## 线性分类器

试题编号：	202006-1  
试题名称：	线性分类器

[返回目录](#目录)


```python
def xianXingFenLeiQi():
    n, m = map(int, input().split())
    datas = []
    # 录入数据
    for i in range(n):
        data = input().split()
        data[0] = int(data[0])
        data[1] = int(data[1])
        datas.append(data)
    flags = []
    for i in range(m):
        line = list(map(int, input().split()))
        flag = True
        # 判断第一个点的位置
        r1 = datas[0][0] * line[1] + datas[0][1] * line[2] + line[0]
        if r1 > 0 and datas[0][2] == 'A':
            AisUp = True
        elif r1 < 0 and datas[0][2] != 'A':
            AisUp = True
        else:
            AisUp = False

        for j in range(1, n):
            result = datas[j][0] * line[1] + datas[j][1] * line[2] + line[0]
            if AisUp:
                if result > 0 and datas[j][2] == 'A':
                    flag = True
                elif result > 0 and datas[j][2] == 'B':
                    flag = False
                    break
                elif result < 0 and datas[j][2] == "A":
                    flag = False
                    break
                elif result < 0 and datas[j][2] == "B":
                    flag = True
            else:
                if result < 0 and datas[j][2] == 'A':
                    flag = True
                elif result < 0 and datas[j][2] == 'B':
                    flag = False
                    break
                elif result > 0 and datas[j][2] == "A":
                    flag = False
                    break
                elif result > 0 and datas[j][2] == "B":
                    flag = True
        flags.append(flag)
    for flag in flags:
        if flag:
            print("Yes")
        else:
            print("No")


# xianXingFenLeiQi()
```


## 称检测点查询

试题编号：	202009-1  
试题名称：	称检测点查询

[返回目录](#目录)


```python
def 称检测点查询():
    n, X, Y = map(int, input().split())
    w = []
    s = []
    for i in range(n):
        x, y = map(int, input().split())
        si = (x - X) ** 2 + (y - Y) ** 2
        s.append(si)
        w.append([i + 1, si])
    s = sorted(s)
    da = []
    for i in range(3):
        for j in range(n):
            flag = False
            if w[j][1] == s[i]:
                if w[j][0] not in da:
                    da.append(w[j][0])
                    flag = True
                    break
                if flag:
                    break
    for d in da:
        print(d)


# 称检测点查询()
```
