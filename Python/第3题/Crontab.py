#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Vigilr
@file: Crontab.py
@date: 2020-09-04
@Editor: PyCharm
@desc: 
"""
# crontab
Days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Days_of_mons_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Month_string_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Weekday_string_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


def m_string2int(m):
    try:
        a = int(m)
        return a
    except:
        for i in range(12):
            if m.lower() == Month_string_list[i].lower():
                return i + 1


def w_string2int(w):
    try:
        a = int(w)
        return a
    except:
        for i in range(7):
            if w.lower() == Weekday_string_list[i].lower():
                return i


def ddmm(day, mon):
    # d为输入天的字符串，m为输入月份的字符串
    # start为开始的天，end为结束的天
    # 函数返回所有符合条件的天的list
    day_mon_set = []
    dayset = []
    days = day.split(',')
    for d in days:
        if d == '*':
            dayset = list(i + 1 for i in range(31))
        elif len(d.split('-')) != 1:
            s, e = list(map(int, d.split('-')))
            for i in range(s, e + 1):
                dayset.append(i)
        else:
            dayset.append(int(d))
    mons = mon.split(',')
    monset = []
    for m in mons:
        if m == '*':
            monset = list(i + 1 for i in range(12))
        elif len(m.split('-')) != 1:
            s, e = m.split('-')
            for i in range(m_string2int(s), m_string2int(e) + 1):
                monset.append(i)
        else:
            monset.append(m_string2int(m))
    for x in monset:
        for y in dayset:
            day_mon_set.append(x * 100 + y)
    return day_mon_set


def MMHH(mm, hh):
    min_hour_set = []
    minset = []
    hourset = []
    mms = mm.split(',')
    for m in mms:
        if m == '*':
            minset = list(i for i in range(60))
        elif len(m.split('-')) != 1:
            s, e = list(map(int, m.split('-')))
            for i in range(s, e + 1):
                minset.append(i)
        else:
            minset.append(int(m))
    hhs = hh.split(',')
    for h in hhs:
        if h == '*':
            hourset = list(i for i in range(24))
        elif len(h.split('-')) != 1:
            s, e = list(map(int, h.split('-')))
            for i in range(s, e + 1):
                hourset.append(i)
        else:
            hourset.append(int(h))
    for h in hourset:
        for m in minset:
            min_hour_set.append(h * 100 + m)
    return min_hour_set


def day_of_week(ww):
    if ww == '*':
        return list(i for i in range(7))
    else:
        dset = []
        wws = ww.split(',')
        for w in wws:
            if len(w.split('-')) != 1:
                s, e = w.split('-')
                for i in range(w_string2int(s), w_string2int(e) + 1):
                    dset.append(i)
            else:
                dset.append(w_string2int(w))
        return dset


def check(ymhdmw):
    normal = []
    for X in ymhdmw:
        year, mon_day, hour_min, weekday, com = X
        # 检查是否在设置的时间范围内
        time = year * 100000000 + mon_day * 10000 + hour_min
        if time < start or time >= end:
            continue

        # 检查每个月的日期数是否正常
        if (year % 4) == 0:
            daysbefore = sum(Days_of_mons_in_leap_year[0:mon_day // 100 - 1])
            if (Days_of_mons_in_leap_year[mon_day // 100 - 1] < (mon_day % 100)):
                continue
        else:
            daysbefore = sum(Days_of_month[0:mon_day // 100 - 1])
            if Days_of_month[mon_day // 100 - 1] < (mon_day % 100):
                continue

        # 检查星期数是否正常
        years_from_1970 = year - 1970
        num_of_leap_year = (years_from_1970 + 1) // 4
        days_from_197011 = years_from_1970 * 365 + num_of_leap_year + daysbefore + mon_day % 100 - 1
        if ((days_from_197011 % 7) + 4) % 7 == weekday:
            normal.append([time, command])
    return normal


def Crontab():
    global start, end, command
    n, start, end = list(map(int, input().split()))
    crontab = []
    startyear = start // 100000000
    endyear = end // 100000000
    for i in range(n):
        minutes, hours, day_of_month, month, dayofweek, command = input().split()
        minhoueset = MMHH(minutes, hours)
        daymonset = ddmm(day_of_month, month)
        week = day_of_week(dayofweek)
        ymhdmw = []
        for i in range(startyear, endyear + 1):
            for mh in minhoueset:
                for dm in daymonset:
                    for w in week:
                        ymhdmw.append([i, dm, mh, w, command])
        crontab.append(check(ymhdmw))
    crontab1 = []
    for X in crontab:
        for x in X:
            crontab1.append(x)
    crontab2 = sorted(crontab1, key=lambda x: x[0])
    for i in crontab2:
        print(i[0], i[1])


Crontab()
