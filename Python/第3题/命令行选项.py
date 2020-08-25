#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 命令行选项.py
@date: 2020-08-25
@Editor: PyCharm
@desc: 
"""


def 命令行选项(ops, count, cmd_list):
    ops += " "
    global i
    uop = []  # 存储无参选项
    hop = []  # 存储有参选项
    for i in range(len(ops) - 1):
        if ops[i + 1] == ":":
            hop.append(ops[i])
        else:
            uop.append(ops[i])
    for i in range(count):
        # 将命令分割
        cmd = cmd_list[i]
        d = {}
        j = 1
        while j < len(cmd):
            # 如果为参数选项
            if cmd[j][0] == "-" and len(cmd[j]) == 2:
                if cmd[j][1] in uop:  # 无参选项处理
                    d[cmd[j][1]] = "#"
                    j += 1
                elif cmd[j][1] in hop and j + 1 < len(cmd):  # 有参选项处理
                    d[cmd[j][1]] = cmd[j + 1]
                    j += 2
                else:  # 其他选项错误退出循环
                    break
            else:
                break
        keys = list(set(d.keys()))
        keys.sort()
        print("Case " + str(i + 1) + ":", end="")
        for key in keys:
            print(" -" + key, end="")
            if d[key] != "#":
                print(" " + d[key], end="")
        print()


options = input()
n = int(input())
cmds = []
for i in range(n):
    cmds.append(list(input().split()))
命令行选项(options, n, cmds)

"""
样例输入
albw:x
4
ls -a -l -a documents -b
ls
ls -w 10 -x -w 15
ls -a -b -c -d -e -l

样例输出
Case 1: -a -l
Case 2:
Case 3: -w 15 -x
Case 4: -a -b
"""
