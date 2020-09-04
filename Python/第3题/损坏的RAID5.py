#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 损坏的RAID5.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""


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


损坏的RAID5()
