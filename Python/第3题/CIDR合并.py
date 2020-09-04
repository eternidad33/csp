#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: CIDR合并.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""
import re


def dvismerge(ip1: tuple, ip2: tuple) -> bool:  # 大小合并
    # True 1 > 2
    minlen = min(ip1[1], ip2[1])
    if ip1[0][:minlen] == ip2[0][:minlen]:  # 等价
        return True
    else:
        return False


def vismerge(ip_pre1: tuple, ip_pre2: tuple) -> tuple:  # 同级合并
    len1, len2 = ip_pre1[1], ip_pre2[1]
    ip1, ip2 = ip_pre1[0], ip_pre2[0]
    if len1 == len2 and ip1[:len1 - 1] == ip2[:len1 - 1] and ip1[len1 - 1] != ip2[len1 - 1]:
        # 1011-4 & 1010-4 -> 101-3
        return True, (ip1[:len1 - 1].ljust(32, '0'), len1 - 1)
    else:
        return False, 0


def formatIP(iplist: list, ip_split: list) -> str:
    op = re.compile(r'[\./]')
    for ip in iplist:
        d = re.split(op, ip)  # 按.和/拆分
        if ip.count("/") is 0:  # 省略长度型
            length = len(d)  # 不为为0的长(256)
            for _ in range(4 - length):
                d.append("0")
            d.append(str(length * 8))
            ip_split.append(list(map(int, d)))
        else:
            if len(d) is 5:  # 标准
                ip_split.append(list(map(int, d)))
            else:  # 省略后缀
                length = len(d) - 1  # 不为0的长度(256)
                tmp = d[:length]
                for _ in range(4 - length):
                    tmp.append("0")
                tmp.append(d[-1])
                ip_split.append(list(map(int, tmp)))


def binip(ip_split: list, bin_ip):
    for ip in ip_split:
        t = ''
        for i in range(4):
            t += bin(ip[i])[2:].rjust(8, '0')  # 前导补零
        bin_ip.append((t, ip[4]))


def CIDR合并():
    n = int(input())
    ip = []
    ip_split = []
    bin_ip = []  # 二进制补0及长度的元list
    for _ in range(n):
        ip.append(input())
    formatIP(ip, ip_split)  # 格式化
    ip_split.sort()  # 排序
    binip(ip_split, bin_ip)  # 排好序后的二进制
    # 从大到小合并
    i = 0
    while i < len(bin_ip) - 1:
        if dvismerge(bin_ip[i], bin_ip[i + 1]):
            del bin_ip[i + 1]
            i -= 1
        i += 1
    # 同级合并
    i = 0
    while i < len(bin_ip) - 1:
        tmpr = vismerge(bin_ip[i], bin_ip[i + 1])
        if tmpr[0]:
            del bin_ip[i]
            del bin_ip[i]
            bin_ip.insert(i, tmpr[1])
            i -= 2
        i += 1
    # 输出
    for bp, length in bin_ip:
        res_ip = '.'.join(list(map(lambda x: str(int(x, 2)),
                                   re.findall(r'.{8}', bp)))) + '/' + str(length)
        print(res_ip)


CIDR合并()
