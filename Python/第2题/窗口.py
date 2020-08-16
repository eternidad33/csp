def chuangkou(window, point_x, point_y):
    """识别窗口"""
    global i, j
    find = False
    for i, s in reversed(list(enumerate(window))):
        if s[0] <= point_x <= s[2] and s[1] <= point_y <= s[3]:
            print(s[4])
            last = window[i]
            for j in range(i, len(window) - 1):
                window[j] = window[j + 1]
            window[-1] = last
            find = True
            break
    if not find:
        print('IGNORED')


# 录入数据
n, m = map(int, input().split())
w = []
for i in range(n):
    w.append(list(map(int, input().split())))
    w[i].append(i + 1)
for j in range(m):
    x, y = list(map(int, input().split()))
    chuangkou(w, x, y)
