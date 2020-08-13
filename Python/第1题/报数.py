#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 报数.py
@date: 2020-08-13
@Editor: PyCharm
@desc: 
"""
n = int(input())
count = 0
i = 0
l = [0, 0, 0, 0]
while count != n:
    i += 1
    if i % 7 == 0 or str(i).__contains__('7'):
        b = i % 4
        l[b] += 1
    else:
        count += 1
print(l[1])
print(l[2])
print(l[3])
print(l[0])
