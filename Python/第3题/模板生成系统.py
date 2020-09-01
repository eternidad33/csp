#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 模板生成系统.py
@date: 2020-09-01
@Editor: PyCharm
@desc: 
"""
# 模板生成系统
# re正则表达式匹配
import re


def 模板生成系统():
    global var_dict
    m, n = map(int, input().split())
    temple = []  # 模板
    for i in range(m):
        temple.append(input())
    var_dict = dict()  # 变量
    for i in range(n):
        var, value = input().split(" ", 1)
        var_dict[var] = eval(value)  # 清除引号

    def trans(matched):  # 变量替换值函数
        var = matched.group('var')
        if var in var_dict:
            return var_dict[var]
        else:
            return ""

    for i in range(len(temple)):
        print(re.sub(r'{{ (?P<var>\w*) }}', trans, temple[i]))
        # re替换方法，匹配{{  }}格式(?P<var>)命名组，\w匹配小写字母数字和下划线，*表示匹配一个或多个\w
        # trans匹配方法，调用函数将命名组的var替换成值


模板生成系统()

# 11 2
# <!DOCTYPE html>
# <html>
# <head>
# <title>User {{ name }}</title>
# </head>
# <body>
# <h1>{{ name }}</h1>
# <p>Email: <a href="mailto:{{ email }}">{{ email }}</a></p>
# <p>Address: {{ address }}</p>
# </body>
# </html>
# name "David Beckham"
# email "david@beckham.com"
