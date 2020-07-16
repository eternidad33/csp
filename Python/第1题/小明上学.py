r, y, g = list(map(int, input().split()))
n = int(input())
second = 0
for i in range(n):
    k, t = list(map(int, input().split()))
    if k == 0 or k == 1:
        second += t
    elif k == 2:
        second += (t + r)
    else:
        pass
print(second)
