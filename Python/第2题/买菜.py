def 买菜():
    n = int(input())
    H, W = [], []
    for i in range(n):
        H.append(list(map(int, input().split())))
    for i in range(n):
        W.append(list(map(int, input().split())))
    tlen = max(H[-1][-1], W[-1][-1])
    # 初始化时间轴
    timeLine = [0] * tlen
    for s, e in H:
        for i in range(s, e):
            timeLine[i] += 1
    for s, e in W:
        for i in range(s, e):
            timeLine[i] += 1
    print(timeLine.count(2))


买菜()
