n = int(input())
a = list(map(int, input().split()))
b = 0
for i in range(n - 1):
    temp = abs(a[i] - a[i + 1])
    if temp > b:
        b = temp
print(b)
