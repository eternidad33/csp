n = int(input())
a = list(map(int, input().split()))
minn = abs(a[1] - a[0])
for i in range(n):
    for j in range(n):
        if i != j:
            temp = abs(a[i] - a[j])
            if temp < minn:
                minn = temp
print(minn)
