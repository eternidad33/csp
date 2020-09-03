#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 路径解析.py
@date: 2020-09-03
@Editor: PyCharm
@desc: 
"""
# 路径解析
import re  # 引入正则表达式包


def 路径解析():
    n = int(input())
    pwd = input()  # 当前目录
    for i in range(n):
        route = input()
        # re.match()匹配字符串开头
        if re.match("/", route) is None:  # 相对路径和空字符串
            route = pwd + '/' + route
        route += "/"  # 结尾加‘/’方便替换，（必须在处理完空串后再加‘/’ ，空串10分）
        # re.sub()替换
        route = re.sub(r"//+", "/", route)  # 删去多个‘/’
        # 处理[.]
        route = re.sub(r"(/[.])+/", "/", route)  # [.]表示.不转义
        # 处理[..]
        # re.search()搜索
        while re.search(r"/[.]{2}/", route):
            route = re.sub(r"^(/[.]{2})+/", "/", route)  # 最开头根目录的上一级还是‘/’,^匹配开头
            if "/../" in route:  # 文件名不能只用字母数字匹配，要求还有.-_ （10分-20分）
                p = route.index("/../")
                x = route.rindex("/", 0, p)  # 从0到p范围找，找‘/../’前面的一个‘/’索引也就是上级目录
                route = route[0:x] + route[p + 3:]  # 去掉‘/上级目录/../’
        while len(route) > 1 and route[-1] == "/":  # 去除结尾‘/’
            route = route[:-1]
        print(route)


路径解析()
# 7
# /d2/d3
# /d2/d4/f1
# ../d4/f1
# /d1/./f1
# /d1///f1
# /d1/
# ///
# /d1/../../d2
