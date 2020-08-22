# Python 题解

2019 年 12 月份参加 CSP 之前写的代码，只做了历年的前两题，有时间可能会继续更新

- [Python 题解](#python-题解)
  - [题解列表](#题解列表)
  - [常用代码片段](#常用代码片段)
    - [四舍五入](#四舍五入)
    - [向上向下取整](#向上向下取整)
    - [输入输出](#输入输出)
    - [内置函数](#内置函数)
      - [map()函数](#map函数)
      - [zip()函数](#zip函数)
      - [sorted()函数](#sorted函数)
      - [enumerate() 函数](#enumerate-函数)
    - [匿名函数](#匿名函数)

## 题解列表

- [第 1 题题解汇总](题解汇总/第1题题解汇总.ipynb)
- [第 2 题题解汇总](题解汇总/第2题题解汇总.ipynb)
- [第 3 题题解汇总](题解汇总/第3题题解汇总.ipynb)
- [第 4 题题解汇总](题解汇总/第4题题解汇总.ipynb)
- [第 5 题题解汇总](题解汇总/第5题题解汇总.ipynb)

## 常用代码片段

### 四舍五入

```python
>>> round(0.5)
0
>>> round(-0.5)
0
>>> round(0.6)
1
>>> round(0.51)
1
>>> round(-0.51)
-1
```

### 向上向下取整

```python
>>> import math
>>> math.floor(0.6)
0
>>> math.ceil(0.6)
1
>>> math.ceil(-0.6)
0
>>> math.ceil(-1.6)
-1
```

### 输入输出

```python
>>> # 输入一个整数
>>> n=int(input())
6
>>> n
6

>>> # 输入一个整型列表
>>> l=list(map(int,input().split()))
1 2 3 4 5 6
>>> l
[1, 2, 3, 4, 5, 6]

>>> # 同一行输出
>>> print(' '.join(map(str,l)))
1 2 3 4 5 6
>>> print(" ".join(str(i) for i in l))
1 2 3 4 5 6
>>> # 也可遍历输出
>>> for i in l:
...     print(i,end=' ')
...
1 2 3 4 5 6
```

### 内置函数

Python 内置函数如下，使用方式可查看[菜鸟教程](https://www.runoob.com/python/python-built-in-functions.html)

[![Python内置函数](https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/QQ%E6%88%AA%E5%9B%BE20200822165031.png)](https://www.runoob.com/python/python-built-in-functions.html)

#### map()函数

```python
>>>def square(x) :            # 计算平方数
...     return x ** 2
...
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]

```

#### zip()函数

```python
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
```

#### sorted()函数

```python
>>>a = [5,7,6,3,4,1,2]
>>> b = sorted(a)       # 保留原列表
>>> a
[5, 7, 6, 3, 4, 1, 2]
>>> b
[1, 2, 3, 4, 5, 6, 7]

>>> L=[('b',2),('a',1),('c',3),('d',4)]
>>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
>>> sorted(L, key=lambda x:x[1])               # 利用key
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]


>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(students, key=lambda s: s[2])            # 按年龄排序
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

#### enumerate() 函数

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

>>> # 普通的 for 循环
>>> i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print i, seq[i]
...     i +=1
...
0 one
1 two
2 three

>>> # for 循环使用 enumerate
>>> seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
...
0 one
1 two
2 three
```

### 匿名函数

```python
>>> sum = lambda arg1, arg2: arg1 + arg2
>>> a=sum(5,5)
>>> a
10
```
