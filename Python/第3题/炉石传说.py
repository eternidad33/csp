#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: 炉石传说.py
@date: 2020-09-03
@Editor: PyCharm
@desc: 
"""


class summon:
    # 随从类
    def __init__(self, position, attack, health):
        self.position = position  # 位置，取值[1,7]
        self.attack = attack  # 攻击力
        self.health = health  # 生命力
        self.name = 'summon'  # 表明这是一个随从


class attack:
    # 攻击类
    def __init__(self, first, second):
        self.first = first  # 攻击的随从编号，取值[1,7]
        self.second = second  # 攻击对象编号，取值[0,7]，其中0表示攻击英雄
        self.name = 'attack'  # 表明攻击操作


class player:
    # 英雄类
    def __init__(self):
        self.health = 30  # 英雄生命力
        self.attack = 0  # 英雄的攻击力，没有用到
        self.people = []  # 英雄所拥有的随从
#    def fight(self)


def 炉石传说():
    global two
    n = int(input())
    data = []
    one = player()
    two = player()
    flag = 1  # 标记哪个英雄进行操作
    # 读取、预处理键盘输入数据
    for i in range(n):
        temp = input().split()
        if temp[0] == "summon":
            data.append(summon(int(temp[1]), int(temp[2]), int(temp[3])))
        elif temp[0] == 'attack':
            data.append(attack(int(temp[1]), int(temp[2])))
        else:
            data.append(temp[0])
    # 运行用户输入的操作
    for i in range(n):
        if flag == 1:  # 先出英雄操作
            if data[i] == 'end':
                flag = 2
            else:
                if data[i].name == 'summon':  # 上随从
                    one.people.insert(data[i].position - 1, data[i])
                elif data[i].name == 'attack':  # 攻击
                    if data[i].second == 0:
                        two.health = two.health - one.people[data[i].first - 1].attack
                    else:  # 注意，要把两者攻击后的随从生命算出来后，再检测随从是否消失
                        one.people[data[i].first - 1].health -= two.people[data[i].second - 1].attack
                        two.people[data[i].second - 1].health -= one.people[data[i].first - 1].attack
                        if two.people[data[i].second - 1].health <= 0:
                            two.people.pop(data[i].second - 1)
                        if one.people[data[i].first - 1].health <= 0:
                            one.people.pop(data[i].first - 1)
        else:
            if data[i] == 'end':
                flag = 1
            else:
                if data[i].name == 'summon':
                    two.people.insert(data[i].position - 1, data[i])
                elif data[i].name == 'attack':
                    if data[i].second == 0:
                        one.health = one.health - two.people[data[i].first - 1].attack
                    else:
                        two.people[data[i].first - 1].health -= one.people[data[i].second - 1].attack
                        one.people[data[i].second - 1].health -= two.people[data[i].first - 1].attack
                        if one.people[data[i].second - 1].health <= 0:
                            one.people.pop(data[i].second - 1)
                        if two.people[data[i].first - 1].health <= 0:
                            two.people.pop(data[i].first - 1)
    if one.health <= 0:
        print(-1)
    elif two.health <= 0:
        print(1)
    elif one.health > 0 and two.health > 0:
        print(0)
    print(one.health)
    length = len(one.people)
    if length == 0:
        print(0)
    else:
        temp = [length]
        for i in one.people:
            temp.append(i.health)
        print(" ".join(map(str, temp)))
    print(two.health)
    length = len(two.people)
    if length == 0:
        print(0)
    else:
        temp = [length]
        for i in two.people:
            temp.append(i.health)
        print(" ".join(map(str, temp)))


炉石传说()
