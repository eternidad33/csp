#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 画图.py
@date: 2020-09-03
@Editor: PyCharm
@desc: 
"""


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


画图()

# 样例输入
# 4 2 3
# 1 0 0 B
# 0 1 0 2 0
# 1 0 0 A
# 样例输出
# AAAA
# A--A
# 样例输入
# 16 13 9
# 0 3 1 12 1
# 0 12 1 12 3
# 0 12 3 6 3
# 0 6 3 6 9
# 0 6 9 12 9
# 0 12 9 12 11
# 0 12 11 3 11
# 0 3 11 3 1
# 1 4 2 C
# 样例输出
# ................
# ...+--------+...
# ...|CCCCCCCC|...
# ...|CC+-----+...
# ...|CC|.........
# ...|CC|.........
# ...|CC|.........
# ...|CC|.........
# ...|CC|.........
# ...|CC+-----+...
# ...|CCCCCCCC|...
# ...+--------+...
# ................
