#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 化学方程式.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""
import re

pattern_ele = re.compile(r'[A-Z][a-z]?')  # 匹配化学元素的模式
pattern_lc = re.compile(r'^\d+')  # 匹配左边系数的模式
pattern_rc = re.compile(r'\d+$')  # 匹配右边系数的模式
pattern_term = re.compile(r'^[A-Z][a-z]?\d*')  # 匹配化学式中的项(元素部分)和系数
# 该函数用于处理系数和化学式
'''
if:处理测试编号点1-6
elif/else:处理测试编号点7-10
'''


def deal_formula(ceof, formula, dic):
    i = 0
    while i < len(formula):
        term = pattern_term.match(formula[i:])
        if term is not None:  # 处理未出现括号的情况
            term = term.group()
            if term[-1].isdigit():  # 处理如 Na2CO3 的情况
                r_ceof = pattern_rc.search(term)[0]
                ele = term[:-len(r_ceof)]
                deal_ele(ceof * int(r_ceof), ele, dic)
            else:  # 处理如 CaCO3 的情况
                deal_ele(ceof, term, dic)
            i += len(term)

        else:  # 处理出现括号以及括号嵌套的情况：如 （NH4)2CO3、Na(Au(CN)2)
            begin = i + 1
            end = begin
            close = 1
            while end < len(formula):
                if formula[end] == '(':
                    close += 1
                elif formula[end] == ')':
                    close -= 1
                if close == 0:
                    break
                end += 1
            if end + 1 < len(formula) and formula[end + 1].isdigit():
                r_ceof = pattern_lc.match(formula[end + 1:])[0]
                deal_formula(ceof * int(r_ceof), formula[begin:end], dic)
                end += len(r_ceof)
            else:
                deal_formula(ceof, formula[begin:end], dic)
            i = end + 1


# 处理元素
def deal_ele(ceof, element, dic):
    dic[element] += ceof


# 处理表达式
def deal_expr(expr):
    ceof = 1
    formula = expr
    if expr[0].isdigit():
        ceof_str = pattern_lc.match(expr)[0]
        ceof = int(ceof_str)
        formula = expr[len(ceof_str):]
    return ceof, formula


# 校验化学方程式
def checkEquation(equation):
    ele_dic = [{}, {}]
    expr_list = [[], []]
    exprs = equation.split("=")

    for i in range(2):
        eles = set(pattern_ele.findall(exprs[i]))
        for j in eles:
            ele_dic[i][j] = 0

    if ele_dic[0] != ele_dic[1]:
        print('N')
        return None
    for i in range(2):
        expr_list[i] = exprs[i].split('+')
        for j in expr_list[i]:
            ceof, formula = deal_expr(j)
            deal_formula(ceof, formula, ele_dic[i])
    if ele_dic[0] == ele_dic[1]:
        print('Y')
    else:
        print('N')


def 化学方程式():
    n = int(input())
    lists = []
    for i in range(n):
        equation = input()
        lists.append(equation)
    for i in lists:
        checkEquation(i)


化学方程式()
