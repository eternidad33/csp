def huoCheGouPiao(count, l):
    """火车购票

    思路：开辟一个二维数组存取剩余座位号
    """
    num = []  # 存座位号
    # 为num编号
    for i in range(20):
        temp = []
        for j in range(5):
            temp.append(i * 5 + j + 1)
        num.append(temp)

    seats = [5 for i in range(20)]  # 每一行的剩余座位
    p = -1  # 哪一行的座位数够用
    res = [[] for i in range(count)]  # 存取最后结果
    a = 0  # res的下标
    for i in l:
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
            # 找不到行数，则应该安排在编号最小的几个空座位中（不考虑是否相邻）
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


n = int(input())
m = list(map(int, input().split()))
huoCheGouPiao(n, m)
