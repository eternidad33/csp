#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 稀疏向量.py
@date: 2020-08-24
@Editor: PyCharm
@desc: 
"""


def 稀疏向量():
    # # 方法1，使用列表，运行超时，60分
    # n, p, q = map(int, input().split())
    # u = [0 for _ in range(n)]
    # v = [0 for _ in range(n)]
    # for i in range(p):
    #     index, value = map(int, input().split())
    #     u[index - 1] = value
    # for j in range(q):
    #     index, value = map(int, input().split())
    #     v[index - 1] = value
    # uv = 0  # 内积
    # for k in range(n):
    #     uv += u[k] * v[k]
    # print(uv)

    # 方法2，使用字典，运行超时，60分
    n, p, q = map(int, input().split())
    u = {}  # 字典存储u向量索引对应的值
    for i in range(p):
        index, value = map(int, input().split())
        u[index] = value
    uv = 0  # 内积
    for j in range(q):
        index, value = map(int, input().split())
        if index in u.keys():
            uv += value * u[index]
    print(uv)


稀疏向量()
