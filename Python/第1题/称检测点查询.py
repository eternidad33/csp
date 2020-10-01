#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 称检测点查询.py
@date: 2020-10-01
@Editor: PyCharm
@desc: 
"""


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


称检测点查询()
