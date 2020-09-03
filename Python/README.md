# Python 题解

2019 年 12 月份参加 CSP 之前写的代码，只做了历年的前两题，有时间可能会继续更新

## 目录

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
    - [正则表达式及re库](#正则表达式及re库)

## 题解列表

> Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint, aut, quos ipsam temporibus libero dolor laborum ipsum fuga odit rerum rem dolorem recusandae, provident necessitatibus. Illum voluptas autem eum rerum?
>
> 使用 Jupyter Notebook 查看各题的题解代码

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
# 输入一个整数
>>> n=int(input())
6
>>> n
6

# 输入一个整型列表
>>> l=list(map(int,input().split()))
1 2 3 4 5 6
>>> l
[1, 2, 3, 4, 5, 6]

# 同一行输出
>>> print(' '.join(map(str,l)))
1 2 3 4 5 6
>>> print(" ".join(str(i) for i in l))
1 2 3 4 5 6
# 也可遍历输出
>>> for i in l:
...     print(i,end=' ')
...
1 2 3 4 5 6
```

### 内置函数

Python 内置函数如下，使用方式可查看[菜鸟教程](https://www.runoob.com/python3/python3-built-in-functions.html)

[![Python内置函数](https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/QQ%E6%88%AA%E5%9B%BE20200822184129.png)](https://www.runoob.com/python3/python3-built-in-functions.html)

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
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
```

#### sorted()函数

```python
# 以下实例展示了 sorted 的最简单的使用方法：
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]                      # 默认为升序

# 你也可以使用 list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些。
>>> a=[5,2,3,1,4]
>>> a.sort()
>>> a
[1,2,3,4,5]

# 另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

# 利用key进行倒序排序
>>> example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> result_list = sorted(example_list, key=lambda x: x*-1)
>>> print(result_list)
[7, 6, 5, 4, 3, 2, 1, 0]

# 要进行反向排序，也通过传入第三个参数 reverse=True：
>>> example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> sorted(example_list, reverse=True)
[7, 6, 5, 4, 3, 2, 1, 0]
```

#### enumerate() 函数

```python
#  以下展示了使用 enumerate() 方法的实例：
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


# 普通的 for 循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

# 输出结果为：

0 one
1 two
2 three

# for 循环使用 enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

# 输出结果为：

0 one
1 two
2 three
```

### 匿名函数

python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

- lambda 只是一个表达式，函数体比 def 简单很多。
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

```python
>>> sum = lambda arg1, arg2: arg1 + arg2
>>> a=sum(5,5)
>>> a
10
```

### 正则表达式及re库

> 正则表达式的写法，可参看我的[博客](https://blog.csdn.net/qq_42907802/article/details/10653638)，re库实例可查看[菜鸟教程](https://www.runoob.com/python3/python3-reg-expressions.html)

**正则表达式的写法**

| 操作符  | 说明                             | 实例                                    |
| ------- | -------------------------------- | --------------------------------------- |
| `.`     | . 表示任何单个字符               |                                         |
| `[]`    | 字符集，对单个字符给出取值范围`  | 表示a、b、c，[a‐z]表示a到z单个字符      |
| `[^]`   | 非字符集，对单个字符给出排除范围 | `[\^abc]`表示非a或b或c的单个字符        |
| `*`     | 前一个字符0次或无限次扩展        | `abc\*` 表示ab、abc、abcc、abccc等      |
| `+`     | 前一个字符1次或无限次扩展        | `abc+ `表示abc、abcc、abccc等           |
| `?`     | 前一个字符0次或1次扩展           | `abc? `表示ab、abc                      |
| `|`     | 左右表达式任意一个               | `abc\|def `表示abc、def                 |
| `{m}`   | 扩展前一个字符m次                | `ab{2}c`表示abbc                        |
| `{m,n}` | 扩展前一个字符m至n次（含n）      | `ab{1,2}c`表示abc、abbc                 |
| `^`     | 匹配字符串开头                   | `^abc`表示abc且在一个字符串的开头       |
| `$ `    | 匹配字符串结尾                   | `abc$`表示abc且在一个字符串的结尾       |
| `( ) `  | 分组标记，内部只能使用`|`操作符  | `(abc)`表示abc，`(abc|def)`表示abc、def |
| `\d`    | 数字，等价于[0‐9]                |                                         |
| `\w `   | 单词字符，等价于[A‐Za‐z0‐9_]     |                                         |

**re库的用法**

| 函数            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| `re.search()`   | 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象  |
| `re.match()`    | 从一个字符串的开始位置起匹配正则表达式，返回match对象        |
| `re.findall()`  | 搜索字符串，以列表类型返回全部能匹配的子串                   |
| `re.split()`    | 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型     |
| `re.finditer()` | 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象 |
| `re.sub()`      | 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串 |

**Re库的另一种等价用法**

编译正则表达式：`regex = re.compile(pattern, flags=0)`

| 函数               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| `regex.search()`   | 在一个字符串中搜索匹配正则表达式的第一个位置，**返回match对象** |
| `regex.match()`    | 从一个字符串的开始位置起匹配正则表达式，**返回match对象**    |
| `regex.findall()`  | 搜索字符串，*以列表类型返回*全部能匹配的子串                 |
| `regex.split()`    | 将一个字符串按照正则表达式匹配结果进行分割，*返回列表类型*   |
| `regex.finditer()` | 搜索字符串，*返回一个匹配结果的迭代类型，每个迭代元素是match对象* |
| `regex.sub()`      | 在一个字符串中替换所有匹配正则表达式的子串，*返回替换后的字符串* |