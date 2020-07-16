n = int(input())
a = list(map(int, input().split()))

mid = (a[(n - 1) // 2] + a[n // 2]) / 2
if int(mid) == mid:
    mid = int(mid)

print("{} {} {}".format(max(a), round(mid, 1), min(a)))
