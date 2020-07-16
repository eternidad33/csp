n = int(input())
num = []
for i in range(10001):
    num += [0]
s = input().split()
for i in range(n):
    s[i] = int(s[i])
    num[s[i]] += 1
max_num = [0, 0]
for i in range(10001):
    if num[i] >= max_num[0]:
        max_num[0], max_num[1] = i, num[i]
print(max_num[0])
