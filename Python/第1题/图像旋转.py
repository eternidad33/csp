# 图像旋转
n, m = map(int, (input().split()))
img = []
for i in range(n):
    a = list(map(int, input().split()))
    img.append(a)
for i in range(m):
    for j in range(n):
        print(img[j][m - 1 - i], end=" ")
    print()
