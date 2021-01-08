[![Jupyter Notebook预览](https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/upyter%E9%A2%84%E8%A7%88.png)](https://nbviewer.jupyter.org/github/eternidad33/csp/blob/master/Python/题解汇总/第3题题解汇总.ipynb)

# 目录

- [最大的矩形](#最大的矩形)
- [命令行选项](#命令行选项)
- [字符串匹配](#字符串匹配)
- [集合竞价](#集合竞价)
- [节日](#节日)
- [模板生成系统](#模板生成系统)
- [画图](#画图)
- [路径解析](#路径解析)
- [炉石传说](#炉石传说)
- [权限查询](#权限查询)
- [Markdown](#Markdown)
- [JSON查询](#JSON查询)
- [Crontab](#Crontab)
- [URL映射](#URL映射)
- [元素选择器](#元素选择器)
- [CIDR合并](#CIDR合并)
- [损坏的RAID5](#损坏的RAID5)
- [字符画](#字符画)
- [化学方程式](#化学方程式)
- [Markdown渲染器](#Markdown渲染器)

## 最大的矩形

试题编号：	201312-3  
试题名称：	最大的矩形

[返回目录](#目录)


```python
def 最大的矩形(count, l):
    """思路：遍历每个矩形向左右延伸的最大面积"""
    b = []  # 储存所有局部最大矩形
    for i in range(count):
        width = 0  # 矩形宽度
        for j in reversed(range(i)):  # 向左（反转）搜索左边高度不小于矩形i高度的
            if l[j] >= l[i]:
                width += 1  # 加左边宽度
            else:
                break
        for j in range(i, count):  # 向右搜索高度不小于矩形i高度的
            if l[j] >= l[i]:
                width += 1  # 加右边宽度（含矩形i自身）
            else:
                break
        b.append(l[i] * width)  # 得到包含矩形i自身的局部最大矩形面积
    print(max(b))  # 从所有局部最大矩形选出全局最大举行

# n = int(input())
# a = list(map(int, input().split()))
# 最大的矩形(n, a)
```

## 命令行选项

试题编号：	201403-3  
试题名称：	命令行选项

[返回目录](#目录)


```python
def 命令行选项(ops, count, cmd_list):
    ops += " "
    global i
    uop = []  # 存储无参选项
    hop = []  # 存储有参选项
    for i in range(len(ops) - 1):
        if ops[i + 1] == ":":
            hop.append(ops[i])
        else:
            uop.append(ops[i])
    for i in range(count):
        # 将命令分割
        cmd = cmd_list[i]
        d = {}
        j = 1
        while j < len(cmd):
            # 如果为参数选项
            if cmd[j][0] == "-" and len(cmd[j]) == 2:
                if cmd[j][1] in uop:  # 无参选项处理
                    d[cmd[j][1]] = "#"
                    j += 1
                elif cmd[j][1] in hop and j + 1 < len(cmd):  # 有参选项处理
                    d[cmd[j][1]] = cmd[j + 1]
                    j += 2
                else:  # 其他选项错误退出循环
                    break
            else:
                break
        keys = list(set(d.keys()))
        keys.sort()
        print("Case " + str(i + 1) + ":", end="")
        for key in keys:
            print(" -" + key, end="")
            if d[key] != "#":
                print(" " + d[key], end="")
        print()


# options = input()
# n = int(input())
# cmds = []
# for i in range(n):
#     cmds.append(list(input().split()))
# 命令行选项(options, n, cmds)
```

## 字符串匹配

试题编号：	201409-3  
试题名称：	字符串匹配

[返回目录](#目录)


```python
def 字符串匹配(s0, c, ss):
    # 区分大小写
    if c == 1:
        for s in ss:
            if s0 in s:
                print(s)
    else:
        for s in ss:
            if s0.lower() in s.lower():
                print(s)


# s1 = input()
# flag = int(input())
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# 字符串匹配(s1, flag, ls)
```

## 集合竞价

试题编号：	201412-3  
试题名称：	集合竞价

[返回目录](#目录)


```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 集合竞价.py
@date: 2020-08-26
@Editor: PyCharm
@desc: 
"""
# 集合竞价
# cancel是从前往后执行的，不能取消cancel
import sys


def 集合竞价():
    global count
    records = []
    delList = []
    for line in sys.stdin:
        record = list(line.split())
        records.append(record)
    # 根据cancel清除记录
    for record in records:
        if record[0] == "cancel":  # 用数组记录并del可能会删除两遍发生错误
            record[0] = ""
            records[int(record[1]) - 1][0] = ""  # 将要删除的记录和本条记录都清空
        elif record[0] in ("buy", "sell"):
            record[1] = float(record[1])  # 价格
            record[2] = int(record[2])  # 数量
    for i in reversed(range(len(records))):  # 删除撤销记录
        # print(i,records[i])
        if records[i][0] == "":
            records.remove(records[i])
    # print(records)
    # 构建buy，sell字典
    records.sort(key=(lambda x: x[1]), reverse=True)  # 根据价格从大到小排序
    buy_list = {}
    last_buy = 0
    for bs, price, count in records:
        if bs == "buy":
            last_buy += count
        buy_list[price] = last_buy  # 存入字典
    sell_list = {}
    last_sell = 0
    for bs, price, count in records[::-1]:  # 价格从小到大
        if bs == "sell":
            last_sell += count
        sell_list[price] = last_sell
    # 求竞价结果
    prices = list(buy_list)
    max_amount = 0
    best_price = 0
    for price in prices:
        if min(buy_list[price], sell_list[price]) > max_amount:  # 买入和卖出两者的最小值为成交数
            best_price = price
            max_amount = min(buy_list[price], sell_list[price])  # 记录当前最大成交数
    print("{:.2f} {}".format(best_price, max_amount))


# 集合竞价()
```

## 节日

试题编号：	201503-3  
试题名称：	节日

[返回目录](#目录)


```python
month0 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年每月天数
month1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年每月的天数


def is_leap_year(y):
    """判断是否为闰年"""
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


def week(y, m, d):
    """判断y年m月第d天为周几"""
    day_sum = 0
    for i in range(1850, y):
        if is_leap_year(i):
            day_sum += 366
        else:
            day_sum += 365
    month = []
    if is_leap_year(y):
        month[:] = month1
        for i in range(1, m):
            day_sum += month[i - 1]
    else:
        month[:] = month0
        for i in range(1, m):
            day_sum += month[i - 1]
    day_sum += d
    day_sum = (day_sum + 1) % 7
    return day_sum


def 节日():
    l1 = [int(x) for x in input().split()]
    l1[2] = 0 if l1[2] == 7 else l1[2]
    for i in range(l1[3], l1[4] + 1):
        if is_leap_year(i):
            month = month1[l1[0] - 1]
        else:
            month = month0[l1[0] - 1]
        weekday = week(i, l1[0], 1)  # 存储month月的第一天为周几
        a = 0
        for j in range(month):
            if (weekday + j) % 7 == l1[2]:
                a += 1
                if a == l1[1]:
                    b = str(l1[0]).zfill(2)  # 将字符串的长度填充为2，例如：'1'.zfill(2),输出为'01'
                    d = str(j + 1).zfill(2)
                    c = [str(i), '/', b, '/', d]
                    print(''.join(c))
        if a < l1[1]:
            print('none')


# 节日()
```

## 模板生成系统

试题编号：	201509-3  
试题名称：	模板生成系统

[返回目录](#目录)


```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 模板生成系统.py
@date: 2020-09-01
@Editor: PyCharm
@desc: 
"""
# 模板生成系统
# re正则表达式匹配
import re


def 模板生成系统():
    global var_dict
    m, n = map(int, input().split())
    temple = []  # 模板
    for i in range(m):
        temple.append(input())
    var_dict = dict()  # 变量
    for i in range(n):
        var, value = input().split(" ", 1)
        var_dict[var] = eval(value)  # 清除引号

    def trans(matched):  # 变量替换值函数
        var = matched.group('var')
        if var in var_dict:
            return var_dict[var]
        else:
            return ""

    for i in range(len(temple)):
        print(re.sub(r'{{ (?P<var>\w*) }}', trans, temple[i]))
        # re替换方法，匹配{{  }}格式(?P<var>)命名组，\w匹配小写字母数字和下划线，*表示匹配一个或多个\w
        # trans匹配方法，调用函数将命名组的var替换成值


# 模板生成系统()

# 11 2
# <!DOCTYPE html>
# <html>
# <head>
# <title>User {{ name }}</title>
# </head>
# <body>
# <h1>{{ name }}</h1>
# <p>Email: <a href="mailto:{{ email }}">{{ email }}</a></p>
# <p>Address: {{ address }}</p>
# </body>
# </html>
# name "David Beckham"
# email "david@beckham.com"
```

## 画图

试题编号：	201512-3  
试题名称：	画图

[返回目录](#目录)


```python
def 画图():
    global list1, list2, bfs, n, m, artwork
    list1 = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 定义列表使得bfs可以向四周搜索
    list2 = ['-', '|', '+', 'XXX']  # 定义列表填作为是否填充的判断

    def bfs(x, y, c):  # 定义广度搜索函数
        for i in list1:
            xx = i[0] + x
            yy = i[1] + y
            if xx >= n or xx < 0 or yy < 0 or yy >= m or artwork[yy][xx] in list2:
                continue
            artwork[yy][xx] = c
            bfs(xx, yy, c)

    n, m, p = map(int, input().split())
    artwork = [["." for i in range(n)] for j in range(m)]
    for i in range(p):
        list3 = input().split()
        if int(list3[0]) == 0:
            list3 = [int(x) for x in list3]
            if list3[1] == list3[3]:
                for j in range(min(list3[2], list3[4]), max(list3[2], list3[4]) + 1):
                    if artwork[j][list3[1]] == '-' or artwork[j][list3[1]] == '+':
                        artwork[j][list3[1]] = '+'
                    else:
                        artwork[j][list3[1]] = '|'
            else:
                for j in range(min(list3[1], list3[3]), max(list3[1], list3[3]) + 1):
                    if artwork[list3[2]][j] == '|' or artwork[list3[2]][j] == '+':
                        artwork[list3[2]][j] = '+'
                    else:
                        artwork[list3[2]][j] = '-'
        else:
            list2[3] = list3[3]
            bfs(int(list3[1]), int(list3[2]), list3[3])
    for i in range(m):
        for j in artwork[m - 1 - i]:
            print(j, end="")
        print()
```

以上为90分的代码，下面是满分的Java代码

```java
import java.util.Scanner;
 
public class Main {
	public static final int N = 105;
	static char graph[][] = new char[N][N];
	static void dfs(int x, int y, char c,int hei,int wid) {
		if (x >= 0&&x < hei && y < wid && y >= 0 && graph[x][y] != '+' && graph[x][y] != '|' && graph[x][y] != '-'&&graph[x][y] != c) {
			graph[x][y] = c;
			dfs(x + 1, y, c,hei,wid);
			dfs(x - 1, y, c,hei,wid);
			dfs(x, y + 1, c,hei,wid);
			dfs(x, y - 1, c,hei,wid);
		}
	}
 
	static void line(int x1, int y1, int x2, int y2) {
		if (x1 == x2) {
			int h1 = Math.min(y1, y2);
			int h2 = Math.max(y1, y2);
 
			for (int j = h1; j <= h2; j++) {
				if (graph[j][x1] == '.' || graph[j][x1] == '|')
					graph[j][x1] = '|';
				else
					graph[j][x1] = '+';
			}
		}
		if (y1 == y2) {
			int h1 = Math.min(x1, x2);
			int h2 = Math.max(x1, x2);
			for (int j = h1; j <= h2; j++) {
				if (graph[y1][j] == '.' || graph[y1][j] == '-')
					graph[y1][j] = '-';
				else
					graph[y1][j] = '+';
			}
		}
	}
 
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int wid = scanner.nextInt();
		int hei = scanner.nextInt();
		int n = scanner.nextInt();
		for (int i = 0; i < hei; i++) {
			for (int j = 0; j < wid; j++) {
				graph[i][j] = '.';
			}
		}
		for (int k = 0; k < n; k++) {
			int op = scanner.nextInt();
			if (op == 0) {
				int x1 = scanner.nextInt();
				int y1 = scanner.nextInt();
				int x2 = scanner.nextInt();
				int y2 = scanner.nextInt();
				line(x1, y1, x2, y2);
			} else {
				int x = scanner.nextInt();
				int y = scanner.nextInt();
				char c = scanner.next().charAt(0);
				dfs(y, x, c,hei,wid);	
			}
		}
 
		for (int i = hei - 1; i >= 0; i--) {
			for (int j = 0; j < wid; j++) {
				System.out.print(graph[i][j]);
			}
			System.out.println();
		}
	}
}
```

## 路径解析

试题编号：	201604-3  
试题名称：	路径解析

[返回目录](#目录)


```python
def 路径解析():
    n = int(input())
    pwd = input()  # 当前目录
    for i in range(n):
        route = input()
        # re.match()匹配字符串开头
        if re.match("/", route) is None:  # 相对路径和空字符串
            route = pwd + '/' + route
        route += "/"  # 结尾加‘/’方便替换，（必须在处理完空串后再加‘/’ ，空串10分）
        # re.sub()替换
        route = re.sub(r"//+", "/", route)  # 删去多个‘/’
        # 处理[.]
        route = re.sub(r"(/[.])+/", "/", route)  # [.]表示.不转义
        # 处理[..]
        # re.search()搜索
        while re.search(r"/[.]{2}/", route):
            route = re.sub(r"^(/[.]{2})+/", "/", route)  # 最开头根目录的上一级还是‘/’,^匹配开头
            if "/../" in route:  # 文件名不能只用字母数字匹配，要求还有.-_ （10分-20分）
                p = route.index("/../")
                x = route.rindex("/", 0, p)  # 从0到p范围找，找‘/../’前面的一个‘/’索引也就是上级目录
                route = route[0:x] + route[p + 3:]  # 去掉‘/上级目录/../’
        while len(route) > 1 and route[-1] == "/":  # 去除结尾‘/’
            route = route[:-1]
        print(route)
        
# 参考链接：https://blog.csdn.net/SL_logR/article/details/82711605
```

## 炉石传说

试题编号： 201609-3  
试题名称： 炉石传说

[返回目录](#目录)


```python
class summon:
    # 随从类
    def __init__(self, position, attack, health):
        self.position = position  # 位置，取值[1,7]
        self.attack = attack  # 攻击力
        self.health = health  # 生命力
        self.name = 'summon'  # 表明这是一个随从


class attack:
    # 攻击类
    def __init__(self, first, second):
        self.first = first  # 攻击的随从编号，取值[1,7]
        self.second = second  # 攻击对象编号，取值[0,7]，其中0表示攻击英雄
        self.name = 'attack'  # 表明攻击操作


class player:
    # 英雄类
    def __init__(self):
        self.health = 30  # 英雄生命力
        self.attack = 0  # 英雄的攻击力，没有用到
        self.people = []  # 英雄所拥有的随从
#    def fight(self)


def 炉石传说():
    global two
    n = int(input())
    data = []
    one = player()
    two = player()
    flag = 1  # 标记哪个英雄进行操作
    # 读取、预处理键盘输入数据
    for i in range(n):
        temp = input().split()
        if temp[0] == "summon":
            data.append(summon(int(temp[1]), int(temp[2]), int(temp[3])))
        elif temp[0] == 'attack':
            data.append(attack(int(temp[1]), int(temp[2])))
        else:
            data.append(temp[0])
    # 运行用户输入的操作
    for i in range(n):
        if flag == 1:  # 先出英雄操作
            if data[i] == 'end':
                flag = 2
            else:
                if data[i].name == 'summon':  # 上随从
                    one.people.insert(data[i].position - 1, data[i])
                elif data[i].name == 'attack':  # 攻击
                    if data[i].second == 0:
                        two.health = two.health - one.people[data[i].first - 1].attack
                    else:  # 注意，要把两者攻击后的随从生命算出来后，再检测随从是否消失
                        one.people[data[i].first - 1].health -= two.people[data[i].second - 1].attack
                        two.people[data[i].second - 1].health -= one.people[data[i].first - 1].attack
                        if two.people[data[i].second - 1].health <= 0:
                            two.people.pop(data[i].second - 1)
                        if one.people[data[i].first - 1].health <= 0:
                            one.people.pop(data[i].first - 1)
        else:
            if data[i] == 'end':
                flag = 1
            else:
                if data[i].name == 'summon':
                    two.people.insert(data[i].position - 1, data[i])
                elif data[i].name == 'attack':
                    if data[i].second == 0:
                        one.health = one.health - two.people[data[i].first - 1].attack
                    else:
                        two.people[data[i].first - 1].health -= one.people[data[i].second - 1].attack
                        one.people[data[i].second - 1].health -= two.people[data[i].first - 1].attack
                        if one.people[data[i].second - 1].health <= 0:
                            one.people.pop(data[i].second - 1)
                        if two.people[data[i].first - 1].health <= 0:
                            two.people.pop(data[i].first - 1)
    if one.health <= 0:
        print(-1)
    elif two.health <= 0:
        print(1)
    elif one.health > 0 and two.health > 0:
        print(0)
    print(one.health)
    length = len(one.people)
    if length == 0:
        print(0)
    else:
        temp = [length]
        for i in one.people:
            temp.append(i.health)
        print(" ".join(map(str, temp)))
    print(two.health)
    length = len(two.people)
    if length == 0:
        print(0)
    else:
        temp = [length]
        for i in two.people:
            temp.append(i.health)
        print(" ".join(map(str, temp)))


# 炉石传说()
# 参考链接：https://blog.csdn.net/qq_34950042/article/details/88380948
```

## 权限查询

试题编号：	201612-3  
试题名称：	权限查询

[返回目录](#目录)


```python
def 权限查询():
    pris = {}  # privileges
    roles = {}
    users = {}
    # 权限
    p = int(input())
    for i in range(p):
        s = input().split(":")
        pris[s[0]] = s[1] if len(s) == 2 else ""  # 因为保证合法性所以其实不用写这段
    # 角色
    r = int(input())
    for i in range(r):
        s = input().split()
        n = int(s[1])  # 角色权限个数
        mypri = []
        for j in range(2, 2 + n):
            mypri.append(s[j].split(":"))
        roles[s[0]] = mypri  # 以列表储存
    # 用户
    u = int(input())
    for i in range(u):
        s = input().split()
        n = int(s[1])  # 用户角色个数
        myrole = []
        for j in range(2, 2 + n):
            myrole.append(s[j])
        mypri = {}
        for role in myrole:  # 遍历用户
            for pri in roles[role]:  # 遍历每个用户权限
                if len(pri) == 1:  # 无等级权限
                    mypri[pri[0]] = ""
                elif pri[0] not in mypri:  # 等级权限首次存储
                    mypri[pri[0]] = int(pri[1])
                else:  # 比较存入权限最大等级
                    mypri[pri[0]] = max(mypri[pri[0]], int(pri[1]))
        users[s[0]] = mypri  # 用字典存储
    # 查询
    q = int(input())
    for i in range(q):
        name, this_pri = input().split()  # 用户名，权限
        this_pri = this_pri.split(":")  # 区分是否有等级

        if name in users:  # 用户存在
            if this_pri[0] in users[name]:  # 权限名存在
                if len(this_pri) == 1:
                    if users[name][this_pri[0]] == "":  # 无等级权限
                        print("true")
                    else:
                        print(users[name][this_pri[0]])  # 查询等级
                elif len(this_pri) == 2:  # 带等级
                    if users[name][this_pri[0]] == "":  # 无效查询
                        print("false")
                    elif int(this_pri[1]) <= users[name][this_pri[0]]:  # 等级满足
                        print("true")
                    else:  # 等级不满足
                        print("false")
            else:
                print("false")
        else:
            print("false")


# 权限查询()
# 参考链接：https://blog.csdn.net/SL_logR/article/details/82711807
```


## Markdown

试题编号：	201703-3  
试题名称：	Markdown

[返回目录](#目录)


```python
import sys


def Markdown():
    data = []  # 记录Markdown转化为html后的文档，data中的一个元素代表html的一行（除开''）
    flag = False  # 标记段落是否多行
    list_tag = False  # 标记无序列表是否多行
    for line in sys.stdin:  # line代表键盘输入的每行内容
        # 区块
        line = line.strip()
        if '#' in line:  # 标题
            count = line.count("#")  # 计算是第几标题
            temp = line.split('#')[-1].strip()  # 这里分割最好不要用“空格”防止标题含有空格
            temp = "<h" + str(count) + ">" + temp + "</h" + str(count) + ">"
        elif '*' in line:  # 无序列表
            if not list_tag:
                data.append('<ul>')
                list_tag = True
            temp = line.split("*")[-1].strip()  # 采用“*”分割
            temp = "<li>" + temp + "</li>"
        else:  # 段落
            if line and not flag:  # 首次出现段落
                temp = '<p>' + line
                flag = True
            elif line and flag:  # 中间出现段落
                temp = line
            elif line == '' and flag:  # 段落结束，修改data最后一个元素的值（即加上'</p>'）
                data[-1] = data[-1] + '</p>'
                flag = False
                temp = ''
            elif line == '' and list_tag:  # 无序列表结束
                data.append("</ul>")
                temp = ""
                list_tag = False
            else:
                temp = ''
                flag = False
                list_tag = False

        # 行内

        # 强调
        i = 1  # 标记是第一个"_"，还是第二个
        while '_' in temp:  # 注意强调以及超链接都可能多个，所以用无限循环
            index_1 = temp.find('_')
            if i == 1:
                temp = temp[:index_1] + '<em>' + temp[index_1 + 1:]
                i = 2
            else:
                temp = temp[:index_1] + '</em>' + temp[index_1 + 1:]
                i = 1
        # 超链接
        while '[' in temp:  # 注意这里是while，可能有多个超链接
            i1 = temp.find('[')
            i2 = temp.find(']', i1 + 1)
            i3 = temp.find('(', i2 + 1)
            i4 = temp.find(')', i3 + 1)
            temp = temp[:i1] + '<a href="' + temp[(i3 + 1):i4] + '">' + temp[(i1 + 1):i2] + "</a>" + temp[(i4 + 1):]

        data.append(temp)  # 将转化后的html加入data
    if flag:  # 当以段落结束时
        data[-1] = data[-1] + '</p>'
    if list_tag:  # 当以无序列表结束时
        data.append("</ul>")
    for d in data:
        if d == '':
            continue
        print(d)


# Markdown()
# 参考链接：https://blog.csdn.net/qq_34950042/article/details/88427915
```

## JSON查询

试题编号：	201709-3  
试题名称：	JSON查询

[返回目录](#目录)


```python
import json  # python 有内置json库


def JSOIN查询():
    n, m = map(int, input().split())
    # json解析
    json_str = ""
    for i in range(n):
        json_str += input()
    data = json.loads(json_str)  # json字符串加载为字典
    querys = []
    for i in range(m):
        querys.append(input().split("."))  # 根据.划分层次
    json_type = {
        str: "STRING",
        dict: "OBJECT"
    }
    for q in querys:
        try:  # 检查字典项的类型，将每个层次带入查询转为字符串 data["a"]["b"]并eval()执行
            if type(eval("data" + "".join(["[" + repr(x) + "]" for x in q]))) == str:
                print("STRING", eval("data" + "".join(["[" + repr(x) + "]" for x in q])))
            elif type(eval("data" + "".join(["[" + repr(x) + "]" for x in q]))) == dict:
                print("OBJECT")
        except Exception:  # 出现异常表示不存在
            print("NOTEXIST")


# JSOIN查询()
# 参考链接：https://blog.csdn.net/SL_logR/article/details/82711846
```

## Crontab

试题编号：	201712-3  
试题名称：	Crontab

[返回目录](#目录)


```python
Days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Days_of_mons_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Month_string_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Weekday_string_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


def m_string2int(m):
    try:
        a = int(m)
        return a
    except:
        for i in range(12):
            if m.lower() == Month_string_list[i].lower():
                return i + 1


def w_string2int(w):
    try:
        a = int(w)
        return a
    except:
        for i in range(7):
            if w.lower() == Weekday_string_list[i].lower():
                return i


def ddmm(day, mon):
    # d为输入天的字符串，m为输入月份的字符串
    # start为开始的天，end为结束的天
    # 函数返回所有符合条件的天的list
    day_mon_set = []
    dayset = []
    days = day.split(',')
    for d in days:
        if d == '*':
            dayset = list(i + 1 for i in range(31))
        elif len(d.split('-')) != 1:
            s, e = list(map(int, d.split('-')))
            for i in range(s, e + 1):
                dayset.append(i)
        else:
            dayset.append(int(d))
    mons = mon.split(',')
    monset = []
    for m in mons:
        if m == '*':
            monset = list(i + 1 for i in range(12))
        elif len(m.split('-')) != 1:
            s, e = m.split('-')
            for i in range(m_string2int(s), m_string2int(e) + 1):
                monset.append(i)
        else:
            monset.append(m_string2int(m))
    for x in monset:
        for y in dayset:
            day_mon_set.append(x * 100 + y)
    return day_mon_set


def MMHH(mm, hh):
    min_hour_set = []
    minset = []
    hourset = []
    mms = mm.split(',')
    for m in mms:
        if m == '*':
            minset = list(i for i in range(60))
        elif len(m.split('-')) != 1:
            s, e = list(map(int, m.split('-')))
            for i in range(s, e + 1):
                minset.append(i)
        else:
            minset.append(int(m))
    hhs = hh.split(',')
    for h in hhs:
        if h == '*':
            hourset = list(i for i in range(24))
        elif len(h.split('-')) != 1:
            s, e = list(map(int, h.split('-')))
            for i in range(s, e + 1):
                hourset.append(i)
        else:
            hourset.append(int(h))
    for h in hourset:
        for m in minset:
            min_hour_set.append(h * 100 + m)
    return min_hour_set


def day_of_week(ww):
    if ww == '*':
        return list(i for i in range(7))
    else:
        dset = []
        wws = ww.split(',')
        for w in wws:
            if len(w.split('-')) != 1:
                s, e = w.split('-')
                for i in range(w_string2int(s), w_string2int(e) + 1):
                    dset.append(i)
            else:
                dset.append(w_string2int(w))
        return dset


def check(ymhdmw):
    normal = []
    for X in ymhdmw:
        year, mon_day, hour_min, weekday, com = X
        # 检查是否在设置的时间范围内
        time = year * 100000000 + mon_day * 10000 + hour_min
        if time < start or time >= end:
            continue

        # 检查每个月的日期数是否正常
        if (year % 4) == 0:
            daysbefore = sum(Days_of_mons_in_leap_year[0:mon_day // 100 - 1])
            if (Days_of_mons_in_leap_year[mon_day // 100 - 1] < (mon_day % 100)):
                continue
        else:
            daysbefore = sum(Days_of_month[0:mon_day // 100 - 1])
            if Days_of_month[mon_day // 100 - 1] < (mon_day % 100):
                continue

        # 检查星期数是否正常
        years_from_1970 = year - 1970
        num_of_leap_year = (years_from_1970 + 1) // 4
        days_from_197011 = years_from_1970 * 365 + num_of_leap_year + daysbefore + mon_day % 100 - 1
        if ((days_from_197011 % 7) + 4) % 7 == weekday:
            normal.append([time, command])
    return normal


def Crontab():
    global start, end, command
    n, start, end = list(map(int, input().split()))
    crontab = []
    startyear = start // 100000000
    endyear = end // 100000000
    for i in range(n):
        minutes, hours, day_of_month, month, dayofweek, command = input().split()
        minhoueset = MMHH(minutes, hours)
        daymonset = ddmm(day_of_month, month)
        week = day_of_week(dayofweek)
        ymhdmw = []
        for i in range(startyear, endyear + 1):
            for mh in minhoueset:
                for dm in daymonset:
                    for w in week:
                        ymhdmw.append([i, dm, mh, w, command])
        crontab.append(check(ymhdmw))
    crontab1 = []
    for X in crontab:
        for x in X:
            crontab1.append(x)
    crontab2 = sorted(crontab1, key=lambda x: x[0])
    for i in crontab2:
        print(i[0], i[1])


# Crontab()
# 参考链接：https://blog.csdn.net/qq_41564189/article/details/100639481
```


## URL映射

试题编号：	201803-3  
试题名称：	URL映射

[返回目录](#目录)


```python
def URL映射():
    m, n = map(int, input().split())
    rules = {}
    rlist = {}
    for i in range(m):
        rule, name = input().split()
        rlist[rule] = rule.split("/")
        rules[rule] = name
    for i in range(n):
        query = input()
        q = query.split("/")
        find = False
        for rule in rules.keys():
            r = rlist[rule]
            if len(q) >= len(r):
                args = []
                match = 0
                RightPath = False
                for j in range(len(r)):
                    if q[j] == r[j]:
                        match += 1

                    elif q[j].isdigit() and r[j] == "<int>":
                        args.append(str(int(q[j])))
                        match += 1

                    elif r[j] == "<str>":
                        if q[j] == "":  # 加了这个判断就100分了 ?!空字符串对应<str>
                            break
                        args.append(q[j])
                        match += 1

                    elif r[j] == "<path>":
                        args.append("/".join(q[len(r) - 1:]))
                        RightPath = True
                        match += 1

                    else:
                        break

                if match == len(r) and (len(q) == len(r) or RightPath):
                    print(rules[rule] + " " + " ".join(args))
                    find = True
                    break
            else:
                continue
        if not find:
            print("404")


# URL映射()
# 参考链接：https://blog.csdn.net/SL_logR/article/details/82711977
```

## 元素选择器

试题编号：	201809-3  
试题名称：	元素选择器

[返回目录](#目录)


```python
def 元素选择器():
    # 元素选择器
    # 输入
    n, m = map(int, input().split())
    doc = []
    sel = []
    # 结构化文档内容
    for i in range(n):
        doc.append(input())
    # 带查询的选择器
    for i in range(m):
        sel.append(input())
    # 解析文档结构
    cons = []
    for i in range(n):
        level = doc[i].count('.') // 2
        tag = ""
        tid = ""
        if len(doc[i].split()) == 1:
            tag = doc[i][level * 2:]
        else:
            left, right = doc[i].split()
            tag = left[level * 2:]  # 标签大小写不敏感
            tid = right  # id大小写敏感
        pline = -1
        for j in range(i - 1, 0 - 1, -1):
            if cons[j]["level"] == level - 1:
                pline = j + 1
                break
        cons.append({"tag": tag, "id": tid, "level": level, "pline": pline})  # 将信息存为字典添加到列表中
    # 元素选择器选择
    collection = []  # 结果保存列表
    for i in range(m):
        collection.append([])
        if len(sel[i].split()) == 1:  # 选择器不含空格
            if sel[i][0] != '#':  # 标签选择器
                for j in range(n):
                    if cons[j]["tag"].lower() == sel[i].lower():  # 标签大小写不敏感
                        collection[i].append(j + 1)
            else:  # id选择器
                for j in range(n):
                    if cons[j]["id"] == sel[i]:  # id大小写敏感
                        collection[i].append(j + 1)
        else:  # 后代选择器

            p = sel[i].split()
            for j in range(n):
                parent = j + 1
                k = len(p) - 1
                while k >= 0:  # 从后向前迭代检查是否匹配
                    match = False
                    if p[k][0] != '#':
                        if cons[parent - 1]["tag"].lower() == p[k].lower():
                            match = True
                        else:
                            if parent == j + 1 and k == len(p) - 1:  # 第一次必须匹配上不然直接退出
                                break
                    else:
                        if cons[parent - 1]["id"] == p[k]:
                            match = True
                        else:
                            if parent == j + 1 and k == len(p) - 1:
                                break
                    if match:
                        k -= 1
                        if k < 0:  # 匹配成功
                            collection[i].append(j + 1)
                            break
                    if cons[parent - 1]["pline"] == -1:  # 没有父节点了仍未匹配成功即匹配失败
                        break  # 匹配失败退出
                    parent = cons[parent - 1]["pline"]  # 取父节点继续检查匹配
    # 输出
    for x in collection:
        print(len(x), " ".join(map(str, x)))


# 元素选择器()
# 参考链接：https://blog.csdn.net/SL_logR/article/details/82729191
```

## CIDR合并

试题编号：	201812-3  
试题名称：	CIDR合并

[返回目录](#目录)


```python
def dvismerge(ip1: tuple, ip2: tuple) -> bool:  # 大小合并
    # True 1 > 2
    minlen = min(ip1[1], ip2[1])
    if ip1[0][:minlen] == ip2[0][:minlen]:  # 等价
        return True
    else:
        return False


def vismerge(ip_pre1: tuple, ip_pre2: tuple) -> tuple:  # 同级合并
    len1, len2 = ip_pre1[1], ip_pre2[1]
    ip1, ip2 = ip_pre1[0], ip_pre2[0]
    if len1 == len2 and ip1[:len1 - 1] == ip2[:len1 - 1] and ip1[len1 - 1] != ip2[len1 - 1]:
        # 1011-4 & 1010-4 -> 101-3
        return True, (ip1[:len1 - 1].ljust(32, '0'), len1 - 1)
    else:
        return False, 0


def formatIP(iplist: list, ip_split: list) -> str:
    op = re.compile(r'[\./]')
    for ip in iplist:
        d = re.split(op, ip)  # 按.和/拆分
        if ip.count("/") is 0:  # 省略长度型
            length = len(d)  # 不为为0的长(256)
            for _ in range(4 - length):
                d.append("0")
            d.append(str(length * 8))
            ip_split.append(list(map(int, d)))
        else:
            if len(d) is 5:  # 标准
                ip_split.append(list(map(int, d)))
            else:  # 省略后缀
                length = len(d) - 1  # 不为0的长度(256)
                tmp = d[:length]
                for _ in range(4 - length):
                    tmp.append("0")
                tmp.append(d[-1])
                ip_split.append(list(map(int, tmp)))


def binip(ip_split: list, bin_ip):
    for ip in ip_split:
        t = ''
        for i in range(4):
            t += bin(ip[i])[2:].rjust(8, '0')  # 前导补零
        bin_ip.append((t, ip[4]))


def CIDR合并():
    n = int(input())
    ip = []
    ip_split = []
    bin_ip = []  # 二进制补0及长度的元list
    for _ in range(n):
        ip.append(input())
    formatIP(ip, ip_split)  # 格式化
    ip_split.sort()  # 排序
    binip(ip_split, bin_ip)  # 排好序后的二进制
    # 从大到小合并
    i = 0
    while i < len(bin_ip) - 1:
        if dvismerge(bin_ip[i], bin_ip[i + 1]):
            del bin_ip[i + 1]
            i -= 1
        i += 1
    # 同级合并
    i = 0
    while i < len(bin_ip) - 1:
        tmpr = vismerge(bin_ip[i], bin_ip[i + 1])
        if tmpr[0]:
            del bin_ip[i]
            del bin_ip[i]
            bin_ip.insert(i, tmpr[1])
            i -= 2
        i += 1
    # 输出
    for bp, length in bin_ip:
        res_ip = '.'.join(list(map(lambda x: str(int(x, 2)),
                                   re.findall(r'.{8}', bp)))) + '/' + str(length)
        print(res_ip)


# CIDR合并()
# 参考链接：https://blog.csdn.net/q19149/article/details/99244415
```

## 损坏的RAID5

试题编号：	201903-3  
试题名称：	损坏的RAID5

[返回目录](#目录)


```python
def 损坏的RAID5():
    """
    b//s 条带号
    g=b//(s*(n-1)) 组号 校验盘号pid=n-1-g%n
    要将块号映射到磁盘号和该磁盘块号
    """
    n, s, l = map(int, input().split())
    infod = {}
    length = 0
    for i in range(l):
        k, content = input().split()
        infod[k] = content
        if i == 0:
            length = len(content) // 8 * (n - 1) - 1
    m = int(input())
    for i in range(m):
        b = int(input())  # 块号
        if b > length:
            print("-")
            continue
        g = b // (s * (n - 1))  # 组号
        pid = n - 1 - g % n  # 该组校验盘号√
        d = b % (s * (n - 1))  # 块号转换为0-
        did = (d // s + pid + 1) % n  # 磁盘号√
        dbid = g * s + b % s  # 在该磁盘的块号√
        startbit = dbid * 8
        if str(did) not in infod.keys():  # 缺盘
            if len(infod.keys()) == n - 1:  # 可计算
                c = 0
                for j in infod.values():
                    c ^= int(j[startbit:startbit + 8], 16)
                print(hex(c).upper()[2:])

            else:
                print("-")
        else:
            print(infod[str(did)][startbit:startbit + 8])


# 损坏的RAID5()
# 参考链接：https://blog.csdn.net/qq_39577481/article/details/103225826
```

## 字符画

试题编号：	201909-3  
试题名称：	字符画

[返回目录](#目录)


```python
defaback = [0, 0, 0]
reset = "[0m"
last = []
s = ""
prefix = "\\x1B"


def solveCol(c):
    if len(c) == 2:
        c += c[-1] * 6
    elif len(c) == 4:
        c = "#" + c[1] * 2 + c[2] * 2 + c[3] * 2
    l = [int(c[i:i + 2], 16) for i in range(1, 7, 2)]
    return l


# m, n = map(int, input().split())
# p, q = map(int, input().split())
# colormatrix = [[] for i in range(n)]
# for row in range(n):
#     for col in range(m):
#         colormatrix[row].append(solveCol(input()))
#         if (col + 1) % p == 0 and (row + 1) % q == 0:
#             srow = row // q
#             scol = col // p
#             suit = list(
#                 zip(*[colormatrix[k][l] for l in range(col - p + 1, col + 1) for k in range(row - q + 1, row + 1)]))

#             current = [sum(s) // len(s) for s in suit]

#             if srow == 0 and scol == 0:
#                 if current != defaback:
#                     d = "[48;2;" + ";".join(map(str, current)) + "m"
#                     t = ["\\x" + hex(ord(i))[2:].upper().zfill(2) for i in d]
#                     s += prefix + "".join(t)
#             else:
#                 if current == last:
#                     pass
#                 else:
#                     if current == defaback:
#                         s += "\\x1B\\x5B\\x30\\x6D"
#                     else:
#                         d = "[48;2;" + ";".join(map(str, current)) + "m"

#                         t = ["\\x" + hex(ord(i))[2:].upper().zfill(2) for i in d]
#                         s += prefix + "".join(t)
#             last = current
#             # 空格
#             s += "\\x20"
#             # 换行
#             if scol == m // p - 1:
#                 # 输出每行后判断是否重置
#                 if last != defaback:
#                     s += "\\x1B\\x5B\\x30\\x6D"
#                     last = defaback

#                 s += '''\\x0A'''
# print(s)

# 参考链接：https://blog.csdn.net/qq_39577481/article/details/103225865
```

## 化学方程式

试题编号：	201912-3  
试题名称：	化学方程式

[返回目录](#目录)


```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 化学方程式.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""
import re

pattern_ele = re.compile(r'[A-Z][a-z]?')  # 匹配化学元素的模式
pattern_lc = re.compile(r'^\d+')  # 匹配左边系数的模式
pattern_rc = re.compile(r'\d+$')  # 匹配右边系数的模式
pattern_term = re.compile(r'^[A-Z][a-z]?\d*')  # 匹配化学式中的项(元素部分)和系数
# 该函数用于处理系数和化学式
'''
if:处理测试编号点1-6
elif/else:处理测试编号点7-10
'''


def deal_formula(ceof, formula, dic):
    i = 0
    while i < len(formula):
        term = pattern_term.match(formula[i:])
        if term is not None:  # 处理未出现括号的情况
            term = term.group()
            if term[-1].isdigit():  # 处理如 Na2CO3 的情况
                r_ceof = pattern_rc.search(term)[0]
                ele = term[:-len(r_ceof)]
                deal_ele(ceof * int(r_ceof), ele, dic)
            else:  # 处理如 CaCO3 的情况
                deal_ele(ceof, term, dic)
            i += len(term)

        else:  # 处理出现括号以及括号嵌套的情况：如 （NH4)2CO3、Na(Au(CN)2)
            begin = i + 1
            end = begin
            close = 1
            while end < len(formula):
                if formula[end] == '(':
                    close += 1
                elif formula[end] == ')':
                    close -= 1
                if close == 0:
                    break
                end += 1
            if end + 1 < len(formula) and formula[end + 1].isdigit():
                r_ceof = pattern_lc.match(formula[end + 1:])[0]
                deal_formula(ceof * int(r_ceof), formula[begin:end], dic)
                end += len(r_ceof)
            else:
                deal_formula(ceof, formula[begin:end], dic)
            i = end + 1


# 处理元素                                 
def deal_ele(ceof, element, dic):
    dic[element] += ceof


# 处理表达式
def deal_expr(expr):
    ceof = 1
    formula = expr
    if expr[0].isdigit():
        ceof_str = pattern_lc.match(expr)[0]
        ceof = int(ceof_str)
        formula = expr[len(ceof_str):]
    return ceof, formula


# 校验化学方程式       
def checkEquation(equation):
    ele_dic = [{}, {}]
    expr_list = [[], []]
    exprs = equation.split("=")

    for i in range(2):
        eles = set(pattern_ele.findall(exprs[i]))
        for j in eles:
            ele_dic[i][j] = 0

    if ele_dic[0] != ele_dic[1]:
        print('N')
        return None
    for i in range(2):
        expr_list[i] = exprs[i].split('+')
        for j in expr_list[i]:
            ceof, formula = deal_expr(j)
            deal_formula(ceof, formula, ele_dic[i])
    if ele_dic[0] == ele_dic[1]:
        print('Y')
    else:
        print('N')


def 化学方程式():
    n = int(input())
    lists = []
    for i in range(n):
        equation = input()
        lists.append(equation)
    for i in lists:
        checkEquation(i)


# 化学方程式()
# 参考链接：https://www.jianshu.com/p/0594a7f5d4ad
```


## Markdown渲染器

试题编号：	202006-3  
试题名称：	Markdown渲染器

[返回目录](#目录)


```python
# 参考链接：https://www.cnblogs.com/137shoebills/p/13615919.html
```

**C++ 的代码题解**

```c++
#include<bits/stdc++.h>
using namespace std;
const int maxn=10000010;
int myget(char *b){
    char ch=getchar();
    if(ch==EOF)return -1;
    int i=0;
    while(ch!='\n'&&ch!=EOF){
        *(b+i)=ch;++i;
        ch=getchar();
    }return i;
}char a[21000000];
int main(){
    //freopen("init2.txt","r",stdin);
    int n,typ=0,lin=1,cnt=0,now=0,lonf=0;
    int w;cin>>w;getchar();
    int num=0;
    // 段落 1，项目 2，无类型0
    while((n=myget(a))!=-1){
        ++num;//cout<<num<<endl;
        int f=0;
        for(int i=0;i<n;++i){ if(a[i]!=' '){ f=1;break; } }
        //cout<<1<<' '<<lin<<' '<<cnt<<' '<<typ<<' '<<f<<endl;
        if(!f){
            lonf=1;
            continue;
        }
        if(a[0]=='*'&&a[1]==' '){
            if(lonf){
                if(now==1){typ=0;cnt=0;lin+=2;}
                if(cnt!=0){cnt=0;++lin;}
                if(typ!=0){typ=0;++lin;}
                lonf=0;
            }
            if(typ==2){if(cnt!=0||now==1)++lin;}
            else if(typ==1){++lin; if(cnt!=0)++lin;}
            typ=2; cnt=0; now=0;
            int l=0,r=-1;
            for(int i=2;i<n;++i)if(a[i]!=' '){l=i;break;}
            for(int i=n-1;i>=2;--i)if(a[i]!=' '){r=i;break;}
            if(r==-1)now=1;
            for(int i=l;i<=r;++i){
                if(cnt==0&&a[i]==' ')continue;
                if(cnt==0)cnt=3;
                ++cnt;
                if(cnt==w){cnt=0;++lin;}
            }
        }
        else if(typ==2&&(!lonf)&&a[0]==' '&&a[1]==' '){
            int l=0,r=-1;
            for(int i=2;i<n;++i)if(a[i]!=' '){l=i;break;}
            for(int i=n-1;i>=2;--i)if(a[i]!=' '){r=i;break;}
            if(cnt==w-1){++lin;cnt=0;}
            else if(cnt!=0)++cnt;
            for(int i=l;i<=r;++i){
                if(cnt==0&&a[i]==' ')continue;
                if(cnt==0)cnt=3;
                ++cnt;
                if(cnt==w){cnt=0;++lin;}
            }
        }
        else{
            if(lonf){
                if(now==1){typ=0;cnt=0;lin+=2;}
                if(cnt!=0){cnt=0;++lin;}
                if(typ!=0){typ=0;++lin;}
                lonf=0;
            }
            if(typ==1){
                if(cnt==w-1){++lin;cnt=0;}
                else if(cnt!=0)++cnt;
            }
            else if(typ==0)typ=1;
            else{ if(cnt!=0||now)++lin; ++lin;typ=1;cnt=0;}
            int l=0,r=-1;now=0;
            for(int i=0;i<n;++i)if(a[i]!=' '){l=i;break;}
            for(int i=n-1;i>=0;--i)if(a[i]!=' '){r=i;break;}
            for(int i=l;i<=r;++i){
                if(cnt==0&&a[i]==' ')continue;
                ++cnt;
                if(cnt==w){cnt=0;++lin;}
            }
        } //cout<<2<<' '<<lin<<' '<<cnt<<' '<<typ<<endl;
    }
    if(cnt==0&&!now)--lin;
    cout<<lin<<endl;
    return 0;
}
```
