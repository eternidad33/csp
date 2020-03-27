n, L, t = map(int, input().split())
POS = list(map(int, input().split()))
dire = [1] * n
for ti in range(t):
    for i in range(n):
        if POS[i] == L:
            dire[i] = -1
        if POS[i] == 0:
            dire[i] = 1
        POS[i] += dire[i]
    for i in range(n):
        for j in range(i + 1, n):
            if POS[i] == POS[j]:
                dire[i] = -dire[i]
                dire[j] = -dire[j]
print(" ".join(str(i) for i in POS))
