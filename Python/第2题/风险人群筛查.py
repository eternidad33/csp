#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 风险人群筛查.py
@date: 2020-10-01
@Editor: PyCharm
@desc: 
"""


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


风险人群筛查()
