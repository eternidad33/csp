#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: JSON查询.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""
# json
import json  # python 有内置json库


def JSOIN查询():
    n, m = map(int, input().split())
    # json解析
    json_str = ""
    for i in range(n):
        json_str += input()
    data = json.loads(json_str)  # json字符串加载为字典
    querys = []
    for i in range(m):
        querys.append(input().split("."))  # 根据.划分层次
    json_type = {
        str: "STRING",
        dict: "OBJECT"
    }
    for q in querys:
        try:  # 检查字典项的类型，将每个层次带入查询转为字符串 data["a"]["b"]并eval()执行
            if type(eval("data" + "".join(["[" + repr(x) + "]" for x in q]))) == str:
                print("STRING", eval("data" + "".join(["[" + repr(x) + "]" for x in q])))
            elif type(eval("data" + "".join(["[" + repr(x) + "]" for x in q]))) == dict:
                print("OBJECT")
        except Exception:  # 出现异常表示不存在
            print("NOTEXIST")


JSOIN查询()
