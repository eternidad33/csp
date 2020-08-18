#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: test.py
@date: 2020-08-18
@Editor: PyCharm
@desc: 
"""
n = int(input())
pnum = []
for i in range(n):
    pnum.append(list(map(int, input().split())))
i, j = 0, 0
line = []
up = True
for t in range(n * n):
    line.append(pnum[i][j])
    if up:
        if j == n - 1:
            i += 1
            up = False
        elif i == 0:
            j += 1
            up = False
        else:
            j += 1
            i -= 1
    else:
        if i == n - 1:
            j += 1
            up = True
        elif j == 0:
            i += 1
            up = True
        else:
            j -= 1
            i += 1
print(" ".join(map(str, line)))
