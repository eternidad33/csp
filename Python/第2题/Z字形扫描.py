#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: Z字形扫描.py
@date: 2020-08-18
@Editor: PyCharm
@desc: 
"""


def z(num):
    # up用于存储是否向上遍历，默认向上遍历
    up = True
    line = []
    i, j = 0, 0
    for _ in range(n * n):
        line.append(num[i][j])
        # 处理向上移动
        if up:
            # 处理碰到右边界，下移
            if j == n - 1:
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


n = int(input())
pnum = []
for i in range(n):
    pnum.append(list(map(int, input().split())))
z(pnum)
