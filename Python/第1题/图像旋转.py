# 图像旋转
n, m = map(int, (input().split()))


def tuxiangxuanzhuan(row, col):
    img = []
    for i in range(row):
        a = list(map(int, input().split()))
        img.append(a)
    for i in range(col):
        for j in range(row):
            print(img[j][col - 1 - i], end=" ")
        print()


tuxiangxuanzhuan(n, m)
