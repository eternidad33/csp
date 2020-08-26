#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 节日.py
@date: 2020-08-26
@Editor: PyCharm
@desc: 
"""

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


节日()
