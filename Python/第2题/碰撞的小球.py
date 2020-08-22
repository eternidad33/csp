def 碰撞的小球(count, axis_len, time, position):
    dire = [1] * count  # 存储运动方向
    for ti in range(time):
        for p in range(count):
            if position[p] == axis_len:
                dire[p] = -1
            if position[p] == 0:
                dire[p] = 1
            position[p] += dire[p]
        # 查看小球是否相撞
        for p in range(count):
            for q in range(p + 1, count):
                if position[p] == position[q]:
                    dire[p] = -dire[p]
                    dire[q] = -dire[q]
    print(" ".join(str(i) for i in position))


n, L, t = map(int, input().split())
POS = list(map(int, input().split()))  # 存储每个小球位置
碰撞的小球(n, L, t, POS)
