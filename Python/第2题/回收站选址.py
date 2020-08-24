#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 回收站选址.py
@date: 2020-08-24
@Editor: PyCharm
@desc: 
"""


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


回收站选址()
