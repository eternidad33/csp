def xiaoMingZhongPingGuo():
    N, M = map(int, input().split())
    T, k, P = 0, 0, 0
    for i in range(N):
        s = list(map(int, input().split()))
        a0, am = s[0], s[1:]
        T += a0
        am = map(abs, am)
        p = sum(am)
        T -= p
        if p > P:
            P = p
            k = i + 1
    print(T, k, P)


xiaoMingZhongPingGuo()

'''
输入
3 3
73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0
输出
167 2 23

输入
2 2
10 -3 -1
15 -4 0
输出
17 1 4
'''
