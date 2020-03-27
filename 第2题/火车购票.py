n = int(input())
m = list(map(int, input().split()))
num = []  # 存座位号
for i in range(20):
    temp = []
    for j in range(5):
        temp.append(i * 5 + j + 1)
    num.append(temp)
# print(num)

seats = [5 for i in range(20)]  # 每一行的剩余座位
p = -1  # 哪一行的座位数够用

res = [[] for i in range(n)]
a = 0  # res的下标

for i in m:
    for j in range(20):
        if seats[j] >= i:
            p = j
            break
    if p != -1:
        for k in range(5):
            if i == 0:
                break
            if num[p][k] != 0:
                res[a].append(num[p][k])
                num[p][k] = 0
                seats[p] -= 1
                i -= 1
        a += 1
    else:
        # 找不到行数
        for j in range(20):
            for k in range(5):
                if i == 0:
                    a += 1
                    break
                if num[j][k] != 0:
                    res[a].append(num[j][k])
                    num[j][k] = 0
                    seats[j] -= 1
                    i -= 1
            if i == 0:
                break
    p = -1
for i in res:
    for j in i:
        print(j, end=' ')
    print()
