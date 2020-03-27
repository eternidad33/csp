n, m = map(int, input().split())
w = []
for i in range(n):
    w.append(list(map(int, input().split())))
    w[i].append(i + 1)
for j in range(m):
    x, y = list(map(int, input().split()))
    find = False
    for i, s in reversed(list(enumerate(w))):
        if s[0] <= x <= s[2] and s[1] <= y <= s[3]:
            print(s[4])
            last = w[i]
            for j in range(i, len(w) - 1):
                w[j] = w[j + 1]
            w[-1] = last
            find = True
            break
    if not find:
        print('IGNORED')
