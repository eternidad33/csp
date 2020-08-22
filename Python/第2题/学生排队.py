def 学生排队():
    n = int(input())
    q = list(range(1, n + 1))
    m = int(input())
    for i in range(m):
        k, t = map(int, input().split())
        after = q.index(k) + t  # 移动后的索引
        q.remove(k)  # 删除
        q.insert(after, k)  # 插入
    print(' '.join(map(str, q)))


学生排队()
