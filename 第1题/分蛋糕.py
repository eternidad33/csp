n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
t = 0
for i in a:
    t += i
    if t >= k:
        count += 1
        t = 0
if t != 0:
    count += 1
print(count)
