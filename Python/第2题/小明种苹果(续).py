def 小明种苹果续():
    n = int(input())
    T, D, E = 0, 0, 0
    lost_index = []
    for i in range(n):
        s = list(map(int, input().split()))
        a0, am = s[0], s[1:]
        b = False
        temp = am[0]
        for j in am:
            if j > 0:
                if j != temp:
                    temp = j
                    b = True
            else:
                temp += j
        if b:
            lost_index.append(i)
            D += 1
        T += temp
    t = [0] * n
    for i in lost_index:
        t[i] = 1
    if t[-2] == t[-1] == t[0] == 1:
        E += 1
    if t[-1] == t[0] == t[1] == 1:
        E += 1
    for i in range(1, n - 1):
        if t[i - 1] == t[i] == t[i + 1] == 1:
            E += 1
    print(T, D, E)


小明种苹果续()
'''
输入
4
4 74 -7 -12 -5
5 73 -8 -6 59 -4
5 76 -5 -10 60 -2
5 80 -6 -15 59 0
输出
222 1 0
输入
5
4 10 0 9 0
4 10 -2 7 0
2 10 0
4 10 -3 5 0
4 10 -1 8 0
输出
39 4 2
'''
