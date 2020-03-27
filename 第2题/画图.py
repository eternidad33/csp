n = int(input())
pnum = [[0] * 100 for _ in range(100)]
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            pnum[x][y] = 1
area = 0
for i in range(100):
    area += sum(pnum[i])
print(area)
