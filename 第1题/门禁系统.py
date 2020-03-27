n = int(input())
s = input().split()
a = []
for i in range(n):
    s[i] = int(s[i])
    a.append(s[i])
c = []
for j in range(len(a)):
    count = 1
    for k in range(j):
        if a[j] == a[k]:
            count += 1
    c.append(count)
for t in c:
    print(t, end=" ")
