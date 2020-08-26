#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 集合竞价.py
@date: 2020-08-26
@Editor: PyCharm
@desc: 
"""
# 集合竞价
# cancel是从前往后执行的，不能取消cancel
import sys


def 集合竞价():
    global count
    records = []
    delList = []
    for line in sys.stdin:
        record = list(line.split())
        records.append(record)
    # 根据cancel清除记录
    for record in records:
        if record[0] == "cancel":  # 用数组记录并del可能会删除两遍发生错误
            record[0] = ""
            records[int(record[1]) - 1][0] = ""  # 将要删除的记录和本条记录都清空
        elif record[0] in ("buy", "sell"):
            record[1] = float(record[1])  # 价格
            record[2] = int(record[2])  # 数量
    for i in reversed(range(len(records))):  # 删除撤销记录
        # print(i,records[i])
        if records[i][0] == "":
            records.remove(records[i])
    # print(records)
    # 构建buy，sell字典
    records.sort(key=(lambda x: x[1]), reverse=True)  # 根据价格从大到小排序
    buy_list = {}
    last_buy = 0
    for bs, price, count in records:
        if bs == "buy":
            last_buy += count
        buy_list[price] = last_buy  # 存入字典
    sell_list = {}
    last_sell = 0
    for bs, price, count in records[::-1]:  # 价格从小到大
        if bs == "sell":
            last_sell += count
        sell_list[price] = last_sell
    # 求竞价结果
    prices = list(buy_list)
    max_amount = 0
    best_price = 0
    for price in prices:
        if min(buy_list[price], sell_list[price]) > max_amount:  # 买入和卖出两者的最小值为成交数
            best_price = price
            max_amount = min(buy_list[price], sell_list[price])  # 记录当前最大成交数
    print("{:.2f} {}".format(best_price, max_amount))


集合竞价()
