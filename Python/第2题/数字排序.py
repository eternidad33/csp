n = int(input())
ls = list(map(int, input().split()))
ls.sort()
a = {}
for i in ls:
    a[i] = ls.count(i)
a = sorted(a.items(), key=lambda item: item[1], reverse=True)
for j in a:
    print(j[0], j[1])
# 5 2 3 3 1 3 4 2 5 2 3 5
