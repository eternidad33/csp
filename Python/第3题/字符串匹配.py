#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 字符串匹配.py
@date: 2020-08-26
@Editor: PyCharm
@desc: 
"""


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


s1 = input()
flag = int(input())
n = int(input())
ls = []
for i in range(n):
    ls.append(input())
字符串匹配(s1, flag, ls)
