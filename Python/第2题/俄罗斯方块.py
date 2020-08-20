def eLuoSiFangKuai(tmap, shape, x):
    global i, j
    # 将形状转换为4行10列
    for i in range(4):
        shape[i] = [0] * (x - 1) + shape[i] + [0] * (6 - (x - 1))
    # 图形第一行最终落到的方格图对应的行数
    row1 = 0
    find = False
    for i in range(3):
        tmap.append([1] * 10)
    for i in range(15):
        for j in range(4):
            newline = [a + b for a, b in zip(tmap[i + j], shape[j])]
            if 2 in newline:
                row1 = i - 1
                find = True
                break
        if find:
            break
        if i == 14:
            row1 = 14
    # 拼接数据
    for i in range(4):
        tmap[row1 + i] = [a + b for a, b in zip(tmap[row1 + i], shape[i])]
    # 输出数据
    for i in range(15):
        print(' '.join(map(str, tmap[i])))


# 录入数据
tmap, shape = [], []
for i in range(15):
    temp_a = list(map(int, input().split()))
    tmap.append(temp_a)
for j in range(4):
    temp_b = list(map(int, input().split()))
    shape.append(temp_b)
x = int(input())
eLuoSiFangKuai(tmap, shape, x)

'''
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0 0
1 1 1 0 0 0 1 1 1 1
0 0 0 0 1 0 0 0 0 0
0 0 0 0
0 1 1 1
0 0 0 1
0 0 0 0
3
'''
