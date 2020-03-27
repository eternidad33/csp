n, m = map(int, input().split())
bmap = []
amap = [[0] * m for _ in range(n)]
for i in range(n):
    bmap.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if 0 < i < n - 1 and bmap[i - 1][j] == bmap[i][j] and bmap[i][j] == bmap[i + 1][j]:
            amap[i - 1][j] = 1
            amap[i][j] = 1
            amap[i + 1][j] = 1
        if 0 < j < m - 1 and bmap[i][j - 1] == bmap[i][j] and bmap[i][j] == bmap[i][j + 1]:
            amap[i][j - 1] = 1
            amap[i][j] = 1
            amap[i][j + 1] = 1
for i in range(n):
    for j in range(m):
        if amap[i][j] == 1:
            bmap[i][j] = 0
        print(bmap[i][j], end=" ")
    print()
'''
4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3
'''
