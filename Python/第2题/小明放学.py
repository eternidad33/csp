def 小明放学():
    r, y, g = map(int, input().split())
    n = int(input())
    tsum = 0
    for i in range(n):
        k, t = map(int, input().split())
        if k == 0:
            tsum += t
            continue
        if k == 1:
            t += g
        if k == 2:
            t += (r + g)
        nowtime = (t - tsum) % (r + y + g)
        # (t-tsum)为倒计时绝对时间取余一次循环时间得出当前循环距绿灯结束的时间
        if nowtime > g:
            tsum += (nowtime - g)
    print(tsum)


小明放学()
