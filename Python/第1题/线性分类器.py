#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 线性分类器.py
@date: 2020-08-13
@Editor: PyCharm
@desc: 
"""


def xianXingFenLeiQi():
    n, m = map(int, input().split())
    datas = []
    # 录入数据
    for i in range(n):
        data = input().split()
        data[0] = int(data[0])
        data[1] = int(data[1])
        datas.append(data)
    flags = []
    for i in range(m):
        line = list(map(int, input().split()))
        flag = True
        # 判断第一个点的位置
        r1 = datas[0][0] * line[1] + datas[0][1] * line[2] + line[0]
        if r1 > 0 and datas[0][2] == 'A':
            AisUp = True
        elif r1 < 0 and datas[0][2] != 'A':
            AisUp = True
        else:
            AisUp = False

        for j in range(1, n):
            result = datas[j][0] * line[1] + datas[j][1] * line[2] + line[0]
            if AisUp:
                if result > 0 and datas[j][2] == 'A':
                    flag = True
                elif result > 0 and datas[j][2] == 'B':
                    flag = False
                    break
                elif result < 0 and datas[j][2] == "A":
                    flag = False
                    break
                elif result < 0 and datas[j][2] == "B":
                    flag = True
            else:
                if result < 0 and datas[j][2] == 'A':
                    flag = True
                elif result < 0 and datas[j][2] == 'B':
                    flag = False
                    break
                elif result > 0 and datas[j][2] == "A":
                    flag = False
                    break
                elif result > 0 and datas[j][2] == "B":
                    flag = True
        flags.append(flag)
    for flag in flags:
        if flag:
            print("Yes")
        else:
            print("No")


xianXingFenLeiQi()

# def line_sort(in_list):
#     flag_gt = -1
#     flag_lt = -1
#     for i in p_list:
#         if (in_list[0] + in_list[1] * int(i[0]) + in_list[2] * int(i[1])) >= 0:
#             if flag_gt == -1:
#                 flag_gt = i[2]
#                 flag_lt = 'B' if i[2] == 'A' else 'A'
#             if i[2] != flag_gt:
#                 print('No')
#                 return
#
#         elif (in_list[0] + in_list[1] * int(i[0]) + in_list[2] * int(i[1])) < 0:
#             if flag_lt == -1:
#                 flag_lt = i[2]
#                 flag_gt = 'B' if i[2] == 'A' else 'A'
#             if i[2] != flag_lt:
#                 print('No')
#                 return
#     print('Yes')
#
#
# n, m = map(int, input().split())
#
# p_list = []
# for i in range(n):
#     p_list.append(list(input().split()))
#
# for i in range(m):
#     line = list(map(int, input().split()))
#     line_sort(line)

# 9 3
# 1 1 A
# 1 0 A
# 1 -1 A
# 2 2 B
# 2 3 B
# 0 1 A
# 3 1 B
# 1 3 B
# 2 0 A
# 0 2 -3
# -3 0 2
# -3 1 1
