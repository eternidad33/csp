def riQiJiSuan(year, day):
    mon = 0
    md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 判断闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        md[2] = 29
    for i in md:
        if day - i > 0:
            day -= i
            mon += 1
        else:
            break
    print(mon)
    print(day)


y = int(input())
d = int(input())
riQiJiSuan(y, d)
