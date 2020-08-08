n = int(input())
a = list(map(int, input().split()))
t = False
for i in a:
    max_num, min_num = 0, 0
    for j in a:
        if j < i:
            min_num += 1
        if j > i:
            max_num += 1
    if min_num == max_num:
        print(i)
        t = True
        break
if not t:
    print(-1)
