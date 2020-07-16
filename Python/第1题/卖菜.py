n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if i == 0:
        temp = (a[i] + a[i + 1]) // 2
        b.append(temp)
    elif i == n - 1:
        temp = (a[i] + a[i - 1]) // 2
        b.append(temp)
    else:
        temp = (a[i - 1] + a[i] + a[i + 1]) // 3
        b.append(temp)
for i in b:
    print(i, end=" ")
