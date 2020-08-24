def 二十四点(s0):
    for a in s0:
        a = a.replace("x", "*")
        a = a.replace("/", "//")
        sum_a = eval(a)
        if sum_a == 24:
            print("Yes")
        else:
            print("No")


# 录入数据
n = int(input())
s = []
for i in range(n):
    s.append(input())
二十四点(s)
