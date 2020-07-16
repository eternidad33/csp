n = int(input())

s = input().split()
num = []
for i in range(n):
    s[i] = int(s[i])
    if s[i] not in num:
        num.append(s[i])
count = 0
for i in num:
    for j in num:
        if i + j == 0:
            count += 1
print(int(count / 2))
