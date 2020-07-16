n, k = map(int, input().split())
a = list(range(1, n + 1))
num = 1
while len(a) > 0:
    key_del = []
    # key_del存储要删除元素的索引
    for key, value in enumerate(a):
        # key存储的是a的索引
        if num % k == 0 or num % 10 == k:
            key_del.append(key)
        num += 1
    ac = 0
    # 由于删除元素列表的索引会跟随变化
    # ac存储的是删除元素的个数
    for key in key_del:
        del a[key - ac]
        ac += 1
        if len(a) == 1:
            print(a[0])
